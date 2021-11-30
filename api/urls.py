from django.urls import path
from api import views
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
   
    path('blogs/', views.BlogList.as_view(), name='blog-list'),
    path('blogs/<int:pk>/', views.BlogDetail.as_view(), name='blog-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

