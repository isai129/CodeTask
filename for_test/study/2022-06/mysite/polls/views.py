# Create your views here.
from django.http import HttpResponseRedirect  # http响应,重定向
from django.shortcuts import get_object_or_404, render
#  get_object_or_404()  尝试用 get() 函数获取一个对象，如果不存在就抛出 Http404
#  快捷函数： render()「载入模板，填充上下文，再返回由它生成的 HttpResponse 对象」
from django.urls import reverse
from django.views import generic

from .models import Question, Choice


# from django.template import loader  # 载入模板


# 主页
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    # output = ', '.join([q.question_text for q in latest_question_list])
    #  return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', context)


# 详情
def detail(request, question_id):
    # return HttpResponse("You`re looking at question %s." % question_id)
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # return render(request, 'polls/detail.html', {'question': question})
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


# 结果
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # response = "You`re looking at the results of question %s."
    # return HttpResponse(response % question_id)
    return render(request, 'polls/results.html', {'question': question})


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


# 投票
def vote(request, question_id):
    # return HttpResponse("You1re voting on question %s." % question_id)
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html',
                      {'question': question, 'error_message': "You didn`t select a choice."})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
