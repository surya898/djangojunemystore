"""
URL configuration for mystore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()  #this is creating a object
router.register('api/products',views.productViewsetView,basename='products') #viewset verumbo automatic url create cheyyan
router.register("users",views.UserView,basename='user')
router.register('carts',views.Cartview,basename='carts')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('products',views.productView.as_view()),
    path('products/<int:id>/',views.productdetailView.as_view()),   #apiview verumbo
    # path('carts/<int:id>/',views.Cartview.as_view())
    path('reviews/<int:id>/',views.ReviewView.as_view()),
]+router.urls
