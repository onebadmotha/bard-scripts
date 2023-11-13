import asyncio
import playwright
from playwright.async_api import async_playwright

async def main(limit: int = 100):

    # Launch a Chromium browser with a mobile viewport.
    context = await async_playwright().chromium.launch(viewport={'width': 375, 'height': 667})

    # Create a new page.
    page = await context.new_page()

    # Set the user agent to 'Googlebot-Image/1.0'.
    await page.set_user_agent('Googlebot-Image/1.0')

    # Prompt the user for the sitemap URL.
    sitemap_url = input('Enter the sitemap URL: ')

    # Fetch the sitemap.
    await page.goto(sitemap_url)

    # Extract the image URLs from the sitemap.
    image_urls = []
    for link in await page.query_selector_all('url'):
        href = await link.get_attribute('loc')
        if href.endswith('.jpg') or href.endswith('.png') or href.endswith('.gif'):
            image_urls.append(href)

        if len(image_urls) >= limit:
            break

    # Fetch the image pages and check the status code and the image size.
    for image_url in image_urls:
        await page.goto(image_url)

        status_code = await page.status_code()
        if status_code != 200:
            print('The image {} could not be accessed.'.format(image_url))

        image_size = await page.evaluate('document.querySelector("img")?.naturalWidth')
        if image_size is None or image_size < 100:
            print('The image {} is too small.'.format(image_url))

    # Get the full-size image URL for each image.
    full_size_image_urls = []
    for image_url in image_urls:
        await page.goto(image_url)

        full_size_image_url = await page.evaluate('document.querySelector("img")?.src')

        full_size_image_urls.append(full_size_image_url)

    # Close the browser.
    await context.close()

    # Print the full-size image URLs.
    for full_size_image_url in full_size_image_urls:
        print(full_size_image_url)

if __name__ == '__main__':
    asyncio.run(main())