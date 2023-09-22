from rest_framework import serializers

from .models import Author


class AuthorSerializer(serializers.ModelSerializer):
    book_names = serializers.SerializerMethodField()
    class Meta:
        model = Author
        fields = [
            "id",
            "first_name",
            "last_name",
            "book_names"
        ]

    def get_book_names(self, obj):
        return list(obj.books.values_list('name', flat=True))