from django.shortcuts import render , redirect

from .forms import Noteform , Authorform
from .models import Note

# Create your views here.

def note_form(request):
    if request.method =="GET":
     form = Noteform()
     aform =Authorform() 
     return render(request,"note_register/form.html", {'form' : form ,'aform':aform } )
    else : 
      form = Noteform(request.POST)
      if form.is_valid():
        form.save()
      return  redirect('/note/list') 

def note_list(request):
    context = { 'list' : Note.objects.all() } 
    return render(request,"note_register/list.html",context)

def note_del(request,id):
    note =Note.objects.get(pk=id)
    note.delete()
    return redirect('/note/list') 

def note_search(request):
  if request.method=="POST" :
    id  =request.POST['id'] 
    context = {'note' : Note.objects.get(pk=id) }
    return render(request,"note_register/search.html",context)
  else :
     return render(request,"note_register/search.html")
      

   
        