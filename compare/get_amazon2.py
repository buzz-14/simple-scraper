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
        if item is not None and item.find('span',{'class':'a-price-whole'}) is not None :
            item_data_link_name= item.find('a',{'class' :'a-link-normal a-text-normal'})
            item_data_price = item.find('span',{'class':'a-price-whole'})
            link= SITE + item_data_link_name['href']
            name = item_data_link_name.text.strip()
            price = item_data_price.text.strip().replace(",", "")
            clean_input = str_input.lower().split()
            present_flag = True
            for i in range(len(clean_input)):
                if clean_input[i] not in name.lower().replace(" ",""):
                    present_flag = False
            if present_flag == True:
                product_list.append([int(price),name,link])

    sorted_product_list =sorted(product_list,key=lambda x: (x[0]))
    product_list.clear()
    return sorted_product_list


