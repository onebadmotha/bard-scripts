import requests
from bs4 import BeautifulSoup

# Function to extract image URLs from a given URL and print wget statements
def extract_and_print_image_urls(url):
    try:
        # Send an HTTP GET request to the URL
        response = requests.get(url)
        response.raise_for_status()

        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all <img> tags in the HTML
        img_tags = soup.find_all('img')

        for img in img_tags:
            if 'src' in img.attrs:
                img_url = img['src']
                # Print wget statement
                print(f'wget "{img_url}"')

    except Exception as e:
        print(f"An error occurred: {e}")

# Prompt the user for a URL
url = input("Enter a URL: ")

# Extract image URLs and print wget statements
print("Use the following wget statements to download the images:")
extract_and_print_image_urls(url)