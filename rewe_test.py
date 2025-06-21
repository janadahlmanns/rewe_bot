import requests

url = "https://shop.rewe.de/api/baskets/listings/13-8717428071131-rewe-online-services%7C46659854-461346"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:139.0) Gecko/20100101 Firefox/139.0",
    "Accept": "application/vnd.com.rewe.digital.basket-v2+json",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Referer": "https://shop.rewe.de/c/obst-gemuese/?source=homepage-category",
    "cache-control": "no-cache",
    "content-type": "application/json",
    "pragma": "no-cache",
    "x-application-id": "rewe-basket",
    "x-instana-l": "1,correlationType=web;correlationId=b6e7f588e7fc4465",
    "x-instana-s": "b6e7f588e7fc4465",
    "x-instana-t": "b6e7f588e7fc4465",
    "x-origin": "AddToBasketV2",
    "Origin": "https://shop.rewe.de",
    "Alt-Used": "shop.rewe.de",
    "Connection": "keep-alive",
    "Cookie": """__cf_bm=AxTGBxQQYZqUmHtWSl3nc2RpJaZ3RUpr28BBm5X8eLo-1749365638-1.0.1.1-BP0zEteLHWYCScDTst7GahMPS9s2Kj_6XzXSrR5mMnQI4OJKVViNEliawQV_iW9LUAcAzH_H0pyx5uRVlbMWwRTzFfXrYIXHEjQMP8VbJQU; _cfuvid=V_FCobkScy91RajPH_Nh9ihJb9bIeJgRiF4.NkUPlZc-1749364445592-0.0.1.1-604800000; _rdfa=s:a5e02c18-dc00-4c98-b0c7-63ff78880fa0.aXE7QhQwcveGwhxyBIL7sL4IfbLmVK3kKt9vuYzzKSw; cf_clearance=hHqVlp3f0YYq_VCC4cltuqAVHJ9L437t78QbrenG334-1749364447-1.2.1.1-1qPuyzZXo7HobBsChi9SypPXDEBD35j83FQbPFUyQSrNCwm.3ZyWMbsATc0moaTumm_ifIRgjspWuZyaFMDID4Ws5KlToD7Ewu8wwR7gNJLRqIFWSa.yfUZRQXtGVRZ4KiJw8vsFw50i5lkmS5JzoptvTNZ6t1BwImmaab7pFvo1H7NBowyTXFyXKlmDC08ngQ1VlqVMhtDOw7n7uAzqk_zoiGnyW4scpgkLv48DZtdrgZlN7EtTBm6A1QfB8iG5TNxFZOYi9z9TwiDczXFYktvLCbm1StOYMwrC7kWUNiskt3ZR06sm2BJ6iSZg2Okvnmlg8X8_.4erkbUD33.LKIGAPwTsFIjAqeO4Lym1TFA; consentSettings={%22Usercentrics-Consent-Management-Platform%22:1%2C%22Adobe-Launch%22:1%2C%22AWIN%22:1%2C%22Cloudflare%22:1%2C%22Keycloak%22:1%2C%22gstatic-com%22:1%2C%22JSDelivr%22:1%2C%22jQuery%22:1%2C%22Google-Ad-Manager-Basis%22:1%2C%22Funktionale-Cookies-und-Speicher%22:1%2C%22GfK-SENSIC%22:1%2C%22Realperson-Chat-Suite%22:1%2C%22Cloudflare-Turnstile%22:1%2C%22ChannelPilot%22:0%2C%22artegic-ELAINE-Software%22:0%2C%22Outbrain%22:0%2C%22RDFA-Technologie-Statistik-%22:0%2C%22Adobe-Analytics%22:0%2C%22Mouseflow%22:0%2C%22Facebook-Pixel%22:0%2C%22Microsoft-Advertising-Remarketing%22:0%2C%22Google-Maps%22:0%2C%22YouTube-Video%22:0%2C%22Google-Ads-Conversion-Tracking%22:0%2C%22Google-Ads-Remarketing%22:0%2C%22Snapchat-Advertising%22:0%2C%22Pinterest-Tags%22:0%2C%22trbo%22:0%2C%22TikTok-Advertising%22:0%2C%22LinkedIn-Ads%22:0%2C%22Taboola%22:0%2C%22Vimeo%22:0%2C%22Cmmercl-ly%22:0%2C%22Google-Ad-Manager%22:0%2C%22RDFA-Technologie-Marketing-%22:0%2C%22The-Trade-Desk%22:0%2C%22tms%22:1%2C%22necessaryCookies%22:1%2C%22cmpPlatform%22:1%2C%22marketingBilling%22:1%2C%22fraudProtection%22:1%2C%22basicAnalytics%22:1%2C%22marketingOnsite%22:1%2C%22extendedAnalytics%22:0%2C%22serviceMonitoring%22:0%2C%22abTesting%22:0%2C%22conversionOptimization%22:0%2C%22feederAnalytics%22:0%2C%22personalAdsOnsite%22:0%2C%22remarketingOffsite%22:0%2C%22userProfiling%22:0%2C%22sessionMonitoring%22:0%2C%22targetGroup%22:0%2C%22advertisingOnsite%22:0}; intentionLayerIsForced=true; MRefererUrl=direct; mtc=s:eyJ0ZXN0Z3JvdXBzSGFzaCI6IjRhOTliODVjZmI2Yzk1YTFkZTEyZjEwZWFjNTViNWQ0NDM3OWExZjcyZWZjYmJiZGViM2FlNGUzOTVmOTM2ZjYiLCJoYXNoIjoiSkpLMnNNaUpVRHh5aDNjblhZekhGQT09Iiwic3RhYmxlIjpbInNwcy1zdG9jayIsInByZWZpbGxlZC1sb3dyYXRlIiwidHJveSIsImJhc2tldC1hcy1wcm9ncmVzc2JhciIsInNwcy1zdG9jay1ieS1pZGVudCIsImhvbWVwYWdlLXdpdGhvdXQtbXlwcm9kdWN0cyIsInBheWJhY2stcmV3ZS1uZXdzbGV0dGVyIiwiYWJ0LXBkcC1jb21iaW5lZC1kZXNjcmlwdGlvbiIsImNoZWNrb3V0LW1scy1jdXN0b21lci1hc3NpZ25tZW50IiwicGF5bWVudC1lbmFibGUtZ29vZ2xlLXBheSIsImFkZHJlc3MtYXV0b2NvbXBsZXRlIiwicGF5YmFjay10YXJnZXRlZC1idXJuIiwic2ZzLXBpY2t1cC1zdGFnZ2VyaW5nLWluZm9ib3giLCJwYXliYWNrLWVjb3Vwb24tYXBpIiwicmV3ZS1zc28iLCJvZmZlci1kZXRhaWxzLXRyYWNraW5nIiwicGF5YmFjay10YXJnZXRlZC1ib251cy1jb3Vwb24iLCJwYXliYWNrLWV2b3VjaGVyIiwicGF5YmFjay1jYXJkLWNoYW5nZSIsInBheW1lbnQtbmV3LWRpcmVjdC1kZWJpdC1pbnB1dCIsImNhdGVnb3J5LW92ZXJ2aWV3LXJlbmRlcmVyIiwicGF5bWVudC1lbmFibGUtYXBwbGUtcGF5IiwiY2F0ZWdvcnktb3ZlcnZpZXctcmVuZGVyZXItcmVsb2FkIiwia2FuZ2Fyb28tYWNjb3VudC1jb25zb2xlIiwibGQtcmVjaXBlLXJldmlld3MtdjIiLCJsZC1yZWNpcGUtcmV2aWV3cy12MiIsImhpZGUtcGF5YmFjayJdLCJyZHRnYSI6W10sIm10Y0V4cGlyZXMiOjB9.ovBXEL/XvgueaLjagEL1B81trYjcL7cQJYIr9l5FMY4; perfLoad=3.65; perfTimings=event188=3.65%2Cevent189; rstp=eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJhZXMxOTIiOiI4NDkzNzI5MjVmMWEyZTM3NTZiM2VjOTM3MzAxMTM1MjFlNjcyNzI1ZDdjM2VjYmVmNzFjMDFkOTJkZDI1MjY0ZGMwZDkwMjI3MDlhYmFjN2QyMTU0NzNiOWVmY2ZmYzRmNGI0MWExNjk3Nzg4NWU0YzY3YWM3NWYxMjIyYmZhOTE0MDk4MjE2YmQ2NTEzNGRmODBjZDYxMGI4NWUxMGU0NmRjMTNjNjEyNGZmZGFjMDkxNzBkYWEyYzA2N2ZjZDRkOWUyYzk5NGNkNGJkMDM1YTFmZGE3NzNiYmM5MjljMWViMWI1YTk0OGYwZTMwZTYwN2UzMjE4NzM3M2ZlYTE4ZTYzMjM0MGViMThlMWEyYzE4ZGFiMmE5Yzc0OTQ0ZTZhNDE2M2MyMjA2NDc3YjU5MDQyYWI5NzI5Y2E2ZmI5ODNkODhmOTA1OThjODYwYzYyYmViNmUzYWI1Mzg4NzlkYTk2ZTBmYTA3MGNhNmRkYzM1ODBkMDgzYWQzZjM5YTcwYzY2ODQ1NmIzYWFjNzk4NGUzYWU3Zjg2NDE0ZDgxOWZmYmQyMmM4M2FmNTc4MzdhMzljMTVlZTZlNTc2NThmOTZhZTk2MzhhZTNmM2Q3NzFjNTgyNDU5NDlmNmU1YWYzZGNmMGMxMjNmYzA1MWM0MDljNTNkNjdiY2I5NTRjYWM2ZTE1OTk2NDQyNjQ5OGFhOTQ1OGMwYjI3NDBkMjNhMWIyYTI4MjQ0ZmU4YTdiYjE0MTJjZTk3NDQ1OWZiYjA5MjRiMWY2ZGUzMTBiMWJjMzFlMjJlYTJkYzhmM2I1ZDQ1YjFiOWE4ZDA4Y2JlNjdmMjlmNmVhNmMxYzIyYjJhYmM4NDFhYmFmOWZjMDA2ODUxOTBkYWE0MzE4NWZhNDhiMzNiY2U5ZWFlNmYyYjdmMDJlYjgxZTM2NjhkNzExMTU1ZjFkMTQ2MTBiYzMxMGZlYjEzYjE5YWNkYzFkYzIxOWU5Zjg5OGY2NzZlNjBmMTNiZDNjZGE5ZjM1MDU0M2U0NmUyNjAxMzgxOWFkYWFmYjczZDRkOWY0YTJhZWQwNTkxZWEwODZlNWM1Y2U4Y2VjMzNjNWFhZTU0YmQ5OWE2NTJmOTgyMmRjMDM3MTJjMDk2OTEwZTgyMGU1MjcwZTljM2VmYzc5MmUwMzU4Yjc0NTViMDczZGZmMDVlNmU0Mjg2YTk0MmIzN2JkNmEzODAyNDQ4ZTliNjdlYzAxMWY0IiwiZXhwIjoxNzQ5MzY1OTExLCJpYXQiOjE3NDkzNjUzMTEsIml2IjoiSmZUWDN2UG5OSTdwWmRkUzFBalFrQSJ9.pN6tPAkLGb16SsVmT5unH05Wpb7PYOZPgSKgoFIGewovOfIg0tCqdqzLoXUIaFBuVLgjT9yccX6U71JuRBvbdw; websitebot-launch=human-mousemove"""
    }

json_data = {
    "quantity": 1,
    "includeTimeslot": False,
    "context": "product-list-category"
}

response = requests.post(url, headers=headers, json=json_data)

print("Status:", response.status_code)
print("Response:", response.text)
