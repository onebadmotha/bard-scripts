import googleapiclient.discovery

def submit_sitemap(site_url, sitemap_urls):
    # Replace with your service account credentials
    service_account_credentials = google.auth.credentials.Credentials.from_service_account_file('service_account.json')

    # Build the Google Search Console service
    service = googleapiclient.discovery.build('searchconsole', 'v1', credentials=service_account_credentials)

    for sitemap_url in sitemap_urls:
        request = service.sitemaps().submit(siteUrl=site_url, body={'sitemap': sitemap_url})
        response = request.execute()

        if response['status']['code'] == 200:
            print('Sitemap', sitemap_url, 'submitted successfully.')
        else:
            print('Error submitting sitemap', sitemap_url, ':', response['status'])

# Replace the placeholder URLs with your own website's URL and sitemap URLs
#The site_url variable in the script should be changed to match the domain of the sitemap you are submitting. For example, if you are submitting the sitemap for https://www.i-bidder.com/, you would change the site_url variable to the following:
#example: site_url = "https://www.i-bidder.com/"

  site_url = "https://www.example.com/"  # Replace with your website's URL
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
submit_sitemap(site_url="https://www.example.com/", sitemap_urls=sitemap_urls)
