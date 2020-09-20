from django.contrib import admin
from .models import Code
# Register your models here.

# admin.site.register(Code)

@admin.register(Code)
class CodeAdmin(admin.ModelAdmin):
    class Media:
        js = ('tiny.js',)