from django import forms
from pybo.models import Question, Answer

class QuestionForm(forms.ModelForm): # forms.ModelForm을 상속받음
    class Meta: # Meta 클래스를 반드시 가져야함
        model = Question
        fields = ['subject', 'content']
        labels = {
            'subject': '제목',
            'content': '내용',
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }