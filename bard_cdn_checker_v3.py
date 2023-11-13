import requests
import re

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

def check_cdn_response(url):
  """Checks if the CDN is responding to the given URL.

  Args:
    url: The URL to check.

  Returns:
    True if the CDN is responding, False otherwise.
  """

  response = requests.get(url)

  if response.status_code == 200:
    return True
  else:
    return False

def check_google_bot_access(url):
  """Checks if Google Image bot has the ability to crawl the given image URL.

  Args:
    url: The URL of the image to check.

  Returns:
    True if Google Image bot has the ability to crawl the image URL, False otherwise.
  """

  headers = {
    "User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"
  }

  response = requests.get(url, headers=headers)

  if response.status_code == 200:
    return True
  else:
    return False

def check_image_standards(url):
  """Checks if the given image URL meets the standards that Google has outlined for image ranking in Google Images.

  Args:
    url: The URL of the image to check.

  Returns:
    A list of errors, or an empty list if the image URL meets all the standards.
  """

  response = requests.get(url)

  content_type = response.headers["Content-Type"]

  if content_type not in ["image/jpeg", "image/png", "image/webp"]:
    return ["failed image file type not supported"]

  image_width, image_height = response.content.info().get("width"), response.content.info().get("height")

  errors = []

  if image_width < 30 or image_height < 30:
    errors.append("failed image too small (30x30)")
  elif image_width > 1000 or image_height > 1000:
    errors.append("failed image too large (1000x1000)")

  alt_text = response.headers.get("alt")

  if not alt_text or alt_text == "":
    errors.append("failed no alt text")

  return errors

def main():
  url = input("Enter a webpage URL: ")
  url = add_scheme_to_url(url)

  # Check if the CDN is responding.
  if check_cdn_response(url):
    print("CDN: Accessible by Google Images")
  else:
    print("CDN: Not accessible by Google Images")

  # Check if the CDN is delivering files.
  if check_google_bot_access(url):
    print("CDN: Is delivering files")
  else:
    print("CDN: Is not delivering files")

  # Check if the image files meet the standards that Google has outlined for image ranking in Google Images.
  errors = []

  response = requests.get(url)

  for image_url in re.findall(r'src="([^"]+)"', response.content.decode('utf-8')):
    image_errors = check_image_standards(image_url)

    if image_errors:
      errors.append(f"Image: {image_url};")
      for error in image_errors:
        errors.append(f"    {error}")

  if errors:
    for error in errors:
      print(error)

if __name__ == "__main__":
  main()
