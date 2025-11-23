from rest_framework import serializers
from .models import book    

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = book
        fields = ['id', 'title', 'author', 'published_date']

