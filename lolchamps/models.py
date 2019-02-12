from django.db import models

class Champs(models.Model):
    champ_name = models.CharField(max_length=100)
    champ_image = models.ImageField(upload_to=content_path)


