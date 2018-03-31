#-*-coding:utf-8-*-
from django.http import HttpResponse
from .models import Admin_user

# 增删改查数据，先创建对象
def testdb(requests):
    test1 = Admin_user(uname='赖伟',ename='Stefan',email='laiwei@aurao.com',password='wal139491007')
    test1.save()
    return HttpResponse('<p>添加用户成功</p>')

def query(request):
    response = ""
    list = Admin_user.objects.all() #select *
    response1 = Admin_user.objects.filter(id=1) # filter用来过滤条件，支持in like 多用filter吧
    response2 = Admin_user.objects.get(id=1) # get是用来获取对象
    response3 = Admin_user.objects.filter(id=1).order_by("uname")[0:2]

    for data in response3:
        response += data

    return HttpResponse('<p>'+response+'</p>') # 应该能返回一个list或dict 供前台显示

def update(request):
    Admin_user.objects.filter(id=1).update(uname="zhouxing")
    return HttpResponse('<p>更新成功</p>')
    # Admin_user.objects.all().update()

def delete(request):
    Admin_user.objects.filter(id=1).delete()
    return HttpResponse('<p>删除成功</p>')

if __name__ == '__main__':
    print(1)