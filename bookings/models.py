from django.db import models

class Booking(models.Model):
    name = models.CharField(max_length=100)         # Guest name
    email = models.EmailField()                     # Guest email
    check_in = models.DateField()
    check_out = models.DateField()
    guests = models.IntegerField(default=1)
    property_name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name} - {self.property_name}"
