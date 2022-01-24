from django.db import models
from django.contrib.auth.models import User

class Users(User):
    avatar = models.ImageField(upload_to='avatar/%Y', max_length=200, null=True)
    phone = models.CharField(max_length=12, null=True)

    def __str__(self):
        return 'user {}'.format(self.username)

        
        