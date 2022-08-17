from tabnanny import verbose
from django.db import models

# Create your models here.
class BasicInfo(models.Model):##图书基本信息
    BookName=models.CharField(verbose_name='书名',max_length=30,unique=True)
    Author=models.ForeignKey('AuthorInfo',verbose_name='作者',on_delete=models.CASCADE)##外键 作者
    Publisher=models.OneToOneField('PublisherInfo',verbose_name='出版社',on_delete=models.CASCADE)##外键 出版社
    Theme=models.ForeignKey('ThemeInfo',verbose_name='主题/题材',on_delete=models.CASCADE)##外键 主题/题材
    Reading=models.CharField(verbose_name='阅读情况',max_length=10,default='未读')
    Price=models.DecimalField(verbose_name='购入价格',max_digits=5,decimal_places=2,default='721')
    class Meta:
        db_table='图书基本信息'
        verbose_name_plural='图书基本信息'
   
   
class AuthorInfo(models.Model):##作者信息
    Author=models.CharField(verbose_name='作者',max_length=10)
    Country=models.CharField(verbose_name='国家',max_length=10)
    class Meta:
        db_table='作者信息'
        verbose_name_plural='作者信息'
    def __str__(self) :
        return "%s"%(self.Author)


class PublisherInfo(models.Model):##出版社信息
    Publisher=models.CharField(verbose_name='出版社',max_length=10)
    class Meta:
      db_table='出版社信息'
      verbose_name_plural='出版社信息'
    def __str__(self) :
        return "%s"%(self.Publisher)


class ThemeInfo(models.Model):##主题/题材信息
    Theme=models.CharField(verbose_name='主题/题材',max_length=10)
    class Meta:
      db_table='主题/题材信息'
      verbose_name_plural='主题/题材信息'
    def __str__(self) :
        return "%s"%(self.Theme)  
     ##Links