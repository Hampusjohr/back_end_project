from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'menu', views.MenuItemsView, basename='menu')

urlpatterns = [
    path('menu/',views.MenuItemsView.as_view({'get': 'list'}), name='menu-list'),
]
