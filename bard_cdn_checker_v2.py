import requests
import re

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
    A tuple containing four values:
      * True if the image URL meets the standards, False otherwise.
      * A list of reasons why the image URL does not meet the standards, or an empty list if the image URL meets the standards.
      * The image type (jpg, png, or webp).
      * The Google regulation that is being broken.
  """

  response = requests.get(url)

  content_type = response.headers["Content-Type"]

  if content_type == "image/jpeg":
    image_type = "jpg"
  elif content_type == "image/png":
    image_type = "png"
  elif content_type == "image/webp":
    image_type = "webp"
  else:
    image_type = "unknown"

  # TODO: Add more checks for other Google image ranking requirements.

  google_regulation_1 = "The image is in a supported format (jpg, png, or webp)."
  google_regulation_2 = "The image is relevant to the content of the webpage."

  if image_type not in ["jpg", "png", "webp"]:
    return (False, [google_regulation_1], image_type, google_regulation_1)
  elif response.status_code != 200:
    return (False, ["The image cannot be crawled by Googlebot."], image_type, google_regulation_1)
  else:
    return (True, [], image_type, "")

def main():
  url = input("Enter a webpage URL: ")

  # Check if the CDN is responding.
  if check_cdn_response(url):
    print("The CDN is responding.")
  else:
    print("The CDN is not responding.")

  # Check if Google Image bot has the ability to crawl the image file.
  if check_google_bot_access(url):
    print("Google Image bot has the ability to crawl the image file.")
  else:
    print("Google Image bot does not have the ability to crawl the image file.")

  # Check if the image file is within the standards that Google has outlined for image ranking in Google Images.
  image_standards_met, reasons, image_type, google_regulation = check_image_standards(url)

  if image_standards_met:
    print("All images on the page meet the standards for image ranking in Google Images.")
  else:
    print("The following images on the page do not meet the standards for image ranking in Google Images:")
    output = ""
    for url, reason, image_type, google_regulation in zip(reasons, image_type, google_regulation):
      output += f"* {url} ({image_type}) : {reason} ({google_regulation})\n"
    print(output)



CDN: Accesible by Google Images
CDN: Is delivering files
Image: Azure sdjskdsdjdsksj.jpg;  failed image to small (30x30), failed no alt text, etc....