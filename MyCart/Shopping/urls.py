from django.urls import  path
from . import  views

urlpatterns = [
    path("",views.index,name="ShopHome"),
    path("about/",views.about,name="AboutUs"),
    path("contact/",views.contact,name="Contact"),
    path("TrackProduct/",views.track,name="Track"),
    path("search/",views.search,name="Search"),
    path("checkout/", views.checkout, name="Checkout"),
    path("enteruser/", views.enteruser, name="SignUp"),
    path("loginprocess/", views.loginprocess, name="loginprocess"),
    path("logoutprocess/", views.logoutprocess, name="logoutprocess"),
    path("ViewProduct/<int:p_id>",views.ProdView,name="Viewmode"),

]