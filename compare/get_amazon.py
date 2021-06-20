# import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession
from fake_useragent import UserAgent

# html_data= requests.get(URL,headers=header).content
# soup=BeautifulSoup(html_data,'lxml')
ua=UserAgent()
header = {
    "User-Agent" : ua.random
}

product_list=[]

URL = "https://www.amazon.in/s?k="
SITE = "https://www.amazon.in"

session=HTMLSession()

def data(URL):
    r=session.get(URL, headers= header)
    r.html.render(sleep=1,timeout=30)
    soup=BeautifulSoup(r.html.html,'lxml')
    return soup
    

def get_next__page(soup):
    pg= soup.find('ul',{'class':'a-pagination'})
    if not pg.find('li',{'class' : 'a-disabled a-last'}):
        url = 'https://www.amazon.in/'+ str(pg.find('li',{'class':'a-last'}).find('a')['href'])
        return url
    else:
        return
        
def scrape_amazon(str_input):
    mod_URL= URL+str_input.replace(" ","+")
    soup = data(mod_URL)
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

