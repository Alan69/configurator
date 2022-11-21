from django.shortcuts import render, redirect  
from .forms import RegionForm  
from .models import Region, Urls
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
    regions = Region.objects.filter(name=request.user.region)
    url_obj = Urls.objects.all()
    return render(request,"regions/show.html",{'regions':regions, 'url_obj':url_obj}) 

def edit(request, id):  
    regions = Region.objects.get(id=id)  
    return render(request,'regions/edit.html', {'regions':regions})  

def update(request, id):  
    regions = Region.objects.get(id=id)  
    url_obj = Urls.objects.get(name = regions.url)
    form = RegionForm(request.POST, instance = regions) 
    # url = request.POST['url'] 
    # url_obj.name = url
    # url_obj.save()
    # return redirect("/show")
    if form.is_valid():  
        form.save()  
        return redirect("/show")
    return render(request, 'regions/edit.html', {'regions': regions})  

def destroy(request, id):  
    regions = Region.objects.get(id=id)  
    regions.delete()  
    return redirect("/show")  