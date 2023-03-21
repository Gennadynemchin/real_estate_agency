from django.contrib import admin
from .models import Flat, Report


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    raw_id_fields = ('liked_by',)
    search_fields = ('owner', 'town', 'address',)
    readonly_fields = ('created_at',)
    list_display = ('address', 'price', 'new_building', 'construction_year', 'town')
    list_editable = ('new_building',)
    list_filter = ('new_building',)


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    raw_id_fields = ('author', 'flat',)
    list_display = ('author', 'flat', 'text')
