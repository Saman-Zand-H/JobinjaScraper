from django.contrib import admin

from .models import DemandTechnology


@admin.register(DemandTechnology)
class DemandTechnologyAdmin(admin.ModelAdmin):
    list_display = ["name", "count"]
    ordering = ["-count"]
    search_fields = ["name"]
    