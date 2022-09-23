import requests
from bs4 import BeautifulSoup
import smtplib

MY_EMAIL = "example@mail.com"
GMAIL_PASSWORD = "password to MY_EMAIL"
BUY_PRICE = 90

URL = "https://www.amazon.de/-/en/Logitech-wireless-ultra-lightweight-programmable-additives/dp/B07W4DHKTD/" \
      "ref=sr_1_2?keywords=logitech%2Bg%2Bpro%2Bx%2Bsuperlight&" \
      "qid=1663945187&sprefix=logitech%2B%2Caps%2C85&sr=8-2&th=1"

header_config = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.8"
}

response = requests.get(URL, headers=header_config)
response.raise_for_status()
soup = BeautifulSoup(response.text, 'html.parser')

price = soup.find(name="span", class_="a-offscreen").getText()
price_num = float(price[1::])

if price_num < BUY_PRICE:
    title = soup.find(id="productTitle").get_text().strip()
    message = f"{title} is now {price}"

    print(f"{title} is now {price}")

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login(user=MY_EMAIL, password=GMAIL_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}"
        )
