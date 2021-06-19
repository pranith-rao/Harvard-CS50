from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("newlist",views.newlist, name="newlist"),
    path("item/<int:newlist_id>",views.item,name="item"),
    path("bid/<int:newlist_id>",views.bid,name="bid"),
]
