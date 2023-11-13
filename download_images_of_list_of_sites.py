import random
import requests
from PIL import Image
import os
import sys

# Ask the user for the path to the list of image URLs.
image_urls_path = input('Enter the path to the list of image URLs: ')

# Read the image URLs from the file.
with open(image_urls_path, 'r') as f:
    image_urls = [line.strip() for line in f.readlines()]

# Select 20 random image URLs.
random_image_urls = random.sample(image_urls, 20)

def download_image(image_url, output_path):
  """Downloads an image from the given URL and saves it to the given output path.

  Args:
    image_url: The URL of the image to download.
    output_path: The path to save the downloaded image to.
  """

  # Fix the error by adding a `check_existence=False` argument to the `requests.get()` call. This will prevent the error from being raised if the image does not exist.
  response = requests.get(image_url, check_existence=False)
  if response.status_code == 200:
    with open(output_path, 'wb') as f:
      f.write(response.content)
  else:
    print(f'Failed to download image from {image_url}: {response.status_code}')

def get_image_dimensions(image_path):
  """Gets the dimensions of the given image file.

  Args:
    image_path: The path to the image file.

  Returns:
    A tuple of (width, height) in pixels.
  """

  image = Image.open(image_path)
  width, height = image.size
  return width, height

def get_image_alt_text(image_path):
  """Gets the alt text of the given image file.

  Args:
    image_path: The path to the image file.

  Returns:
    The alt text of the image file, or an empty string if the alt text is not present.
  """

  image = Image.open(image_path)
  alt_text = image.info.get('alt', '')
  return alt_text

def generate_report(image_urls, output_path):
  """Generates a report of the given image URLs.

  The report will include the following information for each image URL:
    * URL
    * File type (e.g. JPEG, PNG, etc.)
    * Dimensions (px, h x w)
    * Alt text
    * Any other information that may hinder Google's ranking (e.g. image is too small, image is not WebP, etc.)

  Args:
    image_urls: A list of image URLs.
    output_path: The path to save the report to.
  """

  with open(output_path, 'w') as f:
    f.write('Image URL,File Type,Dimensions,Alt Text,Hinder Google Ranking\n')
    for image_url in image_urls:
      # Parse the domain from the image URL.
      domain = image_url.split('/')[2]

      # Create a folder for the domain if it doesn't exist.
      output_folder = f'{domain}_images'
      if not os.path.exists(output_folder):
        os.makedirs(output_folder)

      # Download the image to the output folder.
      image_path = os.path.join(output_folder, f'image_{image_url}.jpg')
      download_image(image_url, image_path)

      # If the image was downloaded successfully, get the image dimensions and alt text.
      if os.path.exists(image_path):
        width, height = get_image_dimensions(image_path)
        alt_text = get_image_alt_text(image_path)

        # Check if the image is too small.
        if width < 1200 or height < 628:
          hinder_google_ranking = 'Image is too small.'
        else:
          hinder_google_ranking = '-'

        # Check if the image is WebP.
        if not image_path.endswith('.webp'):
          hinder_google_ranking += ' Image
