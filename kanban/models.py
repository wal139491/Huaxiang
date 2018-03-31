from django.db import models

# Create your models here.
# APP端统计
class App_statistic(models.Model):
    dt = models.DateField()
    city = models.CharField(max_length=20)
    new_count = models.IntegerField()
    active_uconut = models.IntegerField()

# web端统计
class web_statistic(models.Model):
    dt = models.DateField()
    city = models.CharField(max_length=20)
    new_count = models.IntegerField()
    active_uconut = models.IntegerField()


# 核心比率
class core_rate(models.Model):
    dt = models.DateField()
    zhuce_rate = models.DecimalField(max_digits=4,decimal_places=2)
    tiaochu_rate = models.DecimalField(max_digits=4,decimal_places=2)
    average_atime = models.DecimalField(max_digits=4,decimal_places=2)
    average_depth = models.DecimalField(max_digits=5,decimal_places=3) #数据库好像写错了
    shop_cart_cancel = models.DecimalField(max_digits=4,decimal_places=2)

# vip 订单流水和订单数
class vip_order(models.Model):
    dt = models.DateField()
    level1_gmv = models.IntegerField()
    level2_gmv = models.IntegerField()
    level3_gmv = models.IntegerField()
    level4_gmv = models.IntegerField()
    level1_count = models.IntegerField()
    level2_count = models.IntegerField()
    level3_count = models.IntegerField()
    level4_count = models.IntegerField()

# 全局漏斗
class loudou(models.Model):
    dt = models.DateField()
    soushuo = models.IntegerField()
    liulan = models.IntegerField()
    add_shopping_cart = models.IntegerField()
    sub_order = models.IntegerField()
    pay_order = models.IntegerField()
    zhuanhua_total = models.DecimalField(max_digits=4,decimal_places=2)
    zhuanhua1 = models.DecimalField(max_digits=4, decimal_places=2)
    zhuanhua2 = models.DecimalField(max_digits=4, decimal_places=2)
    zhuanhua3 = models.DecimalField(max_digits=4, decimal_places=2)
    zhuanhua4 = models.DecimalField(max_digits=4, decimal_places=2)



# 不同运营位转化
class opreation_zhuanhua(models.Model):
    dt = models.DateField()
    b_liu_zhuan = models.DecimalField(max_digits=4,decimal_places=2)
    b_add_zhuan = models.DecimalField(max_digits=4,decimal_places=2)
    b_order_zhuan = models.DecimalField(max_digits=4,decimal_places=2)
    b_pay_zhuan = models.DecimalField(max_digits=4,decimal_places=2)
    c_liu_zhuan = models.DecimalField(max_digits=4,decimal_places=2)
    c_add_zhuan = models.DecimalField(max_digits=4,decimal_places=2)
    c_order_zhuan = models.DecimalField(max_digits=4,decimal_places=2)
    c_pay_zhuan = models.DecimalField(max_digits=4,decimal_places=2)
    r_liu_zhuan = models.DecimalField(max_digits=4, decimal_places=2)
    r_add_zhuan = models.DecimalField(max_digits=4, decimal_places=2)
    r_order_zhuan = models.DecimalField(max_digits=4, decimal_places=2)
    r_pay_zhuan = models.DecimalField(max_digits=4, decimal_places=2)

# top品类和订单
class top_statistic(models.Model):
    dt = models.DateField()
    top1_category = models.CharField(max_length=20)
    top2_category = models.CharField(max_length=20)
    top3_category = models.CharField(max_length=20)
    top4_category = models.CharField(max_length=20)
    top5_category = models.CharField(max_length=20)
    top6_product = models.CharField(max_length=20)
    top1_rate = models.DecimalField(max_digits=4, decimal_places=2)
    top2_rate = models.DecimalField(max_digits=4, decimal_places=2)
    top3_rate = models.DecimalField(max_digits=4, decimal_places=2)
    top4_rate = models.DecimalField(max_digits=4, decimal_places=2)
    top5_rate = models.DecimalField(max_digits=4, decimal_places=2)
    top6_rate = models.DecimalField(max_digits=4, decimal_places=2)




# 商品浏览来源占比
# 最上方的横幅广告、精选就是可以滑动的那个、推荐是像用户推荐点击的
class shoping_from(models.Model):
    dt = models.DateField() # 这个字段没有 添加到前面
    recommend = models.DecimalField(max_digits=4,decimal_places=2)
    banner = models.DecimalField(max_digits=4,decimal_places=2)
    search = models.DecimalField(max_digits=4, decimal_places=2)
    well_chosen = models.DecimalField(max_digits=4, decimal_places=2)
    other = models.DecimalField(max_digits=4, decimal_places=2)


# 运营位概览
class operation(models.Model):
    dt = models.DateField() # 这个字段没有 添加到前面
    banner_yinyliu = models.DecimalField(max_digits=8,decimal_places=1)
    chosen_yinyliu = models.DecimalField(max_digits=8, decimal_places=1)
    recommend_yinyliu = models.DecimalField(max_digits=8, decimal_places=1)
    banner_forder = models.DecimalField(max_digits=8, decimal_places=1)
    chosen_forder = models.DecimalField(max_digits=8, decimal_places=1)
    recommend_forder = models.DecimalField(max_digits=8, decimal_places=1)
    banner_fgmv = models.DecimalField(max_digits=8, decimal_places=1)
    chosen_fgmv = models.DecimalField(max_digits=8, decimal_places=1)
    recommend_fgmv = models.DecimalField(max_digits=8, decimal_places=1)
    banner_click = models.DecimalField(max_digits=8, decimal_places=1)
    chosen_click = models.DecimalField(max_digits=8, decimal_places=1)
    recommend_click = models.DecimalField(max_digits=8, decimal_places=1)
    banner_fugou = models.DecimalField(max_digits=8, decimal_places=1)
    chosen_fugou = models.DecimalField(max_digits=8, decimal_places=1)
    recommend_fugou = models.DecimalField(max_digits=8, decimal_places=1)


