from rest_framework import generics
from .serializers import LiquorSerializer
from .models import Liquor

class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Liquor.objects.all()
    serializer_class = LiquorSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new liquor."""
        serializer.save()

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Liquor.objects.all()
    serializer_class = LiquorSerializer