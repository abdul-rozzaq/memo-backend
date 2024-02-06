from django.contrib import admin

# Register your models here.
from .models import (
    Theme,
    Word
)


class WordAdmin(admin.ModelAdmin):
    list_display = ['uzbek', 'korean']
    list_filter = ['theme']


admin.site.register(Theme)
admin.site.register(Word, WordAdmin)
