from django import forms
from .models import Profile,Project,Rating

numrate =[(x, x) for x in range(1, 11)]


class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['uploaded_by', 'date',]


class RatingForm(forms.ModelForm):
    class Meta:
        model=Rating
        exclude=['user','project','date','score']
        # widget={'usability': forms.ChoiceField(choices=numrate) , 'design': forms.ChoiceField(choices=numrate) , 'content': forms.ChoiceField(choices=numrate) , 'creativity': forms.ChoiceField(choices=numrate)}


class ProfileForm(forms.ModelForm):
   def __init__(self, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.fields['fullname'].widget=forms.TextInput()
   class Meta:
       model=Profile
       exclude=['username']
