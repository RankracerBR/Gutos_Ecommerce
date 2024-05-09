from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)  # cents
    file = models.FileField(upload_to="produtos/", blank=True, null=True)
    #url = models.URLField()
    
    def get_display_price(self):
        return "{0:.2f}".format(self.price / 100)
    
    def __str__(self):
        return self.name