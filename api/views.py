from django.shortcuts import render
from rest_framework.response import Response
from api.models import Blog
from api.serializers import BlogSerializer
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import mixins
from rest_framework import generics

from rest_framework.decorators import api_view

#using generic class based views

class BlogList(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
