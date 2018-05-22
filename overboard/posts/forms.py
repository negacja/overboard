from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from posts.models import Question
from tags.models import Tag
import re
import datetime
from django_select2.forms import Select2MultipleWidget, Select2TagWidget


class AnswerForm(forms.Form):
    answer = forms.CharField(label='answer')


class VoteForm(forms.Form):
    vote = forms.IntegerField(label='vote')
    target = forms.IntegerField(label='target')


class AnswerVoteForm(forms.Form):
    vote = forms.IntegerField(label='vote')
    target = forms.IntegerField(label='target')
    answer = forms.CharField(label='answer', max_length=100)


class NewQuestionForm(forms.Form):
    title = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    tags = forms.MultipleChoiceField(widget=Select2MultipleWidget(attrs={'tags': 'false', 'class': 'form-control', 'rows': 3}),
                                     choices=[(obj.tag_name, obj.tag_name) for obj in Tag.objects.all()])

    #tags = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 2}), required=False,
    #                       help_text='Tag should be one string of characters started with # sign. Separate tags with whitespace.')

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(NewQuestionForm, self).__init__(*args, **kwargs)
        if self.user:
            if self.user.reputation >= 20:
                del self.fields['tags']
                self.fields['tags'] = forms.MultipleChoiceField(
                    widget=Select2TagWidget(attrs={'tags': 'false', 'class': 'form-control', 'rows': 3}),
                    choices=[(obj.tag_name, obj.tag_name) for obj in Tag.objects.all()])

    def save(self):
        question = Question.objects.create(asked_by=User.objects.get(pk=self.data['user_id']),
                                           title=self.data['title'],
                                           content=self.data['content'],
                                           pub_date=datetime.datetime.now())
        question.save()
        regex = re.compile(r'^#*')
        tags_list = [tag for tag in self.data['tags'].split() if regex.match(tag)]
        tags_names = [re.sub('#', '', tag) for tag in tags_list]

        for tag_name in tags_list:
            if Tag.objects.filter(tag_name=tag_name).exists():
                Tag.objects.get(tag_name=tag_name).questions.add(question)
            else:
                tag = Tag.objects.create(tag_name=tag_name)
                tag.questions.add(question)
                tag.save()
        return


