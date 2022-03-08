"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as django_auth_views

from . import views

app_name = 'amazon'

urlpatterns = [
    path('', views.Login.as_view(), name = "login"),
    path('logout', django_auth_views.LogoutView.as_view(), name = 'logout'),
    path('lp/', views.Lp.as_view(), name='lp'),
    path('items/', views.ItemList.as_view(), name = 'item_list'),
    path('item/<int:pk>', views.ItemDetail.as_view(), name = 'item_detail'),
    path('sign_up/', views.SignUp.as_view(), name='sign_up'),
    path('sign_up/done/<token>', views.SignUpDone.as_view(), name='sign_up_done'),
    path('cart/<int:pk>', views.ShoppingCartDetail.as_view(), name='cart'),
    path('ajax_amount/', views.update_cart_item_amount, name='update_cart_item_amount'),
    path('ajax_delete/', views.delete_cart_item, name='delete_cart_item')
]
