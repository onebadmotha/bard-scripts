import gzip
import requests
import re

def get_image_sitemaps(sitemap_index_url):
  """
  Gets a list of image sitemap URLs from the given image sitemap index URL.

  Args:
    sitemap_index_url: The URL of the image sitemap index.

  Returns:
    A list of image sitemap URLs.
  """

  response = requests.get(sitemap_index_url)
  content = gzip.decompress(response.content)
  soup = BeautifulSoup(content, 'xml')

  sitemap_urls = []
  for sitemap_tag in soup.find_all('sitemap'):
    sitemap_urls.append(sitemap_tag['loc'])

  return sitemap_urls

def check_image_is_on_cdn(image_url):
  """
  Checks if the given image URL is on the CDN and can be downloaded.

  Args:
    image_url: The URL of the image.

  Returns:
    True if the image is on the CDN and can be downloaded, False otherwise.
  """

  try:
    response = requests.get(image_url)
    return response.status_code == 200
  except Exception:
    return False

def print_webp_image_urls(image_sitemaps):
  """
  Prints out the URLs of images that are WebP.

  Args:
    image_sitemaps: A list of image sitemap URLs.
  """

  for image_sitemap in image_sitemaps:
    response = requests.get(image_sitemap)
    content = gzip.decompress(response.content)
    soup = BeautifulSoup(content, 'xml')

    for image_tag in soup.find_all('image:image'):
      image_url = image_tag['image:loc']
      if image_url.endswith('.webp'):
        print(image_url)

if __name__ == '__main__':
  # Get the image sitemap URLs from the image sitemap index.
  image_sitemap_urls = get_image_sitemaps('https://www.the-saleroom.com/images_active_sitemapindex')

  # Check if the images are on the CDN and can be downloaded.
  for image_sitemap_url in image_sitemap_urls:
    image_urls = []
    response = requests.get(image_sitemap_url)
    content = gzip.decompress(response.content)
    soup = BeautifulSoup(content, 'xml')

    for image_tag in soup.find_all('image:image'):
      image_url = image_tag['image:loc']
      image_urls.append(image_url)

    for image_url in image_urls:
      if not check_image_is_on_cdn(image_url):
        print('Image URL: {}\nIssue: Failed to download from CDN'.format(image_url))

  # Print out the URLs of images that are WebP.
  print_webp_image_urls(image_sitemaps)
