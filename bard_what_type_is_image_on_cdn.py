import requests
from tempfile import NamedTemporaryFile

def download_image(url):
  """Downloads an image from a URL to a temporary file.

  Args:
    url: The URL of the image.

  Returns:
    The path to the temporary file containing the image.
  """

  response = requests.get(url)
  temp_file = NamedTemporaryFile()
  temp_file.write(response.content)
  temp_file.flush()
  return temp_file.name

def check_image_type_on_cdn(image_url):
  """Checks the image type on the CDN.

  Args:
    image_url: The URL of the image.

  Returns:
    The image type, or None if the image type could not be determined.
  """

  # Download the image from the CDN to a temporary file.
  temp_file_path = download_image(image_url)

  # Determine the image type.
  image_type = imghdr.what(temp_file_path)

  # Delete the temporary file.
  os.remove(temp_file_path)

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