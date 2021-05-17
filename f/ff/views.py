from django.shortcuts import render
from flame import flames
from .models import doc

# Create your views here.
def home(request):
    if request.method=='POST':
        name1=request.POST['fname']
        name2=request.POST['lname']
        result=flames(name1,name2)
        docs=doc(name1=name1,name2=name2,result=result)
        docs.save()
        return render(request, 'resultp.html',{"name1":name1, "name2":name2, "result":result})

    else:
        return render(request,'home.html')