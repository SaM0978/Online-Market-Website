from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=225)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=225)
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField()
    image = models.FileField(upload_to='item-images', null=True, blank=True)
    is_sold = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name