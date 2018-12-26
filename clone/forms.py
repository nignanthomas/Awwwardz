from django import forms
from .models import Profile,Project,Rating


class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['uploaded_by', 'date',]


class RatingForm(forms.ModelForm):
    class Meta:
        model=Rating
        exclude=['user','project','date','score']

class ProfileForm(forms.ModelForm):
   def __init__(self, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.fields['fullname'].widget=forms.TextInput()
   class Meta:
       model=Profile
       exclude=['username']
