Python Scripts for Comparing Sitemaps

Python
# Download a sitemap.
def download_sitemap(sitemap_url):
  response = requests.get(sitemap_url)
  with open("sitemap.xml", "wb") as f:
    f.write(response.content)

# Parse a sitemap.
def parse_sitemap(sitemap_file):
  with open(sitemap_file, "r") as f:
    soup = BeautifulSoup(f.read(), "html.parser")

  return [url.text for url in soup.find_all("loc")]

# Compare two sitemaps.
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

# Example usage:

# Download the active sitemaps and lot sitemaps.
download_sitemap("https://www.i-bidder.com/images_active_sitemapindex")
download_sitemap("https://www.i-bidder.com/lots_sitemapindex")

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
You can copy and paste this script into a new Google Docs document and then run it by clicking on the Run button in the toolbar. The script will then download the active sitemaps and lot sitemaps for i-bidder, parse them, compare them, and print the results to the Google Docs document.

You can then edit the script to compare the sitemaps for different websites. To do this, simply change the values of the active_sitemap_url and lot_sitemap_url variables.