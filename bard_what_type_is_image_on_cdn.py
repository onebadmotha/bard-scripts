import requests
from bs4 import BeautifulSoup
import imghdr
import tempfile

def check_image_type_on_cdn(image_url):
  """Checks the image type on the CDN.

  Args:
    image_url: The URL of the image.

  Returns:
    The image type, or None if the image type could not be determined.
  """

  # Download the image from the CDN to a temporary directory.
  with tempfile.NamedTemporaryFile() as temp_file:
    response = requests.get(image_url)
    with open(temp_file.name, "wb") as f:
      f.write(response.content)

    # Determine the image type.
    image_type = imghdr.what(temp_file.name)

    return image_type

def main():
  """Prompts the user for a URL or image URL and prints the image type on the CDN."""

  url = input("Enter a URL or image URL: ")

  # Check if the URL is a valid image URL.
  if not imghdr.what(url):
    print("Invalid image URL.")
    return

  # Get the image type on the CDN.
  image_type = check_image_type_on_cdn(url)

  if image_type is not None:
    print(f"The image type on the CDN is: {image_type}")
  else:
    print("Could not determine the image type on the CDN.")

if __name__ == "__main__":
  main()
