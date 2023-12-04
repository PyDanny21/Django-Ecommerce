from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import Category,Product,CartItem,Profile
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.decorators import login_required
import random
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# Create your views here.
a=random.randint(0,7)
b=a+14

app_name='Core'
def index(request):
    latestPro=Product.objects.all()
    first= len(latestPro)-14
    second=len(latestPro)
    latest=Product.objects.filter(is_sold=False)[first:second]
    products=Product.objects.filter(is_sold=False)[a:b]
    # try:
    #     products=paginator.page(page)
    # except PageNotAnInteger:
    #     products=paginator.page(1)
    # except EmptyPage:
    #     products=paginator.page(paginator.num_pages)
        
    
    categories=Category.objects.all()
    Total_cart=CartItem.objects.count()
    return render(request,'core/index1.html',{
        'categories':categories,
        'products':products,
        'Total_cart':Total_cart,
        'latest':latest,
    })


def related(request,pk):
    related=get_object_or_404(Product,pk=pk)
    # related=Product.objects.get(pk=product_id)
    relatedCat=Product.objects.filter(category=related.category)
    Total_cart=CartItem.objects.count()
    return render(request,'core/search.html',{
        'relatedCat': relatedCat,
        'related':related,
        'Total_cart':Total_cart,

    })
    
def search(request):
    items=Product.objects.all()
    paginator=Paginator(items,28)
    page=request.GET.get('page')
    page_oj=Paginator.get_page(paginator,page)
    Total_cart=CartItem.objects.count()
    return render(request,'core/searchpage.html',{
        'items':items,
        'Total_cart':Total_cart,
        'page_oj':page_oj,

    })
   
def details(request,pk):
    details=get_object_or_404(Product,pk=pk)
    # related=Product.objects.get(pk=product_id)
    related_items=Product.objects.filter(category=details.category).exclude(pk=pk)[0:14]
    Total_cart=CartItem.objects.count()

    return render(request,'core/productpage.html',{
        'related_items': related_items,
        'details':details,
        'Total_cart':Total_cart,

    })
                  
def add_cart(request, pk):
    # Retrieve the product details from the database
    cart = get_object_or_404(Product, pk=pk)
    cart_item, created=CartItem.objects.get_or_create(cart=cart)
    cart_item.save()
    return HttpResponse('<h2 style="font-size: 30px;">Successful</h2>')


def view_cart(request):
    cart_items=CartItem.objects.all()
    Total_cart=CartItem.objects.count()
    return render(request,'core/cart.html',{
        'cart_items':cart_items,
        'Total_cart':Total_cart,

    })
    
def remove(request, cart_item_id):
    # Delete a CartItem object by its ID
    cart_item = get_object_or_404(CartItem, pk=cart_item_id)
    cart_item.delete()
    return redirect('view_cart')

def delete(request):
    # Delete a CartItem object by its ID
    cart_item = CartItem.objects.all()
    cart_item.delete()
    return redirect('view_cart')

# def plus(request,cart_item_id):
#     if request.method=='POST':
#         cart_item=CartItem.objects.get(pk=cart_item_id)
#         plusIt=cart_item.quantity
#         plusIt+=1
#         cart_item.save()
#         return redirect('view_cart')

#     return redirect('view_cart')


def signup(request):
    if request.method== 'POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']
        if password==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email taken')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username taken')
                return redirect('signup')
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save()

                #Log user in and redirect to settings page
                user_login=auth.authenticate(username=username,password=password)
                auth.login(request,user_login)
                #create profile object for the new user
                user_model=User.objects.get(username=username)
                new_profile=Profile.objects.create(user=user_model,user_id=user_model.id)
                new_profile.save()
                return redirect('signin')
        else:
            messages.info(request,'Password not matching!')
            return redirect('signup')
    else:
        return render(request,'core/signup.html')

def signin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid credentials')
            return redirect('signin')
    else:
        return render(request, 'core/signin.html')
    
@login_required(login_url='signin') 
def logout(request):
    auth.logout(request)
    return redirect('signin')


    