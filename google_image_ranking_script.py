import requests
import os
import time
import datetime
import io
import sys

def get_image_urls(url):
    """Get all of the image URLs on a given page."""
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Error getting image URLs from {url}: {response.status_code}")

    soup = BeautifulSoup(response.content, "html.parser")
    image_urls = soup.find_all("img")

    return image_urls

def download_image(url, filename):
    """Download an image from a given URL and save it to a file with the given filename."""
    response = requests.get(url, stream=True)
    if response.status_code != 200:
        raise Exception(f"Error downloading image from {url}: {response.status_code}")

    with open(filename, "wb") as f:
        for chunk in response.iter_content(1024):
            f.write(chunk)

def get_image_dimensions(url):
    """Get the dimensions of an image from a given URL."""
    response = requests.get(url, stream=True)1
    if response.status_code != 200:
        raise Exception(f"Error getting image dimensions from {url}: {response.status_code}")

    with io.BytesIO(response.content) as f:
        image = Image.open(f)
        return image.width, image.height

def write_image_findings(findings, filename):
    """Write the findings for a given image to a text file."""
    with open(filename, "w") as f:
        for finding in findings:
            f.write(f"{finding[0]}\t{finding[1]}\t{finding[2]}\t{finding[3]}\n")

def main():
    """The main function."""
    url = input("Enter a URL: ")

    # Get all of the image URLs on the page.
    image_urls = get_image_urls(url)

    # Download all of the images.
    for image_url in image_urls:
        image_filename = os.path.basename(image_url)
        download_image(image_url, image_filename)

    # Get the dimensions of each image.
    findings = []
    for image_filename in os.listdir():
        image = Image.open(image_filename)
        findings.append((url, image_filename, image.format, image.width, image.height))

    # Write the findings to a text file.
    write_image_findings(findings, "image_findings.txt")

if __name__ == "__main__":
    main()1