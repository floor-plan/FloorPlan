# Generated by Django 3.0.5 on 2020-04-04 17:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FloorPlan', '0011_auto_20200404_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_categories',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='FloorPlan.ProjectCategory'),
        ),
    ]
