from django.db import models

# Models
class Menu(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()

    class Meta:
        db_table = 'menu'

    def __str__(self):
        return f'{self.title} : {str(self.price)}'


class Booking(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    booking_date = models.DateTimeField()

    class Meta:
        db_table = 'booking'

    def __str__(self):
        return f"Booking by {self.name} on {self.booking_date}"

