#Sure. Here is the final Python script updating all of the search engines with your sitemap changes:

Python
import requests

def ping_sitemap(sitemap_url, search_engine):
  """Pings the specified sitemap on the specified search engine.

  Args:
    sitemap_url: The URL of the sitemap.
    search_engine: The name of the search engine.
  """

  # Create the request.
  headers = {"Content-Type": "application/xml"}
  response = requests.post(f"https://{search_engine}.com/ping?sitemap={sitemap_url}", headers=headers, data="")

  # Check the response status code.
  if response.status_code != 200:
    # Print an error message.
    print(f"Error: {response.status_code}")
    return

  # Print a success message.
  print(f"Successfully pinged the {search_engine} sitemap at {sitemap_url}.")

def main():
  # Get the list of sitemaps to ping.
  sitemap_urls = [
    "https://www.i-bidder.com/sitemapindex",
    "https://www.i-bidder.com/lots_sitemapindex",
    "https://www.i-bidder.com/auctions_sitemapindex",
    "https://www.i-bidder.com/categories_sitemapindex",
    "https://www.i-bidder.com/filteredpages_sitemapindex",
    "https://www.i-bidder.com/auctioneers_sitemapindex",
    "https://www.i-bidder.com/images_active_sitemapindex",
    "https://www.i-bidder.com/images_past_sitemapindex",
    "https://www.i-bidder.com/secondary_categories_sitemapindex",
    "https://www.bidspotter.com/sitemapindex",
    "https://www.bidspotter.com/lots_sitemapindex",
    "https://www.bidspotter.com/auctions_sitemapindex",
    "https://www.bidspotter.com/categories_sitemapindex",
    "https://www.bidspotter.com/filteredpages_sitemapindex",
    "https://www.bidspotter.com/auctioneers_sitemapindex",
    "https://www.bidspotter.com/images_active_sitemapindex",
    "https://www.bidspotter.com/images_past_sitemapindex",
    "https://www.bidspotter.com/secondary_categories_sitemapindex",
    "https://www.bidspotter.co.uk/sitemapindex",
    "https://www.bidspotter.co.uk/lots_sitemapindex",
    "https://www.bidspotter.co.uk/auctions_sitemapindex",
    "https://www.bidspotter.co.uk/categories_sitemapindex",
    "https://www.bidspotter.co.uk/filteredpages_sitemapindex",
    "https://www.bidspotter.co.uk/auctioneers_sitemapindex",
    "https://www.bidspotter.co.uk/images_active_sitemapindex",
    "https://www.bidspotter.co.uk/images_past_sitemapindex",
    "https://www.bidspotter.co.uk/secondary_categories_sitemapindex",
    "https://www.the-saleroom.com/sitemapindex",
    "https://www.the-saleroom.com/lots_sitemapindex",
    "https://www.the-saleroom.com/auctions_sitemapindex",
    "https://www.the-saleroom.com/categories_sitemapindex",
    "https://www.the-saleroom.com/filteredpages_sitemapindex",
    "https://www.the-saleroom.com/auctioneers_sitemapindex",
    "https://www.the-saleroom.com/images_active_sitemapindex",
    "https://www.the-saleroom.com/images_past_sitemapindex",
    "https://www.the-saleroom.com/secondary_categories_sitemapindex",
    "https://www.lot-tissimo.com/sitemapindex",
    "https://www.lot-tissimo.com/lots_sitemapindex",
    "https://www.lot-tissimo.com/auctions_sitemapindex",
    "https://www.lot-tissimo.com/categories_sitemapindex",
    "https://www.lot-tissimo.com/filteredpages_sitemapindex",
    "https://www.lot-tissimo.com/auctioneers_sitemapindex",
    "https://www.lot-tissimo.com/images_active_sitemapindex",
    "https://www.lot-tissimo.com/images_past_sitemapindex",
    "https://www.lot-tissimo.com/secondary_categories_sitemapindex",
    "https://www.proxibid.com/sitemap.xml",
    "https://www.proxibid.com/sitemap-lots.xml",
    "https://www.proxibid.com/sitemap-auctions.xml",
    "https://www.liveauctioneers.com/sitemap.xml",
    "https://www.estatesales.net/site-maps",
    "https://www.antiquestradegazette.com/GoogleSiteMap",
    "https://www.auctionmobility.com/sitemap_index.xml",
    "https://discover.proxibid.com/sitemap_index.xml",
  ]

  # Ping each sitemap on all of the search engines.
  search_engines = ["google", "bing", "yandex"]
  for sitemap_url in sitemap_urls:
    for search_engine in search_engines:
      ping_sitemap(sitemap_url, search_engine)

if __name__ == "__main__":
  main()


#To use the script, simply run it in a terminal. The script will then ping all of the sitemaps in the list on all of the search engines. You can schedule the script to run once per day using a cron job, as described above. This will ensure that all of the major search engines are notified of any changes to your site's URLs once per day.