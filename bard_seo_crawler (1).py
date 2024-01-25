import scrapy

class SEOCheckSpider(scrapy.Spider):
    name = 'seocheck'
    start_urls = ['https://example.com']

    def __init__(self, *args, **kwargs):
        super(SEOCheckSpider, self).__init__(*args, **kwargs)
        self.report = []

    def parse(self, response):
        url = response.url

        # SEO checks
        title = response.css('title::text').get()
        description = response.css('meta[name="description"]::attr(content)').get()
        h1 = response.css('h1::text').get()
        h2 = response.css('h2::text').extract()
        h3 = response.css('h3::text').extract()
        image_alt_text = [alt.strip() for alt in response.css('img::attr(alt)').extract()]
        word_count = len(response.body.split())
        
        # Check for schema markup
        schema_found = 'schema.org' in response.text

        # Example checks
        if "example" in url:
            self.report.append(f'{url} Issue: URL contains "example"')
        if not title:
            self.report.append(f'{url} Issue: Missing <title> tag')
        if not description:
            self.report.append(f'{url} Issue: Missing meta description')
        if not h1:
            self.report.append(f'{url} Issue: Missing <h1> tag')
        
        # Check for pagination in the head and body
        pagination_head = 'rel="next"' in response.text
        pagination_body = 'class="next"' in response.text
        
        # Check for scripts triggering on the page
        scripts_triggered = response.css('script::attr(src)').extract()

        # Check for console errors (you can expand this based on your needs)
        console_errors = response.css('script:contains("console.error")').extract()

        # Recommended SEO and Technical SEO actions (customize these based on your criteria)
        recommended_seo_actions = []
        recommended_technical_seo_actions = []
        
        # Check if the page is in the sitemaps (customize the sitemap URL)
        sitemap_url = 'https://example.com/sitemap.xml'
        in_sitemap = sitemap_url in response.text

        # Check if the page is blocked in robots.txt (customize the robots.txt URL)
        robots_txt_url = 'https://example.com/robots.txt'
        robots_disallowed = 'Disallow:' in requests.get(robots_txt_url).text

        # Collect internal and external links on the page
        internal_links = [link for link in response.css('a::attr(href)').extract() if 'example.com' in link]
        external_links = [link for link in response.css('a::attr(href)').extract() if 'example.com' not in link]

        # Append findings to the report
        self.report.append(f'Page: {url}')
        self.report.append(f'Internal Links: {", ".join(internal_links)}')
        self.report.append(f'External Links: {", ".join(external_links)}')
        self.report.append(f'H2 Headings: {", ".join(h2)}')
        self.report.append(f'H3 Headings: {", ".join(h3)}')
        self.report.append(f'Schema Markup Found: {schema_found}')
        self.report.append(f'Image Alt Text: {", ".join(image_alt_text)}')
        self.report.append(f'Word Count: {word_count}')
        self.report.append(f'Pagination in Head: {pagination_head}')
        self.report.append(f'Pagination in Body: {pagination_body}')
        self.report.append(f'Scripts Triggering: {", ".join(scripts_triggered)}')
        self.report.append(f'Console Errors: {", ".join(console_errors)}')
        self.report.append(f'Recommended SEO Actions: {", ".join(recommended_seo_actions)}')
        self.report.append(f'Recommended Technical SEO Actions: {", ".join(recommended_technical_seo_actions)}')
        self.report.append(f'In Sitemap: {in_sitemap}')
        self.report.append(f'Blocked in Robots.txt: {robots_disallowed}')

        # Follow more links
        for next_page in response.css('a::attr(href)').extract():
            yield response.follow(next_page, callback=self.parse)

    def closed(self, reason):
        with open('seo_report.txt', 'w') as f:
            for entry in self.report:
                f.write(entry + '\n')
