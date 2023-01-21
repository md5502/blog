from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.filters import OrderingFilter, SearchFilter

from .serializers import PostListSerializer, PostDietaleSerializer, CategorySerializer
from blog.models import Post, Category, Comment
from .paginations import PostPageNumberPagination


class PostListViwe(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'content']
    ordering_fields = ['title', 'content']
    pagination_class = PostPageNumberPagination


class PostDetaleApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = PostDietaleSerializer
    queryset = Post.objects.all()


class CategoryListApiView(ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryDetaleApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
