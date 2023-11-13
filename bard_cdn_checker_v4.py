import numpy as np

import requests
import io
import re

import PIL.Image
import cv2

def add_scheme_to_url(url):
  """Adds a scheme to the given URL if it does not already have one.

  Args:
    url: The URL to add a scheme to.

  Returns:
    The URL with a scheme added, or the original URL if it already had a scheme.
  """

  if not re.match(r'^\w+://', url):
    url = 'https://' + url
  return url

def check_azure_cdn_response(url):
  """Checks if the Azure CDN is responding to the given URL.

  Args:
    url: The URL to check.

  Returns:
    True if the Azure CDN is responding, False otherwise.
  """

  response = requests.get(url)

  if response.status_code == 200 and response.headers.get("X-Azure-Cache") is not None:
    return True
  else:
    return False

def check_image_corruption(image_url):

  response = requests.get(image_url)

  # Convert the response content to a byte array.
  byte_array = response.content

  # Remove any null bytes from the byte array.
  byte_array = byte_array.replace(b"\0", b"")

  # Create a BytesIO object from the byte array.
  byte_io = io.BytesIO(byte_array)

  # Convert the BytesIO object to a NumPy array.
  image_array = np.frombuffer(byte_io.getvalue(), dtype=np.uint8)

  # Convert the NumPy array to a string.
  image_string = image_array.tobytes()

  # Print the value of the image_string variable.
  print(image_string)

  # Check for image corruption.
  image = cv2.imread(image_string, cv2.IMREAD_UNCHANGED)

  if image is None:
    return True
  elif image.size == (0, 0):
    return True
  else:
    return False

def main():
  url = input("Enter a webpage URL: ")

  # Add a scheme to the URL if it does not already have one.
  url = add_scheme_to_url(url)

  # Check if the Azure CDN is responding to the given URL.
  cdn_status = "Azure CDN: Accessible" if check_azure_cdn_response(url) else "Azure CDN: Not accessible"

  # Get all of the image URLs on the page.
  image_urls = re.findall(r'src="([^"]+)"', requests.get(url).content.decode('utf-8'))

  # Check each image URL against Google's Image standards and the Azure CDN.
  violations = []
  webp_images = []
  for image_url in image_urls:
    if image_url.startswith("https://portal-images.azureedge.net"):
      # Check for image corruption.
      if check_image_corruption(image_url):
        violations.append((image_url.split("/")[-1], ["Image corruption detected"]))
      else:
        # Check for other violations.
        # ...
        pass

      if image_url.endswith(".webp"):
        webp_images.append(image_url.split("/")[-1])

  # Output the CDN status, image violations, and webp images.
  print(f"CDN status: {cdn_status}")
  print(f"CDN download check:")
  for image_name, errors in violations:
    print(f"  Image name ({image_name}): {errors}")
  print(f"Webp images:")
  for webp_image in webp_images:
    print(f"  {webp_image}")

if __name__ == "__main__":
  main()
