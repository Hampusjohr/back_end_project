from django.shortcuts import render
from rest_framework import viewsets
from .models import MenuItem
from .serializers import MenuItemSerializer
from rest_framework.permissions import AllowAny

class MenuItemsView(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [AllowAny]


