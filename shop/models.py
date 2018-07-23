from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(blank=True)
    amount = models.PositiveIntegerField()          #가격
    photo = models.ImageField()
    is_public = models.BooleanField(default=False, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
