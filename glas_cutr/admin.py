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
class VisionAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'cover_image', 'create_time', 'update_time', 'updated_by', 'is_delete')
    list_filter = ('is_delete', 'updated_by')

admin.site.register(Vision, VisionAdmin)

#Management Team Register
class ManagementAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'create_time', 'update_time', 'updated_by', 'is_delete')
    list_filter = ('is_delete', 'updated_by')

    def description(self, obj):
        return f"{obj.description_prev} {obj.description_bold} {obj.description_next}"


admin.site.register(Management, ManagementAdmin)

class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'role', 'fb_url', 'twt_url', 'lnd_url', 'ins_url', 'profile_img', 'create_time', 'update_time', 'updated_by', 'is_delete']
    list_filter = ['is_delete', 'updated_by','role']
    search_fields = ['name', 'role', 'fb_url', 'twt_url', 'lnd_url', 'ins_url']

admin.site.register(Team, TeamAdmin)

#Service Register
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'create_time', 'update_time', 'updated_by', 'is_delete')
    list_filter = ('is_delete', 'updated_by')

    def description(self, obj):
        return f"{obj.description_prev} {obj.description_bold} {obj.description_next}"

admin.site.register(Service, ServiceAdmin)

class ServiceListAdmin(admin.ModelAdmin):
    list_display = ('service', 'title', 'url', 'icon', 'description', 'create_time', 'update_time', 'updated_by', 'is_delete')
    list_filter = ('is_delete', 'updated_by')

admin.site.register(ServiceList, ServiceListAdmin)

class SubservicesAdmin(admin.ModelAdmin):
    list_display = ('service', 'name', 'create_time', 'update_time', 'updated_by', 'is_delete')
    list_filter = ('is_delete', 'updated_by')

admin.site.register(Subservices, SubservicesAdmin)

#Tool Images Register
class ToolAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon', 'height', 'url', 'create_time', 'update_time', 'updated_by', 'is_delete')
    list_filter = ('is_delete', 'updated_by')

admin.site.register(Tool, ToolAdmin)

#ContactInfo Register
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('number', 'email', 'get_cor_office', 'get_can_office', 'caption', 'fb_url', 'twt_url', 'lnd_url', 'ins_url', 'create_time', 'update_time', 'updated_by', 'is_delete')
    list_filter = ('is_delete', 'updated_by')

    def get_cor_office(self, obj):
        return obj.cor_office
    get_cor_office.short_description = 'Corporate Office'

    def get_can_office(self, obj):
        return obj.can_office
    get_can_office.short_description = 'Canada Office'

admin.site.register(ContactInfo, ContactInfoAdmin)

#User Message Register
class UserMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'message')
    search_fields = ('name', 'email', 'phone', 'message')


admin.site.register(UserMessage, UserMessageAdmin)

