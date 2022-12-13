from django import forms
from django.forms import ModelForm
from .models import NewsStory, Comment, Category

choices = Category.objects.all().values_list('name','name')

choice_list = []

for item in choices:
    choice_list.append(item)


class StoryForm(ModelForm):
    class Meta:
        model = NewsStory
        fields = ['title', 'pub_date', 'content', 'category', 'image_url']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control form-item', 'placeholder': 'Enter a title',}),
            'pub_date': forms.DateTimeInput(format='%Y-%m-%dT%H:%M', attrs={'class':'form-control form-item', 'placeholder':'Select a date','type':'datetime-local'}),
            'content': forms.Textarea(attrs={'class': 'form-control form-item', 'placeholder': 'Enter some text'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control form-item', 'placeholder': 'Select a category'}),
            'image_url': forms.TextInput(attrs={'class': 'form-control form-item', 'placeholder':'Enter a URL'}),
            }

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'body']
        widgets = {
          'name': forms.TextInput(attrs={'placeholder':"Enter your name", 'label':'name', 'class':'form-item',}), 
          'body': forms.Textarea(attrs={'placeholder':"Enter some text", 'label':'body','class':'form-item',}),
        
    }

#form validate method so that future dates can't be selected, show stories for dates in the past