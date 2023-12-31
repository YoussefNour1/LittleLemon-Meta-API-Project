from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.


class Category(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=255, db_index=True)

    def __str__(self):
        return self.title


class MenuItem(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, db_index=True)
    featured = models.BooleanField(db_index=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return self.title


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        unique_together = ('user', 'menu_item')


class Order(models.Model):
    delivery_crew = models.ForeignKey(User, related_name='delivery_crew', on_delete=models.PROTECT, null=True)
    status = models.BooleanField(db_index=True, default=False)
    total = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    date = models.DateField(db_index=True, default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        unique_together = ('order', 'menu_item')
