from django.db import models

# Create your models here.
class User(models.Model):
    
    user_email = models.EmailField(unique=True) # 이메일을 받는데 이게 ID임
    user_password = models.CharField(max_length=128)  # 암호화된 비밀번호 저장
    user_name = models.CharField(max_length=50) 
    user_birthdate = models.DateField()
    user_phone = models.CharField(max_length=20)
    user_address = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    profile_image = models.ImageField(
    upload_to='profile_images/',
    default='profile_images/default.png',
    blank=True
)
    
    class Meta:
        db_table = 'user'
        verbose_name = 'User'

    def __str__(self):
        return self.user_name