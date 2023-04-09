from django.contrib import admin
from .models import Flat, Report, Owner


class FlatInline(admin.TabularInline):
    model = Owner.flats.through
    raw_id_fields = ("name", "flat",)


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    raw_id_fields = ("liked_by",)
    search_fields = (
        "town",
        "address",
    )
    readonly_fields = ("created_at",)
    list_display = (
        "address",
        "price",
        "new_building",
        "construction_year",
        "town",
    )
    list_editable = (
        "new_building",
    )
    list_filter = ("new_building",)
    inlines = [
        FlatInline,
    ]


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    raw_id_fields = (
        "author",
        "flat",
    )
    list_display = ("author", "flat", "text")


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ("flats",)
    search_fields = (
        "name",
    )
    list_display = (
        "name",
        "phonenumber",
        "pure_phone",
    )
    inlines = [
        FlatInline,
    ]



