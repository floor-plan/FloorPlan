# Generated by Django 3.0.5 on 2020-07-08 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FloorPlan', '0018_auto_20200405_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='project',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='FloorPlan.Project'),
        ),
    ]