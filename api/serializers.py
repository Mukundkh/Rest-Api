from rest_framework import serializers
from api.models import Blog

class BlogSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Blog
        fields = ['id','title','content','author']

    def create(self, validated_data):
        return Blog.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.author = validated_data.get('author', instance.author)
        instance.save()
        return instance
     