
"""djangoProject3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include

from trouvetonchamp.views import Index, Products, CreateProduct, RegisterFormView, ProductsUser, ProductSearchView, \
    UpdateProduct

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view(), name="index"),
    path('product/user', ProductsUser.as_view(), name="product_user"),
    path('product-detail/<int:pk>', Products.as_view(), name="product"),
    path('createproduct', CreateProduct.as_view(), name="createproduct"),
    path('updateproduct/<int:pk>', UpdateProduct.as_view(), name='product_update'),
    path('product/search/<str:search>', ProductSearchView.as_view(), name='product_search'),
    path('register', RegisterFormView.as_view(), name='register'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('accounts/', include('django.contrib.auth.urls'))
]
