from django.db import models
from django.db import models


# class Medicine(models.Model):
#     name = models.CharField(max_length=50)
#     manufacturer = models.CharField(max_length=50)
#     price_per_tab = models.IntegerField()
#
#     def __str__(self):
#         return self.name


class IntakeEntry(models.Model):
    intake_time = models.CharField(max_length=50)
    medicine_name = models.CharField(max_length=50)

    def __str__(self):
        return self.intake_time
