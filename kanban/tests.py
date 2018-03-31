from django.test import TestCase

# Create your tests here.
#-*-coding:utf-8-*-
from django.http import HttpResponse
from .models import App_statistic

# 增删改查数据，先创建对象
def testdb(requests):
    test1 = App_statistic(uname='赖伟',ename='Stefan',email='laiwei@aurao.com',password='wal139491007')
    test1.save()
    return HttpResponse('<p>添加用户成功</p>')

def query():
    response = ""
    app_sta = App_statistic.objects.All().values()  # 为什么加values,因为之前返回的是对象，values返回字典
    city = App_statistic.objects.all().distinct('city').values()  # filter用来过滤条件，支持in like 多用filter吧
    app_date = App_statistic.objects.all().distinct('dt').values()
    # app_static = App_statistic.objects.filter().values(''city','new_count')
    app_new = App_statistic.objects.filter().values('city', 'new_count')
    app_active = App_statistic.objects.filter().values('city', 'active_uconut')
    data = city+app_date+app_new+app_active

    #models.UserInfo.objects.all().values('user')    #只取user列
    #models.UserInfo.objects.all().values_list('id','user') # 取id和user 生成一个列表
    #response2 = App_statistic.objects.get(id=1) # get是用来获取对象
    #response3 = App_statistic.objects.filter(id=1).order_by("uname")[0:2]


    # return HttpResponse('<p>'+response+'</p>') # 应该能返回一个list或dict 供前台显示

def update(request):
    App_statistic.objects.filter(id=1).update(uname="zhouxing")
    return HttpResponse('<p>更新成功</p>')
    # App_statistic.objects.all().update()

def delete(request):
    App_statistic.objects.filter(id=1).delete()
    return HttpResponse('<p>删除成功</p>')

class App(TestCase):
    #def setUp(self):
        #App_statistic.objects.create(name="lion", sound="roar")
        #App_statistic.objects.create(name="cat", sound="meow")

    def test_query(self):
        app_active = App_statistic.objects.filter().values('city', 'active_uconut')
        print(type(app_active))

    def test_speak(self):
        print(1)
