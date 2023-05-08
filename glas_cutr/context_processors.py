from . models import *
from . views import *

#Custom Context processors
def add_to_context(request):
    #Adding logo to context
    logo_obj = Logo.objects.first()
    
    #Adding Navigation to context
    nav_obj = Navigation.objects.filter(is_delete=False).order_by('create_time')
    nav = []
    for nav_item in nav_obj:
        has_sub = False
        if Navigation.has_subnavigation(nav_item):
            has_sub = True
            subnav_objs = Navigation.get_subnavigation(nav_item)
        else:
            subnav_objs = []
        
        item = {
            'name':nav_item.name,
            'url' :nav_item.url,
            'has_sub':has_sub,
            'subnav':subnav_objs,
        }
        nav.append(item)
    
    
    context = {
        'logo':logo_obj,
        'nav':nav,
    }
    return context
    