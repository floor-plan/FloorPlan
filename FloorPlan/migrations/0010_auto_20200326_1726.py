# Generated by Django 3.0.4 on 2020-03-26 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FloorPlan', '0009_teammember_team_member'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammember',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]