import requests
from bs4 import BeautifulSoup
import random
import time

def get_random_page_from_section(section_url, schema):
  """Returns a random page from the given section of the GAP sites, using the specified schema."""

  response = requests.get(section_url)
  soup = BeautifulSoup(response.content, 'html.parser')

  # Get all the links on the page
  links = soup.find_all('a', href=True)

  # Choose a random link from the page
  random_link = random.choice(links)

  # Get the full URL of the random link, using the specified schema
  full_url = schema.format(random_link['href'])

  return full_url

def download_image(image_url):
  """Downloads the image at the given URL to the local disk."""

  response = requests.get(image_url)

  # Save the image to a file
  with open(image_url.split('/')[-1], 'wb') as f:
    f.write(response.content)

def generate_report(page_url, image_url1, image_size1, image_url2, image_size2, time_to_download_image1, time_to_download_image2):
  """Generates a report for the given page, including the following metrics:

    * The page URL
    * The image URL
    * The image size according to the code
    * How long it took to get the first image
    * How long it took to get the second image
    * How large they were when downloaded
  """

  report = f"""
Page URL: {page_url}
Image URL 1: {image_url1}
Image Size 1: {image_size1} bytes
Image URL 2: {image_url2}
Image Size 2: {image_size2} bytes
Time to download image 1: {time_to_download_image1} seconds
Time to download image 2: {time_to_download_image2} seconds
"""

  return report

if __name__ == '__main__':
  # Define the schemas for the GAP pages
  category_schema = 'https://www.<domain>.com/en-gb/for-sale/<category>/<sub-category>'
  auction_house_schema = 'https://www.<domain>.com/en-gb/auction-catalogues/<auction house>'
  auction_house_event_schema = 'https://www.the-saleroom.com/en-gb/auction-catalogues/<auction house>/<auction house event>'
  auction_house_lot_schema = 'https://www.the-saleroom.com/en-gb/auction-catalogues/<auction house>/<auction house event>/lot-<lot id>'

  # Get a random page from each section of the GAP sites
  section_urls = ['https://www.the-saleroom.com/en-gb/auction-categories', 'https://www.i-bidder.com/auction-categories', 'https://www.bidspotter.com/auction-categories', 'https://www.bidspotter.co.uk/auction-categories', 'https://www.lot-tissimo.com/auction-categories']

  # Generate a report for each page
  report = ''

  for section_url in section_urls:
    # Get the schema for the current section
    schema = auction_house_schema if section_url == 'https://www.the-saleroom.com/en-gb/auction-categories' else category_schema

    # Get a random page from the current section
    page_url = get_random_page_from_section(section_url, schema)

    # Download 2 random images from the page
    image_urls = []
    time_to_download_images = []

    for i in range(2):
      image_url = None

      # Find an image on the page
      response = requests.get(page_url)
      soup = BeautifulSoup(response.content, 'html.parser')

      images = soup.find_all('img', src=True)

      if images:
        image_url = images[i]['src']

      # Download the image
      if image_url:
        start_time = time.time()
        download_image(image_url)
        end_
