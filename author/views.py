from django.contrib.postgres.aggregates import ArrayAgg
from django.contrib.postgres.fields import ArrayField
from django.db.models import Subquery, OuterRef, F, Value
from django.db.models.functions import Concat
from django.db.models import CharField

from author.models import Author, Books
from rest_framework.generics import ListAPIView

from .serializers import AuthorSerializer


# class AuthorsApiView(ListAPIView):
#     serializer_class = AuthorSerializer
#     MODEL = Author
#     ordering = ["-created_at"]
#
#     def get_queryset(self):
#         return self.MODEL.objects.annotate(
#            book_names=Subquery(
#                 Books.objects.filter(author_id=OuterRef("id"))
#                     .values("author_id")
#                     .annotate(book_names=ArrayAgg("name"))
#                     .values("book_names")
#                 )
#         ).all()


class AuthorsApiView(ListAPIView):
    serializer_class = AuthorSerializer
    MODEL = Author
    ordering = ["-created_at"]

    def get_queryset(self):
        return self.MODEL.objects.all()