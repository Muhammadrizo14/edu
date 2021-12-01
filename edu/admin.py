from django.contrib import admin
from .models import *


class EduAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'lastname', 'age', 'category', 'days', 'money','teacher','phone')
    list_display_links = ('id', 'name', 'lastname', 'age', 'category', 'days' ,'money', 'teacher','phone')
    search_fields = ('name', 'lastname')
    list_filter = ('category',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


class DaysAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)

class MoneyAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(Edu, EduAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Days, DaysAdmin)
admin.site.register(Money, MoneyAdmin)
admin.site.register(Teacher, TeacherAdmin)
