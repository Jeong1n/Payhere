from django.db import models
from user.models import User

class accountbook(models.Model):
    user = models.ForeignKey(User, related_name="article_user",on_delete=models.CASCADE)
    amount = models.CharField(max_length=100)
    memo = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
