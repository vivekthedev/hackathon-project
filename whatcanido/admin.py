from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Data)
class DataAdmin(admin.ModelAdmin):
    prepopulated_fields = {'name_slug':('name',)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'category_slug':('title',)}