from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ['title', 'content', 'image', 'thumbnail', ]
        label = {
            'title': '제목',
            'content': '내용',
            'image': '이미지(선택)',
            'thumbnail': '썸네일 이미지(선택'
        }
