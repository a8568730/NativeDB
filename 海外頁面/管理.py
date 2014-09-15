from django.contrib import admin
from 海外頁面.模型 import 語言表
from 海外頁面.模型 import 類型表
from 海外頁面.模型 import 原始語料表
from 海外頁面.模型 import 原始檔案表
from 海外頁面.模型 import 轉好的表

admin.site.register(語言表)
admin.site.register(類型表)
admin.site.register(原始語料表)
admin.site.register(原始檔案表)
admin.site.register(轉好的表)