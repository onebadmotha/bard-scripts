import gzip
import os
import requests
from bs4 import BeautifulSoup

def create_temp_file():
  """Creates a temporary file."""

  temp_file = tempfile.NamedTemporaryFile(delete=False)
  return temp_file

def write_to_temp_file(temp_file, data):
  """Writes data to a temporary file."""

  temp_file.write(data.encode('utf-8'))
  temp_file.flush()

def read_from_temp_file(temp_file):
  """Reads data from a temporary file."""

  data = temp_file.read().decode('utf-8')
  return data

def parse_sitemap(sitemap_url, temp_file):
  """Parses a gzipped sitemap and writes the results to a temporary file."""

  sitemap_response = requests.get(sitemap_url)
  sitemap_content = gzip.decompress(sitemap_response.content)

  write_to_temp_file(temp_file, sitemap_content)

def scan_page_for_alt_text(page_url, image_url, temp_file):
  """Scans a webpage for alt text for a given image URL and writes the results to a temporary file."""

  page_response = requests.get(page_url)
  page_content = page_response.content

  write_to_temp_file(temp_file, page_content)

  # Read the page content from the temporary file
  page_content = read_from_temp_file(temp_file)

  # Create a BeautifulSoup object
  soup = BeautifulSoup(page_content, 'lxml')

  # Find the image tag
  image_tag = soup.find('img', src=image_url)

  # Get the alt text
  alt_text = image_tag.get('alt')

  if not alt_text:
    write_to_temp_file(temp_file, 'No alt text')
  else:
    write_to_temp_file(temp_file, alt_text)

def generate_report(temp_files):
  """Generates a report of image URLs without alt text from the temporary files."""

  report = []

  for temp_file in temp_files:
    # Read the report from the temporary file
    report.append(read_from_temp_file(temp_file))

  return report

def main():
  # Get the sitemap URLs
  sitemap_urls = [
    'https://www.i-bidder.com/past/sitemap-images48.xml.gz',
    'https://www.i-bidder.com/past/sitemap-images49.xml.gz',
    'https://www.i-bidder.com/past/sitemap-images50.xml.gz'
  ]

  # Create a temporary directory to store the temporary files
  temp_dir = tempfile.mkdtemp()

  # Create a temporary file for each sitemap URL
  temp_files = []
  for sitemap_url in sitemap_urls:
    temp_file = create_temp_file()
    temp_files.append(temp_file)

  # Parse the sitemaps and scan the pages for alt text
  for sitemap_url, temp_file in zip(sitemap_urls, temp_files):
    parse_sitemap(sitemap_url, temp_file)

  # Generate a report of image URLs without alt text
  report = generate_report(temp_files)

  # Save the report to a CSV file
  output_file = 'report.csv'
  with open(output_file, 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['Issue'])
    writer.writerows(report)

if __name__ == '__main__':
  main()
