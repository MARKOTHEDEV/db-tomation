# Generated by Django 3.2 on 2021-12-20 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='solutiondetail',
            name='hover_icon',
            field=models.CharField(default='..', max_length=70),
        ),
        migrations.AddField(
            model_name='solutiondetail',
            name='main_icon',
            field=models.CharField(default='..', max_length=70),
        ),
    ]