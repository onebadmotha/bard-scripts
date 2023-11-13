import requests
import re

def is_cdn_changing_images_to_webp(url):
  """Checks if the CDN is changing images to WebP for the client.

  Args:
    url: The URL of the webpage to check.

  Returns:
    True if the CDN is changing images to WebP for the client, False otherwise.
  """

  # Get the HTML of the webpage.
  response = requests.get(url)
  html = response.content

  # Decode the HTML bytes.
  html = html.decode('utf-8')

  # Extract the image URLs from the HTML.
  image_urls = re.findall(r'src="([^"]+)"', html)

  if image_urls:
    image_url = image_urls[0]
  else:
    # There are no images on the webpage, or the images on the webpage are not being served from a CDN.
    return False

  # Request the image from the CDN using the first image URL.
  response = requests.get(image_url)

  # Check the Content-Type header of the response.
  content_type = response.headers["Content-Type"]

  if content_type == "image/webp":
    return True
  else:
    return False

# Example usage:

url = input("Enter the URL of the webpage to check: ")

if is_cdn_changing_images_to_webp(url):
  print("The CDN is changing images to WebP for the client.")
else:
  print("The CDN is not changing images to WebP for the client.")
