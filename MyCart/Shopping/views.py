
from django.shortcuts import render,redirect
import  json
# Create your views here.
from django.contrib import messages
from django.http import HttpResponse
from .models import Product,ContactUs,Orders,OrderUpdate
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

from django.core.mail import send_mail
from math import *
import django.contrib.sessions
def index(request):
    products=Product.objects.all()
    print(products)


    allProds=[]
    catProds=Product.objects.values('category','id')
    print(catProds)
    categorys={ item['category'] for item in catProds }
    print(categorys)
    for cat in categorys:
        prod=Product.objects.filter(category=cat)
        n = len(prod)
        Noslides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod,range(1,Noslides),Noslides])

    #allProds = [[products, range(1, Noslides), Noslides],
     #                        [products, range(1, Noslides), Noslides]]
    params = {'allProds': allProds}
    if request.session.has_key('name'):
      print(request.session['name']+"In index")
      params['username']=request.session['name']
    return render(request,"Shopping/index.html",params)
def searchMatch(query, item):
    '''return true only if query matches the item'''
    if query in item.desc.lower() or query in item.product_name.lower() or query in item.category.lower():
        print(query)
        return True
    else:
        return False
def search(request):
    query = request.GET.get('search')
    products = Product.objects.all()
    print(products)

    allProds = []
    catProds = Product.objects.values('category', 'id')
    print(catProds)
    categorys = {item['category'] for item in catProds}
    print(categorys)
    for cat in categorys:
        prodtemp = Product.objects.filter(category=cat)
        prod = [item for item in prodtemp if searchMatch(query, item)]
        print(prod)
        n = len(products)
        Noslides = n // 4 + ceil((n / 4) - (n // 4))
        if len(prod) != 0:
            allProds.append([prod, range(1, Noslides), Noslides])


    # allProds = [[products, range(1, Noslides), Noslides],
    #                        [products, range(1, Noslides), Noslides]]
    params = {'allProds': allProds}

    return render(request, "Shopping/index.html", params)
def about(request):
    return render(request,"Shopping/about.html")
def contact(request):
    if request.method == "POST":
        name = request.POST.get('Name', '')
        email = request.POST.get('Email', '')
        phone = request.POST.get('Phone', '')
        desc = request.POST.get('Msg', '')
        contact = ContactUs(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request,"Shopping/ContactUs.html")
def track(request):
    if request.method == "POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Orders.objects.filter(order_id=orderId, email=email)
            if len(order) > 0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.order_desc, 'time': item.timestamp})
                    response = json.dumps({"Status":"Success","updates":updates,"itemsOrder":order[0].items_json}, default=str)
                    print(updates)
                    print(order[0].items_json)
                return HttpResponse(response)
            else:
                return HttpResponse({"Status":"Empty"})
        except Exception as e:
            return HttpResponse({"Status":"Error"})


    return render(request,"Shopping/Tracker.html")
def ProdView(request,p_id):
    product=Product.objects.filter(id=p_id)
    return render(request,"Shopping/ViewProduct.html",{'product':product[0]})
def checkout(request):
    if request.method == "POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('Name', '')
        price=request.POST.get('Amount','')
        email = request.POST.get('Email', '')
        address = request.POST.get('Address', '')
        city = request.POST.get('City', '')
        state = request.POST.get('State', '')
        zip_code = request.POST.get('Zip', '')
        phone = request.POST.get('Phone', '')
        order = Orders(items_json=items_json, name=name, email=email, address=address, city=city,
                       state=state, zip_code=zip_code, phone=phone,price=price)
        order.save()
        update = OrderUpdate(order_id=order.order_id, order_desc="The order has been placed")
        update.save()
        thank = True
        id = order.order_id
        send_mail("ABout Tracking Your Product","Your Tracker Id is "+ str(id), "harshpatel281199@gmail.com", [email], fail_silently=False)

        return render(request, 'Shopping/Checkout.html', {'thank': thank, 'id': id})
    if not request.session.has_key('name'):
        messages.warning(request,"Please Login First")
        return redirect("ShopHome")
    return  render(request,"Shopping/Checkout.html")

def enteruser(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['pass']
        user=User.objects.create_user(username,email,password)

        user.first_name=fname
        print(user.first_name)
        user.last_name=lname
        print(user.last_name)
        user.save()
        messages.success(request,"Your Details Are Added")
        return redirect('ShopHome')
    else:
        messages.ERROR(request, "Something Went Wrong")
        return redirect('ShopHome')


def loginprocess(request):
    if request.method=="POST":
        loginusername=request.POST['username']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username=loginusername,password=loginpassword)

        if user is not None:
            login(request,user)
            messages.success(request,"You Are Logged In")
            request.session['name']=loginusername
            print("inlogin "+request.session['name'])
            return redirect("ShopHome")
        else:
            messages.error(request,"Not A Member")
            return redirect("ShopHome")
    return HttpResponse("404- Not Found")

def logoutprocess(request):

    logout(request)
    messages.warning(request,"You Are LogOut")
    if request.session.has_key('name'):
        del request.session['name']
    return redirect("ShopHome")