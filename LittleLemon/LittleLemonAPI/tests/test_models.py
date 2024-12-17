from django.test import TestCase
from LittleLemonAPI.models import MenuItem
from LittleLemonAPI.serializers import MenuItemSerializer
from rest_framework.test import APIClient
from rest_framework import status

class MenuViewTest(TestCase):
    def setUp(self):
        # Skapa testdata i testdatabasen
        MenuItem.objects.create(title='Pasta', price=100, inventory=20)
        MenuItem.objects.create(title='Pizza', price=150, inventory=20)

        # Skapa en testklient
        self.client = APIClient()

    def test_getall(self):
        # Gör en GET-förfrågan till /api/menu/
        response = self.client.get('/api/menu/')

        # Hämta alla objekt från testdatabasen
        menu_items = MenuItem.objects.all()

        # Serialisera objekten
        serialized_data = MenuItemSerializer(menu_items, many=True).data

        # Kontrollera att statuskoden är 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Kontrollera att API-svaret matchar den serialiserade datan
        self.assertEqual(response.data, serialized_data)
