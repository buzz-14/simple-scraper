from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
from .get_amazon2 import scrape_amazon
from .get_flipkart import scrape_flipkart 

RANGE_SIZE= 4

def get_amz_obj(query):
    amz_item =[]
    amz_item.clear()
    amazon_li= scrape_amazon(query)[:RANGE_SIZE]
    range_len = RANGE_SIZE
    if len(amazon_li) < range_len:
        range_len  = len(amazon_li)
    for i in range(range_len):
        amz_item.append(Item())
    for i in range(range_len):
        amz_item[i].id = i+1
        amz_item[i].name = amazon_li[i][1]
        amz_item[i].price = amazon_li[i][0]
        amz_item[i].link = amazon_li[i][2]
        amz_item[i].image = ""
    return amz_item

def get_flip_obj(query):
    flip_item = []
    flipkart_li = scrape_flipkart(query)[:4]
    range_len = RANGE_SIZE
    if len(flipkart_li) < range_len:
        range_len  = len(flipkart_li)
    for i in range(range_len):
        flip_item.append(Item())
    for i in range(range_len):
        flip_item[i].id = i+1
        flip_item[i].name = flipkart_li[i][1]
        flip_item[i].price = flipkart_li[i][0]
        flip_item[i].link = flipkart_li[i][2]
        flip_item[i].image = ""
    return flip_item



def index(request):
    return render(request,'index.html')

def result(request):
    search = request.GET['query']
    flipkart_items = get_flip_obj(search)
    amazon_items = get_amz_obj(search)
    return render(request,'result.html',{'amazon': amazon_items, 'flipkart':flipkart_items ,})
    