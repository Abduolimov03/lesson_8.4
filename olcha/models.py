
from django.db import models
from decimal import Decimal

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=120)
    image = models.ImageField(upload_to='category/images/')
    slug = models.SlugField(unique=True)


    parent = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        related_name='children',
        null = True,
        blank=True
    )

    def __str__(self):
        if self.parent:
            return f"{self.parent.title} => {self.title}"
        return self.title

    class Meta:
        verbose_name_plural = 'categories'


class Product(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=1)
    discount = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category,
                                 on_delete=models.SET_NULL,
                                 null=True,
                                 blank=True,
                                 related_name='products')

    @property
    def discounted_price(self):
        if self.discount:
            return self.price * Decimal(1 - self.discount / 100)
        return self.price

    def __str__(self):
        return self.name



class Image(models.Model):
    image = models.ImageField(upload_to='product/images/')
    product = models.ForeignKey(Product,
                                on_delete=models.SET_NULL,
                                related_name='images',
                                null=True,
                                blank=True
                                )
    is_primary = models.BooleanField(default=False)

    def __str__(self):
        return self.product.name
