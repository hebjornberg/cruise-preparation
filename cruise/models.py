from django.db import models

# Create your models here.
class Cruise(models.Model): 
    cruise_number = models.CharField(max_length=15, unique=True)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self): 
        return f"Cruise {self.cruise_number} from {self.start_date} to {self.end_date}"
