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
    if soup.find('a',{'class':'_1fQZEK'}) is not None:
        flag_type2 = False
        search_results = soup.find_all('a',{'class':'_1fQZEK'})
    else:
        flag_type2 = True
        search_results = soup.find_all('div',{'class':'_4ddWXP'})
    for item in search_results:
        if item is not None :
            if flag_type2 == False :
                link= SITE + item['href']
                name = item.find('div',{'class':'_4rR01T'}).text.strip()
                price = item.find('div',{'class':'_30jeq3 _1_WHN1'}).text.strip().replace("," , "").replace("₹",'')
            else:
                link= SITE +item.find('a',{'class':'s1Q9rs'})['href']
                name = item.find('a',{'class':'s1Q9rs'}).text.strip()
                price = item.find('div',{'class':'_30jeq3'}).text.strip().replace("," , "").replace("₹",'')
        clean_input = str_input.lower().split()
        present_flag = True
        for i in range(len(clean_input)):
            if clean_input[i] not in name.lower().replace(" ",""):
                present_flag = False
        if "case" in name.lower().replace(" ","") or "cover" in name.lower().replace(" ","") or "glass" in name.lower().replace(" ","") or "tempered" in name.lower().replace(" ",""):
            present_flag = False   
        if present_flag == True:
            product_list.append([int(price),name,link])
    sorted_product_list =sorted(product_list,key=lambda x: (x[0]))
    product_list.clear()
    return sorted_product_list






