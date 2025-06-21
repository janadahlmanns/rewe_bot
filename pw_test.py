import asyncio
import httpx
from playwright.async_api import async_playwright

SERVER_URL = "http://192.168.178.71:5000/list"

# ✅ Dictionary of known item → product ID
known_products = {
    "Bananen": "23376267",
    "Zewa": "7322540973235"
}

async def fetch_item_list():
    async with httpx.AsyncClient() as client:
        response = await client.get(SERVER_URL)
        response.raise_for_status()
        return response.json()["items"]

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.connect_over_cdp("http://localhost:9222")
        context = browser.contexts[0]
        page = context.pages[0] if context.pages else await context.new_page()

        items = await fetch_item_list()

        for entry in items:
            name = entry["item"]
            product_id = known_products.get(name)

            if product_id:
                print(f"🔍 Searching for '{name}' (ID: {product_id})")
                await page.goto("https://shop.rewe.de/", wait_until="domcontentloaded")
                await asyncio.sleep(1)
                await page.fill('[aria-label="Produkte suchen"]', product_id)
                await page.keyboard.press("Enter")
                await page.wait_for_load_state("domcontentloaded")
                await asyncio.sleep(2)

                try:
                    await page.click('[aria-label="Menge erhöhen"]')
                    print(f"✅ Added '{name}' to cart")
                except Exception as e:
                    print(f"❌ Could not click 'Menge erhöhen' for '{name}': {e}")
            else:
                print(f"❓ '{name}' not in known_products → skipping for now")

asyncio.run(run())
