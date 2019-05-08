# Generated by Django 2.2.1 on 2019-05-08 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0001_initial'),
        ('questions', '0002_auto_20190508_2354'),
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='questions.Question')),
                ('team', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='teams.Team')),
            ],
        ),
    ]
