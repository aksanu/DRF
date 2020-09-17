from django.shortcuts import render
from .models import Customer
from .serializers import customerSerializer
from rest_framework import generics

# Create your views here.


class customerListCreateAPIView(generics.ListCreateAPIView):
	queryset= Customer.objects.all()
	serializer_class= customerSerializer


class customerRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
	queryset= Customer.objects.all()
	serializer_class= customerSerializer