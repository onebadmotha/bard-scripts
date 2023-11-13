import requests
from bs4 import BeautifulSoup
import imghdr
import os

def get_image_urls(url):
  """Gets a list of all the image URLs on a website.

  Args:
    url: The URL of the website.

  Returns:
    A list of all the image URLs on the website.
  """

  response = requests.get(url)
  soup = BeautifulSoup(response.content, "html.parser")

  image_urls = []
  for img in soup.find_all("img"):
    image_urls.append(img["src"])

  return image_urls

def write_image_types_to_file(image_urls, output_file):
  """Writes the image types of a list of image URLs to a file.

  Args:
    image_urls: A list of image URLs.
    output_file: The path to the output file.
  """

  # Create the output directory if it does not exist.
  output_dir = os.path.dirname(output_file)
  if not os.path.exists(output_dir):
    os.makedirs(output_dir)

  # Write the image types to the output file.
  with open(output_file, "w") as f:
    for image_url in image_urls:
      image_type = imghdr.what(image_url)
      f.write(f"{image_url}: {image_type}\n")

if __name__ == "__main__":
  website_url = "https://www.the-saleroom.com/"

  image_urls = get_image_urls(website_url)
  output_file = "/home/rob/tmp/image_types.txt"

  write_image_types_to_file(image_urls, output_file)
