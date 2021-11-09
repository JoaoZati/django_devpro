
from django.contrib import admin

from classes.models import Class


class RegistrationInLine(admin.TabularInline):
    model = Class.students.through
    extra = 1
    readonly_fields = ('data',)
    autocomplete_fields = ('user',)
    ordering = ('-data',)


@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    inlines = [RegistrationInLine]
    list_display = ('name', 'slug', 'start', 'end')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('-start',)
