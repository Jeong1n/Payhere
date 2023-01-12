from rest_framework import serializers
from .models import accountbook

class accountbookSerializer(serializers.ModelSerializer):
    class Meta:
        model = accountbook
        fields = "__all__"
