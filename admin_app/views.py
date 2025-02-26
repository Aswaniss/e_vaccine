from django.shortcuts import render,redirect
from admin_app.models import*
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.
def add_hotel(request):
    if request.method == 'POST':
        hotel_name=request.POST['hotelName']
        hotel_description=request.POST['hotelDescription']
        booking_price=request.POST['bookingPrice']
        hotel_image=request.FILES['image']
        
        Hotel.objects.create(
            hotelName=hotel_name,
            hotelDescription=hotel_description,
            bookingPrice=booking_price,
            image=hotel_image   
        )
        return redirect("view_hotel")

    
    return render(request,'add_hotel.html')
        
def view_hotel(request):
    data= Hotel.objects.all()
    context={
        'data':data
    }
    return render(request,'viewhotel.html',context)

def hoteldetails(request,h_id):
    data=Hotel.objects.filter(id=h_id)
    context={
        'data':data
    }
    return render(request,'hotel_details.html',context)

def formupdate(request,u_id):
    data =Hotel.objects.filter(id=u_id)
    context={
        'data':data
    }
    if request.method == 'POST':
        hotel_name=request.POST['hotelName']
        hotel_description=request.POST['hotelDescription']
        booking_price = request.POST['bookingPrice']
        try:
            img=request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        
        except MultiValueDictKeyError:
            file = Hotel.objects.get(id=u_id).image
        
        
        Hotel.objects.filter(id=u_id).update(
        hotelName=hotel_name,
        hotelDescription=hotel_description,
        bookingPrice=booking_price,
        image=file
        )
        return redirect("view_hotel")
    
    return render(request,'form_update.html',context)
      
        
    
def show_index(request):
    return render(request, "index.html")
    
        
    
    