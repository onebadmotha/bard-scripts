import requests

def ping_sitemap(sitemap_url):
  """Pings the specified sitemap.

  Args:
    sitemap_url: The URL of the sitemap.
  """

  # Create the request.
  headers = {"Content-Type": "application/xml"}
  response = requests.post(sitemap_url, headers=headers, data="")

  # Check the response status code.
  if response.status_code != 200:
    # Print an error message.
    print(f"Error: {response.status_code}")
    return

  # Print a success message.
  print(f"Successfully pinged the sitemap at {sitemap_url}.")

def main():
  # Get the list of sitemaps to ping.
  sitemap_urls = [
    "https://www.the-saleroom.com/sitemap.xml",
    "https://www.i-bidder.com/sitemap.xml",
    "https://www.bidspotter.com/sitemap.xml",
    "https://www.bidspotter.co.uk/sitemap.xml",
    "https://www.lot-tissimo.com/sitemap.xml",
    "https://www.proxibid.com/sitemap.xml",
    "https://www.liveauctioneers.com/sitemap.xml",
    "https://www.estatesales.net/sitemap.xml",
  ]

  # Ping each sitemap.
  for sitemap_url in sitemap_urls:
    ping_sitemap(sitemap_url)

if __name__ == "__main__":
  main()