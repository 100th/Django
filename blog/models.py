import re
from django.forms import ValidationError
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# 위도/경도 유효성 체크 함수 (정규표현식으로)
def lnglat_validator(value):
    if not re.match(r'^([+-]?\d+\.?\d*),([+-]?\d+\.?\d*)$', value):
        raise ValidationError('Invalid LngLat Type')



# Post 클래스
class Post(models.Model):
    STATUS_CHOICES = (          # Status 선택
        ('d', 'Draft'),
        ('p', 'Published'),
        ('w', 'Withdrawn'),
    )
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)     # 글쓴이
                                # settings.AUTH_USER_MODEL로 변경 가능
    title = models.CharField(max_length=100, verbose_name='제목',         # 제목
        help_text='포스팅 제목을 입력해주세요. 최대 100자 내외')
    text = models.TextField(verbose_name='내용')                          # 내용
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)       # Status
    created_date = models.DateTimeField(default=timezone.now)             # 글 쓴 날짜
    # created_date = models.DateTimeField(auto_now_add=True)로 강의에서 씀
    published_date = models.DateTimeField(blank=True, null=True)           # publish 날짜
    # updated_at = models.DateTimeField(auto_now=True)로 강의에서 씀
    tags = models.CharField(max_length=100, blank=True)                    # 태그, Relation없이
    tag_set = models.ManyToManyField('Tag', blank=True)                    # 태그 set, Relation있게
    lnglat = models.CharField(max_length=50,                                # 위도/경도
        validators=[lnglat_validator],
        blank=True, help_text='경도/위도 포맷으로 입력')


    # publish 함수. 날짜는 현재 시간이다.
    def publish(self):
        self.published_date = timezone.now()
        self.save()


    # __str__ 있으면 제목 보이도록 한다는데
    def __str__(self):
        return self.title


    # Comment가 승인되면 보여준다.
    def approved_comments(self):
        return self.comments.filter(approved_comment=True)



# Comment 클래스
class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments', on_delete=models.PROTECT)
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)


    # 이중 클래스
    class Meta:
        ordering = ['-id']  # 번호 역순으로 정렬


    # Comment가 승인됐는지
    def approve(self):
        self.approved_comment = True
        self.save()


    # 내용 보여준다
    def __str__(self):
        return self.text



# Tag 클래스. Relation있게
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    # 태그에서 자기 자신 보이도록 설정
    def __str__(self):
        return self.name



# 프로필 클래스
# User와 Profile을 1:1 관계로 설계.
# ForeignKey와의 차이 : 생성되는 필드명은 같으나 유일성의 차이
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # PROTECT, SET_NULL 등
    # user = models.OneToOneField(User)                      # 방법 1 - 비추천
    # user = models.OneToOneField('auth.User')	             # 방법 2 - 비추천
    # user = models.OneToOneField(settings.AUTH_USER_MODEL)  # 방법 3 - 추천
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
