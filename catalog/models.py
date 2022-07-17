from distutils.command.upload import upload
from statistics import mode
from tabnanny import verbose
from django.db import models
from django.urls import reverse

# Create your models here.


class Catalog(models.Model):

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/')
    is_published = models.BooleanField(default=True)

    categ = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Наш каталог"

    def get_abslute_url(self):
        return reverse ('category', kwargs = {'categ_id': self.pk})


class Category(models.Model):

    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_abslute_url(self):
        return reverse ('category', kwargs = {'categ_id': self.pk})