# Register your models here.


from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.models import Profile, AboutMe, MyPortfolio, DetailPort, ContactMe, SecondResume, LangImage


# Register your models here.


@admin.register(Profile)
class PostAdmin(ModelAdmin):
    list_display = ('name', 'job')
    exclude = ()


@admin.register(AboutMe)
class PostAdmin(ModelAdmin):
    list_display = ('firstname', 'lastname', 'email', 'phone')
    exclude = ()


@admin.register(MyPortfolio)
class PostAdmin(ModelAdmin):
    list_display = ('project_name',)
    exclude = ()


@admin.register(DetailPort)
class PostAdmin(ModelAdmin):
    list_display = ('project', 'worked_lang', 'project_url')
    exclude = ()


@admin.register(ContactMe)
class PostAdmin(ModelAdmin):
    list_display = ('desc_title', 'email', 'phone')
    exclude = ()


@admin.register(LangImage)
class PostAdmin(ModelAdmin):
    list_display = ['image_lang']
    exclude = ()
