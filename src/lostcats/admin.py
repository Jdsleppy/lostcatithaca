from django.contrib import admin

from .models import LostCat


class LostCatAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(LostCat, LostCatAdmin)
