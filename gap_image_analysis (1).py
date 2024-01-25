import requests
from bs4 import BeautifulSoup
import random
import time

def get_random_page_from_section(section_url):
  response = requests.get(section_url, headers={'User-Agent': 'Googlebot'})
  soup = BeautifulSoup(response.content, 'html.parser')

  # Get all the links on the page
  links = soup.find_all('a', href=True)

  # Choose a random link from the page
  random_link = random.choice(links)

  # Return the URL of the random link
  return random_link['href']

def download_image(image_url):
  response = requests.get(image_url)

  # Get the size of the image in bytes
  image_size = response.headers['Content-Length']

  # Save the image to a file
  with open(image_url.split('/')[-1], 'wb') as f:
    f.write(response.content)

  return image_size

def generate_report(page_url, image_url1, image_size1, image_url2, image_size2, time_to_download_image1, time_to_download_image2):
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

def debug_code():
  # Test the code to make sure it is working as expected

  # Get a random page from each section of the GAP sites
  gap_sites = ['the-saleroom.com', 'i-bidder.com', 'bidspotter.com', 'bidspotter.co.uk', 'lot-tissimo.com']
  section_urls = ['https://www.the-saleroom.com/en-gb/auction-categories', 'https://www.i-bidder.com/auction-categories', 'https://www.bidspotter.com/auction-categories', 'https://www.bidspotter.co.uk/auction-categories', 'https://www.lot-tissimo.com/auction-categories']

  # Download 2 images from each page chosen
  for section_url in section_urls:
    page_url = get_random_page_from_section(section_url)

    image_url1 = None
    image_url2 = None

    # Find the first image on the page
    response = requests.get(page_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    images = soup.find_all('img', src=True)

    if images:
      image_url1 = images[0]['src']

    # Find the second image on the page
    if image_url1:
      response = requests.get(page_url)
      soup = BeautifulSoup(response.content, 'html.parser')

      images = soup.find_all('img', src=True)

      if images:
        image_url2 = images[1]['src']

    # Download the images
    if image_url1:
      image_size1 = download_image(image_url1)

    if image_url2:
      image_size2 = download_image(image_url2)

    # Generate a report for the page
    report = generate_report(page_url, image_url1, image_size1, image_url2, image_size2)

    # Print the report
    print(report)

if __name__ == '__main__':
  debug_code()
