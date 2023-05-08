from django.contrib import admin
from .models import *


#Logo Register
class LogoAdmin(admin.ModelAdmin):
    list_display = ['logo_dark_url', 'logo_light_url', 'create_time', 'update_time', 'updated_by', 'is_delete']
    list_filter = ['is_delete', 'updated_by']
    
    def logo_dark_url(self, obj):
        return obj.logo_dark.url
    logo_dark_url.short_description = 'Logo Dark URL'
    
    def logo_light_url(self, obj):
        return obj.logo_light.url
    logo_light_url.short_description = 'Logo Light URL'

admin.site.register(Logo, LogoAdmin)


#Navigation Register
class NavigationAdmin(admin.ModelAdmin):
    list_display = ['name', 'url', 'create_time', 'update_time', 'updated_by', 'is_delete']
    list_filter = ['is_delete', 'updated_by']

admin.site.register(Navigation, NavigationAdmin)


#Subnavigation Register
class SubNavigationAdmin(admin.ModelAdmin):
    list_display = ['navigation_name', 'name', 'url', 'create_time', 'update_time', 'updated_by', 'is_delete']
    list_filter = ['navigation__name', 'is_delete', 'updated_by']

    def navigation_name(self, obj):
        return obj.navigation.name
    navigation_name.short_description = 'Navigation Name'

admin.site.register(SubNavigation, SubNavigationAdmin)


#HomeCap Register
class HomeCapAdmin(admin.ModelAdmin):
    list_display = ['title', 'button_url', 'button_name', 'cover_image', 'create_time', 'update_time', 'updated_by', 'is_delete']
    list_filter = ['is_delete', 'updated_by']

    def title(self, obj):
        return f'{obj.title_up} {obj.title_down}'

    title.short_description = 'Title'

admin.site.register(HomeCap, HomeCapAdmin)


#About Us Register
class AboutUSAdmin(admin.ModelAdmin):
    list_display = ['title', 'button_url', 'button_name', 'cover_image', 'create_time', 'update_time', 'updated_by', 'is_delete']
    list_filter = ['is_delete', 'updated_by']

    def title(self, obj):
        return f'{obj.title} {obj.description_bold}'

    title.short_description = 'Title'


admin.site.register(AboutUS, AboutUSAdmin)


#Mission Register
class MissionAdmin(admin.ModelAdmin):
    list_display = ('title', 'cover_image', 'create_time', 'update_time', 'updated_by', 'is_delete')
    list_filter = ('is_delete', 'updated_by')
    
    def title(self, obj):
        return f'{obj.title} {obj.description_bold}'

    title.short_description = 'Title'
    
admin.site.register(Mission, MissionAdmin)

class MissionListAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'create_time', 'update_time', 'updated_by', 'is_delete')
    list_filter = ('mission__title','is_delete', 'updated_by')
    
    def title(self, obj):
        return obj.mission.title + " - " + obj.mission.description_bold
    
    title.short_description = 'Title'

admin.site.register(MissionList, MissionListAdmin)


#Vision Register
admin.site.register(Vision)
admin.site.register(Management)
admin.site.register(Team)
admin.site.register(Service)
admin.site.register(ServiceList)
admin.site.register(Subservices)
admin.site.register(Tool)
admin.site.register(ContactInfo)
admin.site.register(UserMessage)

