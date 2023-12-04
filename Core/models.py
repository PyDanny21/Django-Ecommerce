from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100)

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")

    def __str__(self):
        return self.name


class Product(models.Model):
    category=models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    description=models.TextField(blank=True,null=True)
    price=models.FloatField()
    image=models.ImageField(upload_to='product_images',blank=True,null=True)
    is_sold=models.BooleanField(default=True)
    created_by=models.ForeignKey(User,related_name='products',on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ("Product")
        verbose_name_plural = ("Products")

    def __str__(self):
        return self.name

class CartItem(models.Model):
    cart=models.ForeignKey(Product, related_name='product', on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=0)
    class Meta:
        verbose_name = ("CartItem")
        verbose_name_plural = ("CartItems")

    def __str__(self):
        return self.cart

    def get_absolute_url(self):
        return reverse("CartItem_detail", kwargs={"pk": self.pk})

class Profile(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username
