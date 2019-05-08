from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import Http404
from django.shortcuts import get_object_or_404

from .models import Question, Submission, Image, File
from teams.models import Team


def question(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    all_questions = Question.objects.all()

    team_id = request.session.get('team_id', None)
    team = None
    try:
        team = Team.objects.get(id=team_id)
    except:
        return redirect('/login')

    submissions = Submission.objects.filter(team_id=team.id)
    score = 0
    # score = sum(filter(lambda s: s.question.points, submissions))
    for submission in submissions:
        score += submission.question.points

    return render(request, 'questions/question.html', {
        'question': question,
        'all_questions': all_questions,
        'teamname': team.teamname,
        'score': score,
    })


def leaderboards(request):
    pass
