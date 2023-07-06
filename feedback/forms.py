from django.forms import ModelForm, TextInput,DateTimeInput,Textarea
from django import forms
from .models import Feedback

class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ['title','author', 'mail', 'description']


        widgets={
            "title":TextInput(attrs={
                              'class':"form-control",
                               'placeholder':'Тема'
                              }),
            "author": TextInput(attrs={
                'class': "form-control2",
                'placeholder': 'Автор'

            }),

            "mail": TextInput(attrs={
                'class': "form-control2",
                'placeholder': 'e-mail'

            }),
            "description": Textarea(attrs={
                'class': "form-control",
                'placeholder': 'Текст сообщения',
                'rows':5
            })
        }

# class Feedform(ModelForm):
#     class Meta:
#         model = Feedback
#         fields = ['title', 'memo', 'important']
#

# class Newfeed(forms.Form):
#     title = forms.CharField(max_length=255,widget=forms.TextInput(attrs={'class':'title_feed'}))
#     author = forms.CharField(max_length=255,widget=forms.TextInput(attrs={'class':'author_feed'}))
#     description = forms.CharField(widget=forms.Textarea(attrs={'class':'author_feed'}))
#     alles=forms.BooleanField(widget=forms.BooleanField(attrs={'class':'alles_feed'}))