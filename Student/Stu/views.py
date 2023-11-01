from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.

def index(request):
    stu=Student.objects.all()
    
    form_obj=Student_form()
    if request.method=='POST':
        if 'delete' in request.POST:
                key=request.POST.get('delete')
                fo=Student.objects.get(id=key)
                fo.delete()
    context={'stu':stu,'form_obj':form_obj}
                        
    return render(request,'index.html',context)

