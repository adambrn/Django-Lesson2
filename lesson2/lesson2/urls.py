"""
URL configuration for lesson2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from task1 import views

urlpatterns = [
    path("admin/", admin.site.urls),

    # URL для home
    path('', views.index, name='index'),

    # URL для создания клиента
    path('client/create/', views.create_client, name='create_client'),

    # URL для просмотра клиента
    path('client/<int:client_id>/', views.client_detail, name='client_detail'),

    # URL для просмотра списка клиентов
    path('clients/', views.client_list, name='client_list'),

    # URL для обновления клиента
    path('client/<int:client_id>/update/', views.update_client, name='update_client'),

    # URL для удаления клиента
    path('client/<int:client_id>/delete/', views.delete_client, name='delete_client'),

    # URL для создания товара
    path('product/create/', views.create_product, name='create_product'),

    # URL для просмотра товара
    path('product/<int:product_id>', views.product_detail, name='product_detail'),

    # URL для просмотра списка товаров
    path('products/', views.product_list, name='product_list'),

    # URL для обновления товара
    path('product/<int:product_id>/update/', views.update_product, name='update_product'),

    # URL для удаления товара
    path('product/<int:product_id>/delete/', views.delete_product, name='delete_product'),

    # URL для создания заказа
    path('order/create/', views.create_order, name='create_order'),

    # URL для просмотра заказа
    path('order/<int:order_id>/', views.order_detail, name='order_detail'),

    # URL для просмотра списка заказов
    path('orders/', views.order_list, name='order_list'),

    # URL для обновления заказа
    path('order/<int:order_id>/update/', views.update_order, name='update_order'),

    # URL для удаления заказа
    path('order/<int:order_id>/delete/', views.delete_order, name='delete_order'),
]
