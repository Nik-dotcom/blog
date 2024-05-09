
from django import forms
from .models import Comments, Post

class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ("text_comments",)
    
class AddNewPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title","img","content"]