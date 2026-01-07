from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Publication(models.Model):
    class Meta:
        verbose_name_plural = 'Publications'
    name = models.CharField(max_length=500, null=True, blank=True)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name
    
    def get_friendly_name(self):
        return self.friendly_name


class Article(models.Model):
    category = models.ForeignKey('category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=500, null=True, blank=True)
    keywords = models.CharField(max_length=500, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(max_length=1024, null=True, blank=True)
    url = models.URLField(max_length=1024, null=True, blank=True)
    published_date = models.CharField(max_length=1024, null=True, blank=True)
    publication = models.ForeignKey('publication', null=True, blank=True, on_delete=models.SET_NULL)
    content = models.CharField(max_length=50000, null=True, blank=True)

    def __str__(self):
        return self.name
