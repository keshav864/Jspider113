from bs4 import BeautifulSoup
import requests

url = "http://ful.io"
r = requests.get(url)
sm_sites = ['https://www.facebook.com/fulioTech/','https://www.linkedin.com/company/ful-io/']

soup = BeautifulSoup(r.content, 'html5lib')
all_links = soup.find_all('a', href = True)


for site in sm_sites:
    if all(site in sm_sites for link in all_links):
        print(site)
    else:
        print('no link')