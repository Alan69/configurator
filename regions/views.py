from django.shortcuts import render, redirect  
from .forms import RegionForm  
from .models import Region, Urls, City
from django.http import HttpResponse
import re
from django.utils.html import strip_tags
# Create your views here.  
def emp(request):  
    if request.method == "POST":  
        form = RegionForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = RegionForm()  
    return render(request,'regions/index.html',{'form':form})  
    
def show(request):  
    city = City.objects.get(city_name=request.user.region)
    regions = Region.objects.filter(belong_city=city)
    url_obj = Urls.objects.all()
    return render(request,"regions/show.html",{'regions':regions, 'url_obj':url_obj}) 

def edit(request, id):  
    # urls = Urls.objects.all()
    # return render(request,'regions/edit.html', {'regions':regions, 'urls': urls})  

    try:
        regions = Region.objects.get(id=id)
        error = ''
        if request.method == 'POST':
            region_form = RegionForm(request.POST, instance=regions)
            if region_form.is_valid():
                region_form.save()
                return redirect('/show')
            else:
                error = "Data is not valid"
        else:
           # create and edit form when request is GET
           region_form = RegionForm(instance=regions)

        # add `product_form` in context instead of `product`
        return render(request, 'regions/edit.html', {'region_form':region_form, 'error':error})
    except Region.DoesNotExist:
        return redirect('/')

# def update(request, id):  
#     url_obj = Urls.objects.get(name = regions.url)
#     form = RegionForm(request.POST, instance = regions) 
#     url = request.POST['url'] 
#     url_obj.name = url
#     url_obj.save()
#     return redirect("/show")
    # if form.is_valid():  
    #     form.save()  
    #     return redirect("/show")
    # return render(request, 'regions/edit.html', {'regions': regions})  

def config(request, id):
    regions = Region.objects.filter(id=id)
    # return render(request,'regions/config.html', {'regions':regions}) 

    responce = HttpResponse(content_type='text/plain')
    responce['Content-Disposition'] = 'attachment; filename=config.txt'
    lines = ['connection=wired\n'
    'network_interface=eth0\n'
    'dhcp=yes\n'
    'proxy=\n'
    'browser=chrome\n'
    'browser_user_agent=Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0) USTUDY KIOSK #client_id=50029\n' ]

    for region in regions:
        lines.append(f'homepage={region.url.url}\n')

    lines.append(
        'allow_icmp_protocol=yes\n'
        'primary_keyboard_layout=kz\n'
        'secondary_keyboard_layout=us\n'
        'disable_navigation_bar=yes\n'
        'kiosk_config=http://config.ustudy.kz/shm1/kiosk-config.php?id=$machineid\n'
        'disable_numlock=no\n'
        'timezone=Asia/Almaty\n'
        'wallpaper=http://ustudy.kz/kiosk-bg.jpg\n'
        'wake_on_lan=yes\n'
        'disable_zoom_controls=yes\n'
        'additional_components=uefi.zip 08-ssh.xzm 07-java.xzm 05-flash.xzm 05-flash_legacy.xzm 06-fonts.xzm 002-chrome.xzm\n'
        'screen_settings=DVI-0:disabled\n'
        'disable_private_mode=no\n'
        'removable_devices=no\n'
        "run_command=echo -e "#!/bin/bash\n xmodmap -verbose -e 'keycode 67= Escape'\n xmodmap -verbose -e 'keycode 133='\n xmodmap -verbose -e 'keycode 134='\n xmodmap -verbose -e 'keycode 206='\n xmodmap -verbose -e 'keycode 50='\n xmodmap -verbose -e 'keycode 62='\n xmodmap -verbose -e 'keycode 64='\n xmodmap -verbose -e 'keycode 108=' " > disable_keys.sh; chmod a+x disable_keys.sh; ./disable_keys.sh\n"
    )

    responce.writelines(lines)
    return responce

def destroy(request, id):  
    regions = Region.objects.get(id=id)  
    regions.delete()  
    return redirect("/show")  