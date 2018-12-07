
import urllib3
from bs4 import BeautifulSoup
import requests
import time
# Fetch the html file


urls=['https://www.amazon.com/dp/B06XCM9LJ4/ref=fs_ods_aucc_rd','https://www.amazon.com/dp/B0792KTHKJ/ref=ods_gw_d_cmdw_dnut_aucc_1127?pf_rd_p=984825d7-7af6-44a5-953c-1d5e3c0af1f5&pf_rd_r=N7S1PKSXRX94TFDMR7XH']

total=0
while True:
    for x in urls:
    # http = urllib3.PoolManager()
        response = requests.get(x)
    
        html_doc = response.text

# Parse the html file
        soup = BeautifulSoup(html_doc, "html.parser")
        print(soup)
# Format the parsed html file
        strhtm = soup.prettify()
        test=soup.findAll('span')
        print(test)
        # for x in soup.find_all(id='priceblock_dealprice'): 
        #     print(x)
        #     y=x.split("$")
        #     total=total+float(y[1])

    print(total)
    time.sleep(10)
