from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.(table creation vendiyulla orm queries)

class products(models.Model):

    name = models.CharField(unique=True,max_length=100)
    price = models.PositiveIntegerField()
    description = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    image = models.ImageField(upload_to='image',null=True)

    def __str__(self):
        return self.name
    
    @property                                                              #propery kodukunnath  melete products table alla field + avg rating kittanm 
    def avg_rating(self):
        rate = self.reviews_set.all().values_list('rating',flat = True)    #self.reviews set kodukumbo review akathulla ella fields kittum then value list of kodukumno reviews akathulla rating field kittum
        if rate:
            return sum(rate)/len(rate)                                     # rating undegil aa method call avum
        else:
            return 0
    def review_count(self):
        rate = self.reviews_set.all()
        if rate:
            return rate.count()
        else:
            return 0
class Carts(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(products,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

class Reviews(models.Model):
    product = models.ForeignKey(products,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    command = models.CharField(max_length=200)       #

    def __str__(self):
        return self.command


