from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from .models import Question, Submission, Image, File
from teams.models import Team


def question(request, question_id):  # TODO: add request methods
    this_question = get_object_or_404(Question, id=question_id)
    all_questions = Question.objects.all()

    team_id = request.session.get('team_id', None)

    images = Image.objects.filter(question_id=question_id)
    files = File.objects.filter(question_id=question_id)

    print(files)

    try:
        team = Team.objects.get(id=team_id)
    except Team.DoesNotExist:
        return redirect('/login')

    submissions = Submission.objects.filter(team_id=team.id)
    score = sum(map(lambda s: s.question.points, submissions))

    questions_answered = set(map(lambda s: s.question.id, submissions))

    return render(request, 'questions/question.html', {
        'this_question': this_question,
        'all_questions': all_questions,
        'questions_answered': questions_answered,
        'teamname': team.teamname,
        'score': score,
        'images': images,
        'files': files
    })


def leaderboard(request):
    pass
