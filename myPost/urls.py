from django.urls import path
from myPost import views
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
   
    path('posts/', views.PostList.as_view(), name='post-list'),
    path('posts/<int:pk>/', views.PostDetail.as_view(), name='post-detail'),
]
urlpatterns = format_suffix_patterns(urlpatterns)

