from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

from portfolio.models import Portfolio, Price, CategoryPrice


# Register your models here.

class PortfolioAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    save_as = True
    save_on_top = True
    list_display = ("id", "title", "created_at", "get_photo", "deleted")
    list_display_links = ("id", "title")
    search_fields = ("title",)
    fields = (
        'title', 'slug', 'description', 'content', 'project_url', 'best', 'get_photo', 'photo', 'created_at', 'deleted')
    readonly_fields = ('created_at', 'get_photo',)

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50">')
        return "-"

    get_photo.short_description = "Фото"


class PriceAdmin(admin.ModelAdmin):
    list_display = ("id", "category", "name")
    fields = ("category", "name", "price")


class CategoryPriceAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    fields = ("title",)


admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Price, PriceAdmin)
admin.site.register(CategoryPrice, CategoryPriceAdmin)
