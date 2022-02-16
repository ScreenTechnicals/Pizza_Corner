from django.urls import path
from Home import views
urlpatterns = [
    path('', views.home, name="home"),
    path('orders/', views.orders, name="orders"),
    path('increament/', views.increament, name="increament"),
    path('decreament/', views.decreament, name="decreament"),
    path('menu/', views.menu, name="menu"),
    path('signup/', views.signup, name="signup"),
    path('login/', views.login, name="login"),
    path('deleteOrder/', views.deleteOrder, name="deleteOrder"),
    path('deleteAllOrders/', views.deleteAllOrders, name="deleteAllOrders"),
    path('orderConfirmed/', views.orderConfirmed, name="orderConfirmed"),
    path('profile/', views.profile, name="profile"),
    path('address/', views.address, name="address"),
    path('logout/', views.logout, name="logout"),
    path('contact/', views.contact, name="contact"),
]
