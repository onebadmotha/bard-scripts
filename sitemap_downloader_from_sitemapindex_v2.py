import os
import requests
import xml.etree.ElementTree as ET
import gzip
from io import BytesIO
import shutil
from datetime import datetime

# Function to create nested folders based on the specified structure
def create_nested_folders(base_folder, *folders):
    folder_path = os.path.join(base_folder, *folders)
    os.makedirs(folder_path, exist_ok=True)
    return folder_path

# Function to download and process sitemaps from the given sitemap index URL
def download_and_process_sitemaps(sitemap_index_url):
    try:
        # Step 1: Create the directory structure
        today = datetime.today()
        website_domain = sitemap_index_url.split('//')[1].split('/')[0]
        sitemap_index_name = sitemap_index_url.split('/')[-1]
        folder_structure = [
            website_domain,
            str(today.year),
            str(today.month).zfill(2),
            str(today.day).zfill(2),
            sitemap_index_name,
        ]
        folder_path = create_nested_folders(os.getcwd(), *folder_structure)
        sources_folder = os.path.join(folder_path, 'source')

        # Step 2: Download and process sitemaps
        response = requests.get(sitemap_index_url)
        if response.status_code == 200:
            root = ET.fromstring(response.content)

            for sitemap in root.findall('.//sitemap/loc'):
                sitemap_url = sitemap.text
                sitemap_name = os.path.basename(sitemap_url)
                sitemap_filename = os.path.join(folder_path, sitemap_name)

                # Download the sitemap
                sitemap_response = requests.get(sitemap_url)
                if sitemap_response.status_code == 200:
                    with open(sitemap_filename, 'wb') as sitemap_file:
                        sitemap_file.write(sitemap_response.content)
                    print(f"Downloaded: {sitemap_name}")

                    # Check if it's gzipped
                    if sitemap_response.headers.get('content-type') == 'application/gzip':
                        with open(sitemap_filename, 'wb') as sitemap_file:
                            sitemap_file.write(sitemap_response.content)

                        # Extract the gzipped sitemap
                        with gzip.open(sitemap_filename, 'rb') as gzipped_sitemap:
                            extracted_content = gzipped_sitemap.read()
                        extracted_filename = os.path.join(folder_path, sitemap_name.replace('.gz', ''))
                        with open(extracted_filename, 'wb') as extracted_file:
                            extracted_file.write(extracted_content)

                        print(f"Extracted: {extracted_filename}")

                        # Verify the presence of the extracted file
                        if os.path.isfile(extracted_filename):
                            print(f"Verified: {extracted_filename} is present")
                        else:
                            print(f"Warning: {extracted_filename} is missing")

                        # Create the 'source' folder if it doesn't exist
                        if not os.path.exists(sources_folder):
                            os.makedirs(sources_folder)

                        # Move the original .gz file to the 'source' folder
                        source_filename = os.path.join(sources_folder, sitemap_name)
                        shutil.move(sitemap_filename, source_filename)
                        print(f"Moved to source: {source_filename}")

        else:
            print(f"Failed to fetch sitemap index: {sitemap_index_url}")

        print("Done: All steps completed successfully")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    sitemap_index_url = input("Please enter the sitemap index URL: ")
    download_and_process_sitemaps(sitemap_index_url)