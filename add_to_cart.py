import requests

cookies = """MRefererUrl=direct; mtc=s:eyJ0ZXN0Z3JvdXBzSGFzaCI6IjRhOTliODVjZmI2Yzk1YTFkZTEyZjEwZWFjNTViNWQ0NDM3OWExZjcyZWZjYmJiZGViM2FlNGUzOTVmOTM2ZjYiLCJoYXNoIjoiSkpLMnNNaUpVRHh5aDNjblhZekhGQT09Iiwic3RhYmxlIjpbInNwcy1zdG9jayIsInByZWZpbGxlZC1sb3dyYXRlIiwidHJveSIsImJhc2tldC1hcy1wcm9ncmVzc2JhciIsInNwcy1zdG9jay1ieS1pZGVudCIsImhvbWVwYWdlLXdpdGhvdXQtbXlwcm9kdWN0cyIsInBheWJhY2stcmV3ZS1uZXdzbGV0dGVyIiwiYWJ0LXBkcC1jb21iaW5lZC1kZXNjcmlwdGlvbiIsImNoZWNrb3V0LW1scy1jdXN0b21lci1hc3NpZ25tZW50IiwicGF5bWVudC1lbmFibGUtZ29vZ2xlLXBheSIsImFkZHJlc3MtYXV0b2NvbXBsZXRlIiwicGF5YmFjay10YXJnZXRlZC1idXJuIiwic2ZzLXBpY2t1cC1zdGFnZ2VyaW5nLWluZm9ib3giLCJwYXliYWNrLWVjb3Vwb24tYXBpIiwicmV3ZS1zc28iLCJvZmZlci1kZXRhaWxzLXRyYWNraW5nIiwicGF5YmFjay10YXJnZXRlZC1ib251cy1jb3Vwb24iLCJwYXliYWNrLWV2b3VjaGVyIiwicGF5YmFjay1jYXJkLWNoYW5nZSIsInBheW1lbnQtbmV3LWRpcmVjdC1kZWJpdC1pbnB1dCIsImNhdGVnb3J5LW92ZXJ2aWV3LXJlbmRlcmVyIiwicGF5bWVudC1lbmFibGUtYXBwbGUtcGF5IiwiY2F0ZWdvcnktb3ZlcnZpZXctcmVuZGVyZXItcmVsb2FkIiwia2FuZ2Fyb28tYWNjb3VudC1jb25zb2xlIiwibGQtcmVjaXBlLXJldmlld3MtdjIiLCJsZC1yZWNpcGUtcmV2aWV3cy12MiIsImhpZGUtcGF5YmFjayJdLCJyZHRnYSI6W10sIm10Y0V4cGlyZXMiOjB9.ovBXEL/XvgueaLjagEL1B81trYjcL7cQJYIr9l5FMY4; _rdfa=s:a5e02c18-dc00-4c98-b0c7-63ff78880fa0.aXE7QhQwcveGwhxyBIL7sL4IfbLmVK3kKt9vuYzzKSw; rstp=eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJhZXMxOTIiOiI2MDg3MTc3MGE2OGQ5MzFjNTYyZGIzMjQ3N2Q5MjVhMmNhNmFhMzEzZWZjNGEyZmM1NjQ0YjA4OTVhMjVhZmI0MGE3YjJlYzU2ZGMzYjQ0Y2E3MjA1NjA0ZThjNjQ3NTVhYjdiNmY5NDhmNWQ4N2U1ZTlmMjliMzg0MzUxMTg3MGUwMDM5NGUxYTc5OTQzYWFhOWIxZjc5Y2RlZGZmNjc4YTI1ZDRiOWE4OTEyZTg5MDM1YWFhODg2ZTJkNTQ4MjhlYmUwYzQ4ZjZkMzRiODJhMjhlZDIzYmIxOGIxM2NkZDE3ZmU3NDQ0YWI1Y2Q2NmI5NTY3ZTRhNTNjNThhZDI5MDExYmU3ZTFmOWZkNGM1MzUyMWJkOThmZDIwYWZkNDQ4NzhkZDcwNTNiYjdlOWRiM2U5MzNkODRlYWQ4NjJkZDMxNzA0NGNmZWExYTM4YzlkM2M2ZTE0MGU3NDI5NTY1NGMzMzgwZTZmMjYyOWNlMjM1MDU3YWY4NmY0OTg5MTc4YWYxMWEwMDU1MjVkYjk1Mzg1ZmE2NWIzYmMwNmYzZDY2ODZkM2M3ZGI4ZjA1Y2NjMDc1MmEyZjExZDI3OGRlY2YxN2RjNzk3M2YyODk5NGI3YmM1ODc4ZTg2MjJiMWYwY2QxYjA5ZmMxZWZkZmZkZDEwNWFmMWZlNWZmNDQ4NmIyMmQwMGJlZWY5ZmViNmQyYTc0ZTgyMjEzMDM3MjAyMDY5ZTQxZTc4NzcyYTBjNzFkMjY1OTFjN2MzYmRjNWJjNTcwMTU4MThkYWNlZmJmYWM0Y2ZiOTlmNGUxMTM2ZDgwODZkY2YxZGMxZjdmNGQwYjc4OWFjYWYyYzgwZjEzOGRlYzNmNmNlOWQ1NmI1MjVmZmM2NzcwNGFhN2NlZWI1ZWI2MzVmYjk2YzY5MWY2MjUzN2JkZmNlZTUzYzJiMzRmNmVkMDAwN2NiYTUzOGI1NjZkNmM5NDUxZDM4M2FhMWQ1YzBhNjE3NDVkNDM0MDFlMGZiZTkzOGYxMDQ2YTQ5ODEzNTQ2ZWY3MTdlOWI4OTIzMTM0MDBjMGU4Y2Y5ZjM1ZDYwNDBkNWJhN2VjMDM1YWZkMzYwYmYyYWRlMWEwNWVmYmZhNTIwZGZjYmUyNzM0MzNkNmNkN2Q0Y2Q5ZDFiYzgyZDJmYzRjYjQ5MjFiN2ZjNzg4NTY0M2E4OWI3YTZjN2Y2ZTI1MzA5ZTBhNWQzNDdhOGJiMDAyMzBkYjQzIiwiZXhwIjoxNzQ5MzYzODI3LCJpYXQiOjE3NDkzNjMyMjcsIml2IjoiczhlcnZlOS01bWhfV0RNQTVLbE1HQSJ9.C6bsV6iGqZcErDZyPSuN6HpGJoKjG6BjwjPq1czUS8ycrQ43ukLYL48v5KouOG6Jy0QJVLgRvxAAxzz1Ql9IUA; __cf_bm=0QS7khEgWoliLpgnvfnk0hcpFkQDhoDbD6tjPJPFf4Y-1749363227-1.0.1.1-8OW9zRrCJUe5CnKnj1jFF7VRDtUkPITBqBFtFR3MY..5HOF9FckxcIPWwaB9_X.qfxnK2nbV7DeMZrP5T1l8.iWDS6x1vUFC4.ka3VbWI.E; _cfuvid=NENWlhDeMNt3yjQvV9625gWQMj6FNYMWGR9wjS6ctu8-1749363227073-0.0.1.1-604800000; intentionLayerIsForced=true; cf_clearance=IvrktjuwE.3w4qmOhUv.9oFRa2NSnF84y1cSC2Ae2Ng-1749363230-1.2.1.1-JzpWMq.q_g_pyHGju5or8pWmCmB8j9eN0nCDNZg5VSFVqC0mrSDZCyjk.0cAUKxV.meSD0skP3H8tI5Fj3YqYbNBbX_.oY.Zh6LScd8lQSRIvPX_pSiFWupAZHR5DwjyjoTCAtGCxmr8ja0P96D1AL74sBbETJyzVUZM9FqOq1.ryRHn.EgldNwAAvIeNpWr20UWlyJYIIBrcAC.MtTfdo5eEc93JjUVyqN9q1nqLbokuQV3pfLSBEdZT0avU6zqqLAX66HhyYlbnW26ieHJthM8OOIAWUsJ5r_dmIYBfhzMZJme6rKHP4NBw4CMOvTXH8qZWrpwJE5n4kQx90hc6pBtwy52QxXEQMh4h6ATTf8; consentSettings={%22Usercentrics-Consent-Management-Platform%22:1%2C%22Adobe-Launch%22:1%2C%22AWIN%22:1%2C%22Cloudflare%22:1%2C%22Keycloak%22:1%2C%22gstatic-com%22:1%2C%22JSDelivr%22:1%2C%22jQuery%22:1%2C%22Google-Ad-Manager-Basis%22:1%2C%22Funktionale-Cookies-und-Speicher%22:1%2C%22GfK-SENSIC%22:1%2C%22Realperson-Chat-Suite%22:1%2C%22Cloudflare-Turnstile%22:1%2C%22ChannelPilot%22:0%2C%22artegic-ELAINE-Software%22:0%2C%22Outbrain%22:0%2C%22RDFA-Technologie-Statistik-%22:0%2C%22Adobe-Analytics%22:0%2C%22Mouseflow%22:0%2C%22Facebook-Pixel%22:0%2C%22Microsoft-Advertising-Remarketing%22:0%2C%22Google-Maps%22:0%2C%22YouTube-Video%22:0%2C%22Google-Ads-Conversion-Tracking%22:0%2C%22Google-Ads-Remarketing%22:0%2C%22Snapchat-Advertising%22:0%2C%22Pinterest-Tags%22:0%2C%22trbo%22:0%2C%22TikTok-Advertising%22:0%2C%22LinkedIn-Ads%22:0%2C%22Taboola%22:0%2C%22Vimeo%22:0%2C%22Cmmercl-ly%22:0%2C%22Google-Ad-Manager%22:0%2C%22RDFA-Technologie-Marketing-%22:0%2C%22The-Trade-Desk%22:0%2C%22tms%22:1%2C%22necessaryCookies%22:1%2C%22cmpPlatform%22:1%2C%22marketingBilling%22:1%2C%22fraudProtection%22:1%2C%22basicAnalytics%22:1%2C%22marketingOnsite%22:1%2C%22extendedAnalytics%22:0%2C%22serviceMonitoring%22:0%2C%22abTesting%22:0%2C%22conversionOptimization%22:0%2C%22feederAnalytics%22:0%2C%22personalAdsOnsite%22:0%2C%22remarketingOffsite%22:0%2C%22userProfiling%22:0%2C%22sessionMonitoring%22:0%2C%22targetGroup%22:0%2C%22advertisingOnsite%22:0}; websitebot-launch=human-mousemove; perfTimings=event188=1.04%2Cevent189; perfLoad=1.04"""

# Constant for your account (from Network tab)
customer_id = "46659854"
market_id = "461346"

# Products to add (mix of EAN and REWE internal IDs)
product_ids = [
    "4008452027602",    # Milk
    "4017100370007",    # Butterkeks
    "PJ9GUAE8",         # REWE batteries
]

headers = {
    "Host": "shop.rewe.de",
    "Accept": "application/vnd.com.rewe.digital.basket-v2+json",
    "Accept-Language": "en-US,en;q=0.5",
    "Content-Type": "application/json",
    "Origin": "https://shop.rewe.de",
    "Referer": "https://shop.rewe.de/",
    "Cookie": cookies,
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:139.0) Gecko/20100101 Firefox/139.0",
    "x-application-id": "rewe-basket",
    "x-instana-l": "1,correlationType=web",
    "x-instana-s": "static",
    "x-instana-t": "static",
    "x-origin": "AddToBasketV2"
}

payload = {
    "context": "product-list-search",
    "includeTimeslot": False,
    "quantity": 1
}

for product_id in product_ids:
    prefix = str(len(product_id))
    url = f"https://shop.rewe.de/api/baskets/listings/{prefix}-{product_id}-rewe-online-services|{customer_id}-{market_id}"
    print(f"🛒 Adding {product_id} using {url} ...")
    response = requests.post(url, json=payload, headers=headers)
    print(f"✅ Status: {response.status_code}")
    print(response.text)

