from django.db import models


# Create your models here.
class Category(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return self.name  # Outputs name when object is converted to string


class Tag(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name  # Outputs name when object is converted to string


class Product(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=20)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)  # 9999999999.99
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="products"
    )
    tag = models.ManyToManyField(Tag, related_name="products")

    def __str__(self):
        return self.name  # Outputs name when object is converted to string
