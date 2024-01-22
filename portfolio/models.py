from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Portfolio(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    description = models.CharField(max_length=255, verbose_name=_('Description'))
    content = models.TextField(blank=True, verbose_name=_('Content'))
    project_url = models.URLField(verbose_name=_('Project url'), blank=True, max_length=256)
    photo = models.ImageField(upload_to="photo/%Y/%m/%d/", blank=True, verbose_name=_('Photo'))
    slug = models.SlugField(max_length=255, verbose_name=_('Slug'), unique=True)
    best = models.BooleanField(default=False, verbose_name=_('Best'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Publication DateTime'))
    deleted = models.BooleanField(default=False, verbose_name=_('Deleted'))

    def __str__(self):
        return self.title

    def delete(self, *args):
        self.deleted = True
        self.save()

    def get_absolute_url(self):
        return reverse("portfolio:portfolio", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = _('Portfolio')
        verbose_name_plural = _('Portfolio')
        ordering = ["-created_at"]


class Price(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Name'))
    price = models.CharField(max_length=255, verbose_name=_('Price'))
    category = models.ForeignKey("CategoryPrice", blank=True, on_delete=models.PROTECT, related_name="price",
                                 verbose_name=('CategoryPrice'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Price')
        verbose_name_plural = _('Price')
        ordering = ["name"]


class CategoryPrice(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('Title'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ["title"]
