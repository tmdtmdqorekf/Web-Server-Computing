from django.shortcuts import render
from .models import Question

# Create your views here.
def index(request):
    question_list = Question.objects.all()
    context = {'question_list': question_list}
    return render(request, 'pybo/question_list.html', context)