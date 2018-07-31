from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


# 프로필 클래스
# User와 Profile을 1:1 관계로 설계.
# ForeignKey와의 차이 : 생성되는 필드명은 같으나 유일성의 차이
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # user = models.OneToOneField(User, on_delete=models.CASCADE) # PROTECT, SET_NULL 등
    # user = models.OneToOneField(User)                      # 방법 1 - 비추천
    # user = models.OneToOneField('auth.User')	             # 방법 2 - 비추천
    # user = models.OneToOneField(settings.AUTH_USER_MODEL)  # 방법 3 - 추천
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
