import requests

# Set the site URL.
site_url = "https://example.com/"

# Create the request.
headers = {"Authorization": "Bearer YOUR_API_KEY"}
response = requests.get(f"https://searchconsole.googleapis.com/v1/webmasters/sites/{site_url}/crawlStats", headers=headers)

# Check the response status code.
if response.status_code == 200:
  # Get the crawl stats.
  crawl_stats = response.json()

  # Get the number of image sitemap pages crawled.
  num_image_sitemap_pages_crawled = crawl_stats["crawlStats"]["crawlTimeSpentPerResourceType"]["IMAGE_SITEMAP"]["pages"]["crawled"]

  # Print the number of image sitemap pages crawled.
  print(f"The Google image bot visited the image sitemaps {num_image_sitemap_pages_crawled} times.")
else:
  # Print an error message.
  print(f"Error: {response.status_code}")
