from django.contrib import admin
from .models import*
# Register your models here.
##下方绑定和注册已经同时进行了

from .models import BasicInfo
class BasicInforManger(admin.ModelAdmin):
  list_display=['BookName','Author','Publisher','Theme']##展示的列
  list_display_links=['BookName']##超链接选项
  search_fields=['BookName']##搜索框
admin.site.register(BasicInfo,BasicInforManger)##绑定注册模型管理器类和模型类

from .models import AuthorInfo
class AuthorInfoManager(admin.ModelAdmin):
  list_display=['Author','Country']
  list_filter=['Country']
  search_fields=['Author']
admin.site.register(AuthorInfo,AuthorInfoManager)

from .models import PublisherInfo
class PublisherInfoManager(admin.ModelAdmin):
  list_display=['Publisher']
  search_fields=['Publisher']
admin.site.register(PublisherInfo,PublisherInfoManager)

from .models import ThemeInfo
class ThemeInfoManager(admin.ModelAdmin):
  list_display=['Theme']
  search_fields=['Theme']
admin.site.register(ThemeInfo,ThemeInfoManager)