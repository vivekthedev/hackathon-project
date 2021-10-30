from django.db import models
from django.urls import reverse 
from django.template.defaultfilters import slugify

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=250)
    category_slug = models.SlugField()

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title
    


class Data(models.Model):
    name = models.TextField(max_length=250)
    name_slug = models.SlugField(max_length=250)
    in_review = models.BooleanField(default=True)
    solution = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE, related_name='category')

    class Meta:
        verbose_name_plural = 'Data'

    def __str__(self):
        return self.name[:50]
    
    def save(self, *args, **kwargs):
        s = slugify(self.name)
        self.name_slug = s[:50]
        super(Data, self).save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('whatcanido:problempage', args=(self.name_slug,))

