from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError('Users must have an username')
        user = self.model(
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    username = models.CharField("이메일", max_length=20, unique=True)
    password = models.CharField("비밀번호", max_length=200)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'username'
    objects = UserManager()
    def __str__(self):
        return self.username
    def has_perm(self, perm, obj=None):
        return True
    def has_module_perms(self, app_label):
        return True
    class meta:
        db_table = 'user'