# Generated by Django 3.2 on 2021-12-20 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0003_solutiondetail_intro_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='solutiondetail',
            name='number',
            field=models.CharField(default='..', max_length=5),
        ),
    ]