import re
from django.forms import ValidationError
from django.db import models
from django.utils import timezone


def lnglat_validator(value):
    if not re.match(r'^([+-]?\d+\.?\d*),([+-]?\d+\.?\d*)$', value):
        raise ValidationError('Invalid LngLat Type')


class Post(models.Model):
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published'),
        ('w', 'Withdrawn'),
    )
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, verbose_name='제목',
        help_text='포스팅 제목을 입력해주세요. 최대 100자 내외')
    text = models.TextField(verbose_name='내용')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    tags = models.CharField(max_length=100, blank=True)
    lnglat = models.CharField(max_length=50,
        validators=[lnglat_validator],
        blank=True, help_text='경도/위도 포맷으로 입력')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments', on_delete=models.PROTECT)
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    class Meta:
        ordering = ['-id']

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
