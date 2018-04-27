from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.db.models import Count, Sum, Q
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.views import View
from django.views.generic import ListView
from django.contrib.auth import login, authenticate
import datetime

from posts.models import Question, Vote, Answer
from tags.models import Tag
from .forms import RegistrationForm
from posts.forms import AnswerForm

# Create your views here.


class QuestionList(ListView):
    model = Question
    context_object_name = 'questions'
    selected_tab = ''
    template_name = 'index_content.html'

    def get_context_data(self, **kwargs):
        context = super(QuestionList, self).get_context_data(**kwargs)
        context['selected_tab'] = self.selected_tab
        return context

    def get_queryset(self):
        return Question.objects.all().order_by('-pub_date')


def user_page(request, user_id):
    other_user = get_object_or_404(User, pk=user_id)
    form = AnswerForm
    return render(request, 'user_page.html', {'otheruser': other_user, 'form': form })


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect(reverse('core:index'))
    else:
        form = RegistrationForm()
    return render(request, 'register_form.html', {'form': form})