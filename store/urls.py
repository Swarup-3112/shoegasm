from . import views
from django.urls import path 

urlpatterns = [
    path('',views.home , name="home"),
    path('store/',views.store , name="store"),
    path('store/<str:id>/',views.shoeprofile , name="shoeprofiles"),
    path('men-store/Sport',views.menstoresport , name="mensport"),
    path('men-store/Sneaker',views.menstoresneaker , name="mensneaker"),
    path('men-store/Casual',views.menstorecasual , name="mencasual"),
    path('women-store/Sport',views.womenstoresport , name="womensport"),
    path('women-store/Sneaker',views.womenstoresneaker , name="womensneaker"),
    path('women-store/Casual',views.womenstorecasual , name="womencasual"),
    path('trial/',views.home1 , name="home1"),
]