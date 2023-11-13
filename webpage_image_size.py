import datetime
import requests
import bs4
from PIL import Image

def get_all_images(webpage_url):
  """Downloads all the images from a webpage.

  Args:
    webpage_url: The URL of the webpage to download the images from.

  Returns:
    A list of Image objects, one for each image on the webpage.
  """

  response = requests.get(webpage_url)
  soup = bs4.BeautifulSoup(response.content, "html.parser")

  images = []
  for img_tag in soup.find_all("img"):
    try:
      img_url = img_tag["src"]
    except KeyError:
      continue

    try:
      img_response = requests.get(img_url)
      img = Image.open(img_response.content)
    except Exception as e:
      print(f"Error downloading image {img_url}: {e}")
      continue
    images.append(img)

  return images

def write_image_sizes_to_file(images, filename):
  """Writes the URL and dimensions of each image to a file.

  Args:
    images: A list of Image objects.
    filename: The name of the file to write to.
  """

  with open(filename, "w") as f:
    for image in images:
      image_url = image.url
      image_width, image_height = image.size
      f.write(f"{image_url} {image_width} {image_height}\n")

def main():
  """Asks the user for a webpage, downloads all the images, and writes the URL
  and dimensions of each image to a file.
  """

  webpage_url = input("Enter the URL of the webpage: ")
  images = get_all_images(webpage_url)

  # Create a filename based on the website name and the current date.
  website_name = webpage_url.split("//")[1].split(".")[0]
  date = datetime.datetime.today().strftime("%Y-%m-%d")
  filename = f"{website_name}_imageSizes_{date}.txt"

  write_image_sizes_to_file(images, filename)

  print(f"Image sizes written to file: {filename}")

if __name__ == "__main__":
  main()
