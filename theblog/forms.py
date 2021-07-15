from django import forms
from django.db import models
from django.forms import widgets
from .models import Post, Category

choices = Category.objects.all().values_list('name','name')

choice_list = []

for item in choices:
   choice_list.append(item)

class PostForm(forms.ModelForm):
   class Meta:
      model = Post
      fields = ('title', 'title_tag', 'author', 'category', 'body','snippet')
      
      widgets = {
         'title': forms.TextInput(attrs={'class':'form-control'}),
         'title_tag': forms.TextInput(attrs={'class':'form-control'}),
         'author': forms.TextInput(attrs={'class':'form-control','value':'', 'id':'dev','type':'hidden'}),
         # 'author': forms.Select(attrs={'class':'form-control'}),
         'category': forms.Select(choices=choice_list, attrs={'class':'form-control'}),
         'body': forms.Textarea(attrs={'class':'form-control'}),
         'snippet': forms.Textarea(attrs={'class':'form-control'}),
      }
      
      
class EditForm(forms.ModelForm):   # Update form
   class Meta:
      model = Post
      # fields = ('title', 'title_tag', 'auther', 'body')
      fields = ('title', 'title_tag', 'body', 'snippet')
      
      widgets = {
         'title': forms.TextInput(attrs={'class':'form-control'}),
         'title_tag': forms.TextInput(attrs={'class':'form-control'}),
         # 'auther': forms.Select(attrs={'class':'form-control'}),
         'body': forms.Textarea(attrs={'class':'form-control'}),
         'snippet': forms.Textarea(attrs={'class':'form-control'}),
      }