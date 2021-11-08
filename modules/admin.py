from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin

from modules.models import Module


@admin.register(Module)
class ModuloAdmin(OrderedModelAdmin):
    list_display = ('title', 'slug', 'public', 'move_up_down_links')
    prepopulated_fields = {'slug': ('title',)}
