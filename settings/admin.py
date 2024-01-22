from django.contrib import admin
from django.utils.translation import gettext_lazy as _


# Register your models here.
from django.db.utils import ProgrammingError
from settings.models import SiteSettings, SocialNet, MenuHome, ProfessionalSkills


class SiteSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('Main page options'), {
            'fields': ('title', 'site_url',)
        }),
        (_('Social Network'), {
            'fields': ('social_net_link',),
        }),
    )

    # Create a default object on the first page of SiteSettingsAdmin with a list of settings
    def __init__(self, model, admin_site):
        super().__init__(model, admin_site)
        # be sure to wrap the loading and saving SiteSettings in a try catch,
        # so that you can create database migrations
        try:
            SiteSettings.load().save()
        except ProgrammingError:
            pass

    # prohibit adding new settings
    def has_add_permission(self, request, obj=None):
        return False

    # as well as deleting existing
    def has_delete_permission(self, request, obj=None):
        return False


class SocialNetAdmin(admin.ModelAdmin):
    prepopulated_fields = {"title": ("social_net",)}
    fields = ("title",'social_net','url')
    list_display = ("id", "title")
    list_display_links = ("id", "title")

class MenuHomeAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    save_as = True
    save_on_top = True


class ProfessionalSkillsAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    save_as = True
    save_on_top = True


admin.site.register(SiteSettings, SiteSettingsAdmin)
admin.site.register(SocialNet, SocialNetAdmin)
admin.site.register(MenuHome, MenuHomeAdmin)
admin.site.register(ProfessionalSkills, ProfessionalSkillsAdmin)