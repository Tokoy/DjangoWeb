from django.contrib import admin
from hello import models
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','pub_date','update_time',)

admin.site.register(models.Article)
admin.site.register(models.Person)