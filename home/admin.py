from django.contrib import admin
from .models import Text, Image

# Register your models here.
@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'photo']

@admin.register(Text)
class TextAdmin(admin.ModelAdmin):
    list_display = ['id', 'text']