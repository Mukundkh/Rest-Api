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

#listing all the blogs or creating new blog
class BlogList(APIView):
    def get(self, request, format=None):
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#fetch, update and delete blogs
class BlogDetail(APIView):
    def get_object(self, pk):
        try:
            return Blog.objects.get(pk=pk)
        except Blog.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        blogs = self.get_object(pk)
        serializer = BlogSerializer(blogs)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        blogs = self.get_object(pk)
        serializer = BlogSerializer(blogs, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        blogs = self.get_object(pk)
        blogs.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#generic class based-views
# class BlogList(generics.ListCreateAPIView):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer


# class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer
