from django.apps import AppConfig

class RestaurantConfig(AppConfig):  # Ändra klassen till ett unikt namn
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'restaurant'  # Se till att namnet matchar appens nya mappnamn
