from django import forms
from .models import Note,Author

class Noteform(forms.ModelForm):
    class Meta:
        model= Note
        fields = '__all__'
        labels ={
            'title' : 'Note Title',
            'txt' : ' Note text',
            'authorname' : 'Author' 
        }


#def __init__(self, *args, **kwargs):
 #   super(Noteform,self).__init__(*args,**kwargs)
   # self.fields['authorname'].empty_label ="select"
    #self.fields['txt'].requierd = False 


class Authorform(forms.ModelForm):
    class Meta:
        model= Author
        fields = '__all__'      
