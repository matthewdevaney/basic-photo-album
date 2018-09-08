from django.db import models


class Images(models.Model):
    img = models.ImageField(upload_to='upload/')

