from django.db import models

# Create your models here.(table creation vendiyulla orm queries)

class products(models.Model):

    name = models.CharField(unique=True,max_length=100)
    price = models.PositiveIntegerField()
    description = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    image = models.ImageField(null=True)

    def __str__(self):
        return self.name



