from django.contrib.auth.models import User
from rest_framework import serializers
from books_api.models import Book


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "is_staff"]


class BookModelSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    release = serializers.DateTimeField(required=False)
    writer = serializers.CharField(required=False, allow_blank=True, max_length=100)
    name = serializers.CharField(required=True, allow_blank=True, max_length=100)
    genre = serializers.CharField(required=False, allow_blank=True, max_length=100)
    synopsis = serializers.CharField(required=False, allow_blank=True, max_length=100)
    price = serializers.IntegerField()

    def create(self, validated_data):
        return Book.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.release = validated_data.get("release", instance.release)
        instance.writer = validated_data.get("writer", instance.writer)
        instance.name = validated_data.get("name", instance.name)
        instance.genre = validated_data.get("genre", instance.genre)
        instance.synopsis = validated_data.get("synopsis", instance.synopsis)
        instance.price = validated_data.get("price", instance.price)
        instance.save()
        return instance


class BookSerializer(BookModelSerializer):
    class Meta:
        model = Book
        fields = ["release", "writer", "name", "genre", "synopsis", "price"]
