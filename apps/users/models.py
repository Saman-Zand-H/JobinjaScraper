from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, 
                                        PermissionsMixin, 
                                        UserManager)


class UserModel(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, 
                                unique=True,
                                db_index=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    email = models.EmailField(blank=True, 
                              null=True, 
                              unique=True)
    
    objects = UserManager()
    
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["first_name", "last_name"]
    
    @property
    def name(self):
        return f"{self.first_name.title()} {self.last_name.title()}"
    
    def __str__(self):
        return f"{self.name} - @{self.username}"
