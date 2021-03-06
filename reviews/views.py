from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import ReviewSerializer
from .models import Review
from rest_framework import generics



class ReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ProductReview(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    def filter_queryset(self, queryset):
        product = self.kwargs['pk']
        return queryset.filter(prod_num=product)

# Create your views here.

# @api_view(['GET', 'POST'])
# def reviews_list(request):
#     if request.method == 'GET':
#         reviews = Review.objects.all()
#         serializer = ReviewSerializer(reviews, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = ReviewSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

# @api_view(['GET', 'PUT', 'DELETE'])
# def reviews_detail(request, pk):
#     review = get_object_or_404(Review, pk=pk)
#     if request.method == 'GET':
#         serializer = ReviewSerializer(review)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = ReviewSerializer(review, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#     elif request.method == 'DELETE':
#         review.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def product_reviews(request, pk):
    if request.method == 'GET':
        reviews = Review.objects.filter(prod_num=pk)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
