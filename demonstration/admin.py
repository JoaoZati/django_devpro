from django.contrib.admin import ModelAdmin, register

from demonstration.models import Video


@register(Video)
class VideoAdmin(ModelAdmin):
    list_display = ('title', 'slug', 'vimeo_id', 'created_at')
    ordering = ('created_at',)
    prepopulated_fields = {'slug': ('title',)}
