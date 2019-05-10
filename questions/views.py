from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.shortcuts import HttpResponse

from .models import Question, Submission, Image, File
from teams.models import Team


def question(request, question_id):
    this_question = get_object_or_404(Question, id=question_id)

    team_id = request.session.get('team_id', None)
    try:
        team = Team.objects.get(id=team_id)
    except Team.DoesNotExist:
        return redirect('/login')

    if request.method == 'GET':
        all_questions = Question.objects.all()

        images = Image.objects.filter(question_id=question_id)
        files = File.objects.filter(question_id=question_id)

        submissions = Submission.objects.filter(team_id=team_id)
        score = sum(map(lambda s: s.question.points, submissions))

        # score = 0
        # for submission in submissions:
        #     score += submission.question.points

        questions_answered = set(map(lambda s: s.question.id, submissions))

        # questions_answered = set()
        # for submission in submissions:
        #     questions_answered.add(submission.question.id)

        return render(request, 'questions/question.html', {
            'this_question': this_question,
            'all_questions': all_questions,
            'questions_answered': questions_answered,
            'teamname': team.teamname,
            'score': score,
            'images': images,
            'files': files
        })
    else:
        answer = request.POST.get("answer", None)
        if answer == this_question.answer:
            try:
                Submission.objects.get(team_id=team_id, question_id=question_id)
                return redirect(f'/question/{question_id}')
            except Submission.DoesNotExist:
                submission = Submission()

                submission.question = this_question
                submission.team = team

                submission.save()
                return redirect(f'/question/{question_id}')
        else:
            return redirect(f'/question/{question_id}')


def leaderboard(request):
    teams = Team.objects.all()
    # [(teamname, participant1, participant2, score), (...), ...]
    data = []
    for team in teams:
        submissions = Submission.objects.filter(team_id=team.id)
        score = sum(map(lambda s: s.question.points, submissions))
        data.append((team.teamname, team.name1, team.name2, score))

    data.sort(key=lambda x: x[3], reverse=True)

    return render(request, 'questions/leaderboard.html', {
        'teams': data
    })
