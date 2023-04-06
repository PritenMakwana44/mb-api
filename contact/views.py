from rest_framework import generics
from .models import Contact
from .serializer import ContactSerializer


class ContactDetail(generics.ListCreateAPIView):
    """Detail for contact form"""
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
