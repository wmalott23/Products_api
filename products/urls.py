from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    # path('', views.products_list),
    # path('<int:pk>/', views.product_detail),
    path('', views.ProductList.as_view()),
    path('<int:pk>/', views.ProductDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)