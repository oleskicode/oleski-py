import requests
from bs4 import BeautifulSoup

baseurl = "https://freevpnplanet.com/"
text_to_verify = "Free VPN – Best Free Online VPN, Fast and Secure"

try:
    response = requests.get(baseurl)
    if response.status_code == 200:
        print("Status 200 OK")
        soup = BeautifulSoup(response.text, 'lxml')
        h1_exists = soup.find('h1', string = text_to_verify)
        print(h1_exists)
except requests.exceptions.RequestException as e:
    print(f"An error occurred while fetching the webpage: \n{e}")
finally:
    print("Finished")
