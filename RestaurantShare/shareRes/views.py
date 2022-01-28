from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
from django.urls import reverse

from .models import *


def index22(request):
    #return HttpResponse("index test test")
    #return render(request, 'shareRes/index.html')
    categories = Category.objects.all()
    restaurants = Restaurant.objects.all();
    content = {'categories': categories, 'restaurants':restaurants}
    return render(request, 'shareRes/index.html', content)

def Delete_restaurant(request):
    resId = request.POST['resId']
    restaurant = Restaurant.objects.get(id = resId)
    restaurant.delete()
    return HttpResponseRedirect(reverse('index'))
    return

def restaurantDetail(request, res_id):
    restaurant = Restaurant.objects.get(id = res_id)
    content = {'restaurant' : restaurant}
    #return HttpResponse("restaurantDetail")
    return render(request, 'shareRes/restaurantDetail.html', content)

def Update_restaurant(request):
    resId = request.POST['resId']
    change_category_id = request.POST['resCategory']
    change_category = Category.objects.get(id = change_category_id)
    change_name = request.POST['resTitle']
    change_link = request.POST['resLink']
    change_content = request.POST['resContent']
    change_keyword = request.POST['resLoc']
    before_restaurant = Restaurant.objects.get(id = resId)
    before_restaurant.category = change_category
    before_restaurant.restaurant_name = change_name
    before_restaurant.restaurant_link = change_link
    before_restaurant.restaurant_content = change_content
    before_restaurant.restaurant_keyword = change_keyword
    before_restaurant.save()
    return HttpResponseRedirect(reverse('resDetailPage', kwargs={'res_id':resId}))

def restaurantUpdate(request, res_id):
    categories = Category.objects.all()
    restaurant = Restaurant.objects.get(id = res_id)
    content = {'categories': categories, 'restaurant':restaurant}
    # return HttpResponse("restaurantDetail")
    return render(request, 'shareRes/restaurantUpdate.html', content)

def restaurantCreate(request):
    #return HttpResponse("restaurantCreate")
    categories = Category.objects.all()
    content = {'categories': categories}
    return render(request, 'shareRes/restaurantCreate.html', content)

def Create_restaurant(request):
    category_id = request.POST['resCategory']
    category = Category.objects.get(id=category_id)
    name = request.POST['resTitle']
    link = request.POST['resLink']
    content = request.POST['resContent']
    keyword = request.POST['resLoc']
    new_res = Restaurant(category=category, restaurant_name=name,
                         restaurant_link=link, restaurant_content=content, restaurant_keyword=keyword)
    new_res.save()
    return HttpResponseRedirect(reverse('index'))


def categoryCreate(request):
    #return HttpResponse("categoryCreate")
    categories = Category.objects.all()
    content = {'categories': categories}
    return render(request, 'shareRes/categoryCreate.html', content)

# category create 과정.
def Create_category(request):
    #return HttpResponse("여기서 category Create 기능을 구현할 거야.")
    category_name = request.POST['categoryName'] # 사용자가 문자열을 입력 후 "추가" 버튼을 눌렀을 때 POST 방식으로 파라미터가 전달되므로,
    new_category = Category(category_name = category_name) #사요ㅇ자가 입력한 문자열 값을 category_name 변수에 담는다.
    new_category.save() # 데이터베이스에 저장하기 위해 save() 함수를 이용한다.
    #return HttpResponseRedirect(reverse('index'))
    return HttpResponseRedirect(reverse('cateCreatePage'))

def Delete_category(request):
    category_id = request.POST['categoryId']
    delete_category = Category.objects.get(id = category_id)
    delete_category.delete();
    return HttpResponseRedirect(reverse('cateCreatePage'))