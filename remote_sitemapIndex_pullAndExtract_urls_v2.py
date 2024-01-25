import requests
import gzip
import xml.etree.ElementTree as ET
import os


def extract_and_save_urls_from_sitemap(sitemap_url, output_directory):
    # Fetch the sitemap content
    response = requests.get(sitemap_url)

    if response.status_code == 200:
        # Extract the filename from the URL
        sitemap_filename = os.path.basename(sitemap_url)

        # Remove any potential query parameters in the filename
        sitemap_filename = sitemap_filename.split("?")[0]

        # Remove "https://www." and ".xml.gz" from the filename
        sitemap_filename = sitemap_filename.replace("https://www.", "").replace(".xml.gz", ".txt")

        # Decompress the gzipped content
        sitemap_content = gzip.decompress(response.content).decode('utf-8')

        # Parse the XML content
        root = ET.fromstring(sitemap_content)

        # Open a text file for writing
        output_filepath = os.path.join(output_directory, sitemap_filename)
        with open(output_filepath, "w") as output_file:
            # Iterate through URLs and write those containing "https://www." to the file
            for url in root.iter("{http://www.sitemaps.org/schemas/sitemap/0.9}loc"):
                url_text = url.text
                if "https://www." in url_text:
                    output_file.write(url_text + "\n")

        print(f"URLs extracted and saved to {output_filepath}")
    else:
        print(f"Failed to fetch sitemap: {response.status_code}")

def extract_sitemaps_from_index(sitemap_index_url, output_directory):
    # Fetch the sitemap index content
    response = requests.get(sitemap_index_url)

    if response.status_code == 200:
        sitemap_index_content = response.text
        root = ET.fromstring(sitemap_index_content)

        for sitemap in root.iter("{http://www.sitemaps.org/schemas/sitemap/0.9}sitemap"):
            sitemap_url = sitemap.find("{http://www.sitemaps.org/schemas/sitemap/0.9}loc").text
            extract_and_save_urls_from_sitemap(sitemap_url, output_directory)

    else:
        print(f"Failed to fetch sitemap index: {response.status_code}")

if __name__ == "__main__":
    sitemap_index_url = input("Enter the sitemap index URL: ")
    output_directory = "output"  # Change this to your desired output directory
    os.makedirs(output_directory, exist_ok=True)
    extract_sitemaps_from_index(sitemap_index_url, output_directory)