from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent

ua=UserAgent()
header = {
    "User-Agent" : ua.random
}

product_list=[]

URL = "https://www.flipkart.com/search?q="
SITE = "https://www.flipkart.com"
    
def scrape_flipkart(str_input):
    mod_URL= URL+str_input.replace(" ","%20")
    html_data= requests.get(mod_URL,headers=header).content
    soup=BeautifulSoup(html_data,'lxml')
    search_results = soup.find_all('a',{'class':'_1fQZEK'})

    for item in search_results:
        link= SITE + item['href']
        name = item.find('div',{'class':'_4rR01T'}).text.strip()
        price = item.find('div',{'class':'_30jeq3 _1_WHN1'}).text.strip().replace("," , "").replace("₹",'')
        if(str_input.replace(" ","").lower() in name.replace(" ", "").lower() and "case" not in name.replace(" ", "").lower() and "cover" not in name.replace(" ", "").lower() and "glass" not in name.replace(" ", "").lower()):
            product_list.append([int(price),name,link])

    sorted_product_list =sorted(product_list,key=lambda x: (x[0]))
    return sorted_product_list







