# Generated by Django 2.2.1 on 2019-05-09 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_submission'),
    ]

    operations = [
        migrations.RenameField(
            model_name='file',
            old_name='question_id',
            new_name='question',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='question_id',
            new_name='question',
        ),
    ]