# Generated by Django 3.0.4 on 2020-03-26 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FloorPlan', '0006_remove_task_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='project',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='FloorPlan.Project'),
        ),
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(choices=[('PLUMBING', 'Plumbing'), ('ELECTRICAL', 'Electrical'), ('MASONRY', 'Masonry'), ('FRAMING', 'Framing'), ('ROOFING', 'Roofing')], default='misc', max_length=30),
        ),
        migrations.AddConstraint(
            model_name='category',
            constraint=models.UniqueConstraint(fields=('category', 'project'), name='unique_team'),
        ),
    ]
