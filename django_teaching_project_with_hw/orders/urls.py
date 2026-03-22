from django.urls import path
from . import views

urlpatterns = [
    path('orders/', views.orders),
    path('', views.OrderListView.as_view(), name='order-list'),
    path('orders/<int:id>/', views.order_detail),
    path('groups/', views.group, name='group-list'),
    path('groups/<int:id>/', views.group_detail, name='group-detail'),
]