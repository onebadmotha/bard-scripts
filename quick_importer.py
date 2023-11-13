from PIL import Image

def get_image_type(image_url):
  """Gets the image type of an image URL.

  Args:
    image_url: The URL of the image.

  Returns:
    The image type of the image, or None if the image type cannot be determined.
  """

  try:
    image = Image.open(image_url)
    image_type = image.format
  except OSError:
    image_type = None

  return image_type

# Example usage:

image_url = "https://portal-images.azureedge.net/auctions-2022/artmar10023/images/0cf8de64-3d03-47e1-9ce1-ae9800be9d6e.jpg"

image_type = get_image_type(image_url)

if image_type is None:
  print("Could not determine image type.")
else:
  print(f"Image type: {image_type}")