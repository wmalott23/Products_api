from django.urls import path
from . import views

urlpatterns = [
    path('', views.reviews_list),
    path('<int:pk>/', views.reviews_detail),
    path('product/<int:pk>/', views.product_reviews)
]