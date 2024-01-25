import requests

def is_cdn_changing_images_to_webp(url):
  """Checks if the CDN is changing images to WebP for the client.

  Args:
    url: The URL of the webpage to check.

  Returns:
    True if the CDN is changing images to WebP for the client, False otherwise.
  """

  # Get the original image URL from the HTML of the webpage.
  response = requests.get(url)
  html = response.content

  # Extract the image URL from the HTML.
  image_url = re.findall(r'src="([^"]+)"', html)[0]

  # Request the image from the CDN using the original image URL.
  response = requests.get(image_url)

  # Check the Content-Type header of the response.
  content_type = response.headers["Content-Type"]

  if content_type == "image/webp":
    return True
  else:
    return False

# Example usage:

url = "https://example.com/index.html"

if is_cdn_changing_images_to_webp(url):
  print("The CDN is changing images to WebP for the client.")
else: