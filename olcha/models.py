from tkinter.tix import IMAGE

from django.db import models
from django.utils.text import slugify


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
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="product/images/")
    desc = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


    def __str__(self):
        return self.title

