from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from django.template import loader
from .models import Question

#static index page
# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

# include latest poll questions in the index page
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     output = ', '.join([q.question_text for q in latest_question_list])
#     return HttpResponse(output)

#index page that is not hardcoded in views. 
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return HttpResponse(template.render(context, request))

#same but using django's render shortcut
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


#just for testing. It displays the question number entered in the URL even if it does not exit
# def detail(request, question_id):
#     return HttpResponse("You're looking at question %s." % question_id)

#Raises 404 error if requested question does not exit. or goes to the details page of the question
# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, 'polls/detail.html', {'question': question})

#same but using shortcut to raising 404 error
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
