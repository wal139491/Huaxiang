from django.db import models

# Create your models here.
# 类名是表名 其他是字段 数据库名在setting里面设置过了
class Admin_user(models.Model):
    uname = models.CharField(max_length=50) # label='用户名'
    ename = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    dept = models.CharField(max_length=50)
    position = models.CharField(max_length=50)


class apply_auth(models.Model):
    id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=50)
    dept = models.CharField(max_length=50)
    admin_name = models.CharField(max_length=50)
    apply_theme = models.CharField(max_length=50)
    apply_gongneng = models.CharField(max_length=50)
    apply_reason = models.CharField(max_length=255)
    create_time = models.DateTimeField()
    auth_time = models.DateTimeField()
    is_operate = models.IntegerField()

class auth_base(models.Model):
    user_id = models.IntegerField()
    auth1 = models.IntegerField()
    auth2 = models.IntegerField()
    auth3 = models.IntegerField()
    auth4 = models.IntegerField()
    auth5 = models.IntegerField()
    auth6 = models.IntegerField()
    auth7 = models.IntegerField()
    auth8 = models.IntegerField()
