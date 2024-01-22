from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

from settings.singleton import SingletonModel

class SocialNet(models.Model):
    SOCIALNET_CHOICES = [
        ("fa-telegram", "Telegram"),
        ("fa-whatsapp", "Whatsapp"),
        ("fa-vk", "VK"),
        ("fa-facebook", "Facebook"),
        ("fa-linkedin-in", "LinkedIn"),
        ("fa-odnoklassniki", "OK"),
        ("fa-google-plus-g", "Google+"),
        ("fa-instagram", "Instagram"),
        ("fa-github", "GitHub"),
        ("fa-twitter", "Twitter/X"),
    ]
    social_net = models.CharField(max_length=17, choices=SOCIALNET_CHOICES, blank=True , verbose_name=_('Social network'))
    title =  models.CharField( blank=True,verbose_name=_('Title'), max_length=256)
    url = models.URLField(verbose_name=_('Website url'), blank=True, max_length=256)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Social network')
        verbose_name_plural = _('Social networks')

class MenuHome(models.Model):
    name = models.CharField(verbose_name=_('Name'),max_length=50, unique=True)
    url = models.CharField(verbose_name=_('Url'), max_length=255)
    active_item = models.BooleanField(verbose_name=_('Active item'), default=True)
    position = models.PositiveIntegerField(verbose_name=_('Position'), default=1)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = _('Menu')
        verbose_name_plural = _('Menu')
        ordering = ('position',)

class SiteSettings(SingletonModel):
    site_url = models.URLField(verbose_name=_('Website url'),blank=True, max_length=256)
    title = models.CharField(verbose_name=_('Title'), max_length=256)
    social_net_link = models.ManyToManyField("SocialNet", blank=True, related_name="sitesettings", verbose_name=_('Social Network'))


    def __str__(self):
        return 'Settings'

    class Meta:
        verbose_name = _('Setting')
        verbose_name_plural = _('Settings')

class ProfessionalSkills(models.Model):
    title = models.CharField(verbose_name=_('Title'), max_length=256)
    position = models.PositiveIntegerField(verbose_name=_('Position'), default=1)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Publication DateTime'))
    deleted = models.BooleanField(default=False, verbose_name=_('Deleted'))

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = _('ProfessionalSkills')
        verbose_name_plural = _('ProfessionalSkills')
        ordering = ('position',)


