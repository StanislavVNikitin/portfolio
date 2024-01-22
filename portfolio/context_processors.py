from settings.models import SiteSettings
from settings.models import MenuHome

def load_settings(request):
    return {'site_settings': SiteSettings.load(), 'menu_items': MenuHome.objects.filter(active_item=True).order_by('position')}
