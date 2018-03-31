from django.db import models

# Create your models here.
# 类名是表名 其他是字段 数据库名在setting里面设置过了
class Admin_user(models.Model):
    uname = models.CharField(max_length=50) # label='用户名'
    ename = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)

