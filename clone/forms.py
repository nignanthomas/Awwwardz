# from django import forms
# from .models import Post,Comment,Profile
# from .models import *
#
#
# class NewPostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         exclude = ['upload_by', 'pub_date','likes']
#
#
# # class ProfileForm(forms.ModelForm):
# #     class Meta:
# #         model=Profile
# #         exclude=['username']
#
# class CommentForm(forms.ModelForm):
#     class Meta:
#         model=Comment
#         exclude=['username','post']
#
# class ProfileForm(forms.ModelForm):
#    def __init__(self, *args, **kwargs):
#        super().__init__(*args, **kwargs)
#        self.fields['fullname'].widget=forms.TextInput()
#    class Meta:
#        model=Profile
#        exclude=['username']
