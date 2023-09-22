from author.models import Author
from rest_framework.generics import ListAPIView

from .serializers import AuthorSerializer


class AuthorsApiView(ListAPIView):
    serializer_class = AuthorSerializer
    MODEL = Author
    ordering = ["-created_at"]

    def get_queryset(self):
        return self.MODEL.objects.all()