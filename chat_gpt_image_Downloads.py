import requests
from bs4 import BeautifulSoup

# Function to extract image URLs from a given URL
def extract_image_urls(url):
    try:
        # Send an HTTP GET request to the URL
        response = requests.get(url)
        response.raise_for_status()

        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all <img> tags in the HTML
        img_tags = soup.find_all('img')

        # Extract the 'src' attribute from each <img> tag
        image_urls = [img['src'] for img in img_tags if 'src' in img.attrs]

        return image_urls

    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# Prompt the user for a URL
url = input("Enter a URL: ")

# Extract image URLs and print them
image_urls = extract_image_urls(url)
if image_urls:
    for img_url in image_urls:
        print(img_url)
else:
    print("No image URLs found on the page.")