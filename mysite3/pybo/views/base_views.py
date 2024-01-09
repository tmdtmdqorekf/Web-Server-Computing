from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q, Count

from ..models import Question

def index(request):
    # localhost:8000/pybo/?page=1 처럼
    # GET 방식으로 호출된 URL에서 page 가져올 때 사용
    page = request.GET.get('page', '1')
    kw = request.GET.get('kw', '')  # 검색어
    so = request.GET.get('so', 'recent') # 정렬 기준

    if so == 'recommend':
        question_list = Question.objects.annotate(
            num_voter=Count('voter')).order_by('-num_voter', '-created_date')
    elif so == 'popular':
        question_list = Question.objects.annotate(
            num_answer=Count('answer')).order_by('-num_answer', '-created_date')
    else:
        question_list = Question.objects.order_by('-created_date')

    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) |  # 제목 검색
            Q(content__icontains=kw) |  # 내용 검색
            Q(answer__content__icontains=kw) |  # 답변 내용 검색
            Q(author__username__icontains=kw) |  # 질문 글쓴이 검색
            Q(answer__author__username__icontains=kw)  # 답변 글쓴이 검색
        ).distinct()
    
    # 페이지당 10개씩 보여주기
    paginator = Paginator(question_list, 10)
    # 요청된 페이지에 해당되는 페이징 객체 생성
    # 데이터 전체 조회 x, 해당 페이지의 데이터만 조회하도록 쿼리가 변경됨
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj, 'page': page, 'kw': kw}
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)