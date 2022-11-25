from django.db import models


class IntakeEntry(models.Model):
    intake_time = models.CharField(max_length=50)
    medicine_name = models.CharField(max_length=50)

    def __str__(self):
        return self.intake_time
