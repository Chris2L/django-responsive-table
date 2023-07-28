from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _

# Create your models here.

class Author(models.Model):

    name = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    country = models.CharField(max_length=150)
    email = models.EmailField(max_length=254, blank=True)
    still_alive = models.BooleanField()    

    class Meta:
        verbose_name = _("author")
        verbose_name_plural = _("authors")

    def __str__(self):
        return self.name + " " + self.lastname

    def get_absolute_url(self):
        return reverse("author_detail", kwargs={"pk": self.pk})
