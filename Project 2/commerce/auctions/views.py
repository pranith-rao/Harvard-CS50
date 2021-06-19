from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib import messages
import datetime

from .models import User, auction, bids


def index(request):
    items = auction.objects.all()  
    return render(request, "auctions/index.html",context={
        'item':items
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def newlist(request):
    if request.method == 'POST':
        title = request.POST['title']
        desc = request.POST['desc']
        bid = request.POST['bid']
        category = request.POST['category']
        time = datetime.datetime.now()
        user = request.user.username
        if request.POST.get('listimg'):
            listimg = request.POST['listimg']
        else:
            listimg = "https://askleo.askleomedia.com/wp-content/uploads/2004/06/no_image-300x245.jpg"
        item = auction(title=title,description=desc,bid=bid,category=category,image=listimg,time=time,user=user,current_bid=0)
        item.save()
        messages.success(request, 'Item added successfully')
        return redirect(reverse(index))
    return render(request, "auctions/listing.html")

def item(request,newlist_id):
    item = auction.objects.get(id=newlist_id)
    return render(request,"auctions/item.html",{
        "item":item
    })

def bid(request,newlist_id):
    if request.method == "POST":
        bid = int(request.POST['bid'])
        items = auction.objects.get(id=newlist_id)
        if bid <= items.bid and bid <= items.current_bid:
            messages.error(request, 'Bid must be higher than the current price')
            return redirect(reverse("item",kwargs={"newlist_id":newlist_id}))
        else:
            item_name = items.title
            user = request.user
            current_bid = bid
            bid = bids(item_name=item_name, username=user, current_bid=current_bid)
            bid.save()
            items.current_bid = current_bid
            items.save()
            return redirect(reverse("item",kwargs={"newlist_id":newlist_id}))


