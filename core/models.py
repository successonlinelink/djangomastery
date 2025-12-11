from django.db import models
from shortuuid.django_fields import ShortUUIDField
from django_ckeditor_5.fields import CKEditor5Field
import shortuuid

STATUS_CHOICE = [
        ('Draft', 'Draft'),
        ('Pending', 'Pending'),
        ('Published', 'Published'),
    ]


class Portfolio(models.Model):
    pid = ShortUUIDField(length=10, max_length=10, prefix="django-mastery", alphabet=shortuuid.get_alphabet())
    title = models.CharField(max_length=200)
    description = CKEditor5Field('Text', config_name='extends')
    

    image = models.ImageField(upload_to="portfolio/", null=True, blank=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICE, default="draft")
    date = models.DateTimeField(auto_now_add=True)

    site_url = models.URLField(max_length=200, blank=True)


    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title
    
class Contact(models.Model):
    cid = ShortUUIDField(length=10, max_length=10, prefix="django-mastery", alphabet=shortuuid.get_alphabet())
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    


