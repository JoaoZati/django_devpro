from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin

from modules.models import Module, Lesson


@admin.register(Module)
class ModuloAdmin(OrderedModelAdmin):
    list_display = ('title', 'slug', 'public', 'move_up_down_links')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Lesson)
class LessonAdmin(OrderedModelAdmin):
    list_display = ('title', 'module', 'slug', 'move_up_down_links')
    list_filter = ('module',)
    ordering = ('module', 'slug')
    prepopulated_fields = {'slug': ('title',)}
