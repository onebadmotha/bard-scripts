import requests
from bs4 import BeautifulSoup

def download_sitemap(sitemap_url):
  response = requests.get(sitemap_url)
  with open("sitemap.xml", "wb") as f:
    f.write(response.content)

def parse_sitemap(sitemap_file):
  with open(sitemap_file, "r") as f:
    soup = BeautifulSoup(f.read(), "html.parser")

  return [url.text for url in soup.find_all("loc")]

def compare_sitemaps(active_sitemap_urls, lot_sitemap_urls):
  new_lots = []
  missing_images = []

  for lot_sitemap_url in lot_sitemap_urls:
    lot_sitemap = parse_sitemap(lot_sitemap_url)

    for lot in lot_sitemap:
      if lot not in active_sitemap_urls:
        new_lots.append(lot)

  for active_sitemap_url in active_sitemap_urls:
    if not any(lot_sitemap.endswith(active_sitemap_url) for lot_sitemap in lot_sitemap_urls):
      missing_images.append(active_sitemap_url)

  return new_lots, missing_images

if __name__ == "__main__":
  active_sitemap_url = "https://www.i-bidder.com/images_active_sitemapindex"
  lot_sitemap_url = "https://www.i-bidder.com/lots_sitemapindex"

  # Download the sitemaps.
  download_sitemap(active_sitemap_url)
  download_sitemap(lot_sitemap_url)

  # Parse the sitemaps.
  active_sitemap_urls = parse_sitemap("sitemap.xml")
  lot_sitemap_urls = parse_sitemap("sitemap.xml")

  # Compare the sitemaps.
  new_lots, missing_images = compare_sitemaps(active_sitemap_urls, lot_sitemap_urls)

  # Print the results.
  print("New lots:")
  for new_lot in new_lots:
    print(new_lot)

  print("Missing images:")
  for missing_image in missing_images:
    print(missing_image)
Use code with caution. Learn more
To use the script, simply save it as a Python file (e.g. compare_sitemaps.py) and run it in a terminal. The script will then download the active sitemaps and lot sitemaps, parse them, compare them, and print the results to the console.

You can then add the new lots to the active image sitemap and add missing images to the active image sitemap.