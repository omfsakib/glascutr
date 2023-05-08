from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages

# Create your views here.
def home(request):
    #Home Caption & Cover
    home_obj = HomeCap.objects.first()
    
    #About US
    about_obj = AboutUS.objects.first()
    
    #Mission
    mission_obj = Mission.objects.first()
    sub_mission_obj = MissionList.objects.filter(is_delete=False).order_by('create_time')
    
    #Vision
    vision_obj = Vision.objects.first()
    
    #Management
    management_obj = Management.objects.first()
    team_obj = Team.objects.filter(is_delete = False).order_by('create_time')
    
    #Service
    service_obj = Service.objects.first()
    service_list_obj = ServiceList.objects.filter(is_delete = False).order_by('create_time')
    service_list = []
    for service_item in service_list_obj:
        has_sub = False
        if ServiceList.has_subservice(service_item):
            has_sub = True
            sub_objs = ServiceList.get_subservice(service_item)
        else:
            sub_objs = []
            
        print(sub_objs)
        
        item = {
            'name':service_item.title,
            'url' :service_item.url,
            'description': service_item.description,
            'icon': service_item.icon.url,
            'has_sub':has_sub,
            'subservice':sub_objs,
        }
        service_list.append(item)
        
    
    #Tools Image
    tools_obj = Tool.objects.filter(is_delete = False).order_by('create_time')
    
    #Contact Info
    contact_info_obj = ContactInfo.objects.first()
    
    #User Message
    if request.method == "POST" and 'message' in request.POST:
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        
        message_obj = UserMessage.objects.create(name=name, email=email, phone=phone, message=message)
        messages.success(request,'We received your message. Wait for our team to contact!')
        return redirect('home')
        
        
    context = {
        'homecap':home_obj,
        'about':about_obj,
        'mission':mission_obj,
        'submission':sub_mission_obj,
        'vision':vision_obj,
        'management':management_obj,
        'team':team_obj,
        'service':service_obj,
        'service_list':service_list,
        'tools':tools_obj,
        'contact':contact_info_obj,
    }
    return render(request, 'pages/home.html', context)