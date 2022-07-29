from django.db import models
from stdimage import StdImageField


class Users(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    active = models.BooleanField()
    price = models.DecimalField(max_digits=5,decimal_places=2)


    photo = StdImageField(
        upload_to = 'photo/%y/%m/%d/', variations={
            'pequeno':(300,300),
            'medio':(500,500),
            'grande':(800,800),
        }
    )

    def __str__(self):
        return self.name
