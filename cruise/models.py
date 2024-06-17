from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Cruise(models.Model): 
    cruise_number = models.CharField(max_length=15, unique=True)
    start_date = models.DateField()
    end_date = models.DateField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self): 
        return f"{self.cruise_number} from {self.start_date} to {self.end_date}"

class Item(models.Model): 
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=0)
    description = models.TextField(blank=True, null=True)
    cruise = models.ForeignKey(Cruise, on_delete=models.CASCADE, related_name='items')

    def __str__(self): 
        return f"{self.quantity} x {self.name} for {self.cruise.cruise_number}"
