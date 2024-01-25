import requests
from bs4 import BeautifulSoup

def download_images(page_url, output_directory):
  """Downloads all of the images from the given webpage to the given output directory."""

  response = requests.get(page_url)
  soup = BeautifulSoup(response.content, 'html.parser')

  # Get all of the image tags on the webpage
  image_tags = soup.find_all('img')

  # Download each image
  for image_tag in image_tags:
    if hasattr(image_tag, 'src'):
      image_url = image_tag['src']

      # Check if the image is hosted on the Azure CDN
      if not image_url.startswith('https://portal-images.azureedge.net/'):
        print('Image is not hosted on the Azure CDN:', image_url)

      # Check if the image is accessible
      try:
        requests.get(image_url)
      except requests.exceptions.RequestException as e:
        print('Image is not accessible:', image_url, e)

      # Download the image if it is hosted on the Azure CDN and accessible
      if image_url.startswith('https://portal-images.azureedge.net/') and requests.get(image_url).status_code == 200:
        image_response = requests.get(image_url)

        with open(os.path.join(output_directory, image_url), 'wb') as f:
          f.write(image_response.content)

if __name__ == '__main__':
  # Get the page URL from the user
  page_url = input('Enter the page URL: ')

  # Get the output directory from the user
  output_directory = input('Enter the output directory: ')

  # Download the images
  download_images(page_url, output_directory)
