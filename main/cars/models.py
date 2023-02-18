from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    category = models.CharField(max_length=24, default='standard', unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category


class Car(models.Model):
    choices_engine = [
        ('diesla', 'diesla'),
        ('gas', 'gas'),
        ('petrol', 'petrol'),
    ]
    id = models.AutoField(primary_key=True)
    brand = models.CharField(max_length=50)
    number = models.IntegerField(default="")
    engine = models.CharField(choices=choices_engine, default="", max_length=10)
    year = models.PositiveSmallIntegerField(help_text="production date")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(max_length=512, blank=True)
    image = models.ImageField(upload_to='cars/', blank=True)
    is_available = models.BooleanField(default=True)
    capacity = models.CharField(max_length=2, default='')
    rent = models.CharField(max_length=3, default='')

    def __str__(self):
        return f'{self.brand}, {self.number}'


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, max_length=32, null=True, on_delete=models.SET_NULL)
    brand = models.ForeignKey(Car, max_length=32, blank=False, default='', on_delete=models.CASCADE)
    start_date = models.CharField(max_length=32, blank=False)
    end_date = models.CharField(max_length=32, blank=False)

    def __str__(self):
        return f'{self.order_id}, {self.brand}' + " : " + str(self.user)



