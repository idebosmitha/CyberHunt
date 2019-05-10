from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Team


def home(request):
    return render(request, 'teams/home.html')


def login(request):
    if request.method == 'GET':
        return render(request, 'teams/login.html')
    else:
        teamname = request.POST.get('teamname', None)
        password = request.POST.get('password', None)

        if teamname is not None and password is not None:
            try:
                team = Team.objects.get(teamname=teamname, password=password)
                request.session['team_id'] = team.id
                return redirect('/question/1')
            except Team.DoesNotExist:
                return render(request, 'teams/login.html', {'error': 'Invalid credentials'})
        else:
            return render(request, 'teams/login.html', {'error': 'All fields are required'})


def register(request):
    if request.method == 'GET':
        return render(request, 'teams/register.html')
    else:  # request.method == 'POST'
        team = Team()
        teamname = request.POST.get('teamname', None)
        password1 = request.POST.get('password1', None)
        password2 = request.POST.get('password2', None)

        name1 = request.POST.get('name1', None)
        year1 = request.POST.get('year1', None)
        dept1 = request.POST.get('dept1', None)
        phone1 = request.POST.get('phone1', None)

        name2 = request.POST.get('name2', None)
        year2 = request.POST.get('year2', None)
        dept2 = request.POST.get('dept2', None)
        phone2 = request.POST.get('phone2', None)

        if all((teamname, password1, password2, name1, name2, year1, year2, dept1, dept2, phone1, phone2)):
            team.teamname = teamname
            if password1 != password2:
                return render(request, 'teams/register.html', {'error': 'Passwords don\'t match'})
            
            team.password = password1
            team.name1 = name1
            team.year1 = year1
            team.dept1 = dept1
            team.phone1 = phone1

            team.name2 = name2
            team.year2 = year2
            team.dept2 = dept2
            team.phone2 = phone2

            team.save()

            return redirect('login')
        else:
            return render(request, 'teams/register.html', {'error': 'All fields are required'})


def logout(request):
    pass
