from django.db import models
# Create your models here.
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.

class Client(models.Model):
    owner= models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=240)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=300)
    email = models.EmailField(max_length=240)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('crm:detail-client', kwargs={'pk': self.pk})
