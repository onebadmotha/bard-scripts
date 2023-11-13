import playwright
from playwright.async_api import async_playwright

async def main():
    context = await async_playwright().chromium.launch()

    page = await context.new_page()
    await page.goto('https://www.example.com')

    # Check if the H1 is present and visible.
    h1 = await page.query_selector('h1')
    if h1 is None:
        print('The H1 is not present.')
    elif not await h1.is_visible():
        print('The H1 is not visible.')
    else:
        print('The H1 is present and visible.')

    # Check if the meta title is present and within 50-60 characters.
    meta_title = await page.query_selector('meta[name="title"]')
    if meta_title is None:
        print('The meta title is not present.')
    elif len(meta_title.content) < 50 or len(meta_title.content) > 60:
        print('The meta title is not between 50 and 60 characters.')
    else:
        print('The meta title is present and within 50-60 characters.')

    # Check if the meta description is present.
    meta_description = await page.query_selector('meta[name="description"]')
    if meta_description is None:
        print('The meta description is not present.')
    else:
        print('The meta description is present.')

    # Check if the canonical URL is present.
    canonical_url = await page.evaluate('document.querySelector("link[rel=canonical]")?.href')
    if canonical_url is None:
        print('The canonical URL is not present.')
    else:
        print('The canonical URL is present.')

    # Check for schema markup.
    schema_markup = await page.evaluate('document.querySelector("script[type=application/ld+json]")?.text')
    if schema_markup is None:
        print('Schema markup is not present.')
    else:
        print('Schema markup is present.')

    # Check if the images have alt text.
    images = await page.query_selector_all('img')
    for image in images:
        alt_text = await image.get_attribute('alt')
        if alt_text is None or alt_text == '':
            print('The image {} does not have alt text.'.format(image.src))

    # Check if the page is using preloading.
    preloading_enabled = await page.evaluate('document.querySelector("link[rel=preload]") is not null')
    if preloading_enabled:
        print('Preloading is enabled.')
    else:
        print('Preloading is not enabled.')

    # Check if the page has pagination in the head.
    pagination_in_head = await page.evaluate('document.querySelector("link[rel=next]") is not null')
    if pagination_in_head:
        print('Pagination is in the head.')
    else:
        print('Pagination is not in the head.')

    await context.close()

if __name__ == '__main__':
    main()
