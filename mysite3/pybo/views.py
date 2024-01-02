from django.utils import timezone
from django.shortcuts import get_object_or_404, redirect, render
from .models import Question
from .forms import QuestionForm, AnswerForm
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    # localhost:8000/pybo/?page=1 처럼
    # GET 방식으로 호출된 URL에서 page 가져올 때 사용
    page = request.GET.get('page', '1')

    question_list = Question.objects.all()
    
    # 페이지당 10개씩 보여주기
    paginator = Paginator(question_list, 10)
    # 요청된 페이지에 해당되는 페이징 객체 생성
    # 데이터 전체 조회 x, 해당 페이지의 데이터만 조회하도록 쿼리가 변경됨
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj}
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)

def answer_create(request, question_id):
    question=get_object_or_404(Question, pk=question_id)

    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.created_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        form = AnswerForm()
    
    context = {'question': question, 'form': form}
    return render(request, 'pybo/question_detail.html', context)

def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.created_date = timezone.now()
            question.save()
            return redirect('pybo:index')
    else:
        form = QuestionForm()
    
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)