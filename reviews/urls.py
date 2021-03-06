from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    # path('', views.reviews_list),
    # path('<int:pk>/', views.reviews_detail),
    # path('product/<int:pk>/', views.product_reviews)
    path('', views.ReviewList.as_view()),
    path('<int:pk>/', views.ReviewDetail.as_view()),
    path('product/<int:pk>/', views.ProductReview.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)