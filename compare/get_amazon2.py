import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
# from requests_html import HTMLSession

# html_data= requests.get(URL,headers=header).content
# soup=BeautifulSoup(html_data,'lxml')
ua=UserAgent()
header = {
    "User-Agent" : ua.random
}

product_list=[]

URL = "https://www.amazon.in/s?k="
SITE = "https://www.amazon.in"

def scrape_amazon(str_input):
    mod_URL= URL+str_input.replace(" ","+")
    html_data= requests.get(mod_URL,headers=header).content
    soup=BeautifulSoup(html_data,'lxml')
    search_results = soup.find_all('div',{'data-component-type':'s-search-result'})

    for item in search_results:
        item_data_link_name= item.find('a',{'class' :'a-link-normal a-text-normal'})
        item_data_price = item.find('span',{'class':'a-price-whole'})
        link= SITE + item_data_link_name['href']
        name = item_data_link_name.text.strip()
        price = item_data_price.text.strip().replace(",", "")
        if(str_input.replace(" ","").lower() in name.replace(" ", "").lower() and "case" not in name.replace(" ", "").lower() and "cover" not in name.replace(" ", "").lower() and "glass" not in name.replace(" ", "").lower()):
            product_list.append([int(price),name,link])

    sorted_product_list =sorted(product_list,key=lambda x: (x[0]))
    return sorted_product_list

