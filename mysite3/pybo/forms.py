from django import forms
from pybo.models import Question

class QuestionForm(forms.ModelForm): # forms.ModelForm을 상속받음
    class Meta: # Meta 클래스를 반드시 가져야함
        model = Question
        fields = ['subject', 'content']