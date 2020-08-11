from django.shortcuts import render
from testapp.models import Student

# Create your views here.

def home_page_view(request):
    #students=Student.objects.all()
    #students=Student.objects.filter(marks__lt=35)
    #students=Student.objects.filter(name__startswith='A')
    #students=Student.objects.all().order_by('marks') # Ascending order
    students=Student.objects.all().order_by('-marks') # descending order
    return render(request,'testapp/index.html',{'students':students})