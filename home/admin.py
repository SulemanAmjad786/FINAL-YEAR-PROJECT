from django.contrib import admin
from .models import Head
from .models import About
from .models import Blog
from django.utils.html import format_html
# Register your models here.


class AboutAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(object.about_image.url))
    list_display = ('id', 'title', 'thumbnail', 'about_title', 'about_description',
                    'market_captilization', 'daily_transaction', 'active_accounts', 'years')
    list_display_links = ('id', 'title', 'thumbnail', 'years')
    search_fields = ('id', 'about_description')


admin.site.register(Head)
admin.site.register(About, AboutAdmin)
admin.site.register(Blog)
