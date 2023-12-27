from django.shortcuts import get_object_or_404, render
from .models import Question

# Create your views here.
def index(request):
    question_list = Question.objects.all()

    context = {'question_list': question_list}
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    question_list = get_object_or_404(Question, pk=question_id)

    context = {'question_list': question_list}
    return render(request, 'pybo/question_detail.html', context)