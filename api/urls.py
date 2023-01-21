from .views import PostListApiView, PostDetaleApiView, CategoryListApiView, CategoryDetaleApiView
from django.urls import path

app_name = 'api'

urlpatterns = [
    path('posts/', PostListApiView.as_view()),
    path('posts/<int:pk>', PostDetaleApiView.as_view(), name='Post_detail'),
    path('categorys', CategoryListApiView.as_view()),
    path('categorys/<int:pk>', CategoryDetaleApiView.as_view()),
]
