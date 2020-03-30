# Generated by Django 3.0.4 on 2020-03-30 22:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('PLUMBING', 'Plumbing'), ('ELECTRICAL', 'Electrical'), ('MASONRY', 'Masonry'), ('FRAMING', 'Framing'), ('ROOFING', 'Roofing'), ('HOMEOWNER', 'Homeowner')], default='HOMEOWNER', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('address', models.CharField(max_length=400)),
                ('lot_number', models.CharField(blank=True, max_length=100)),
                ('category', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='FloorPlan.Category')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=100, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('role', models.CharField(choices=[('PROJECT-MANAGER', 'Project-Manager'), ('SUPPLIER', 'Supplier'), ('SUB-CONTRACTOR', 'Sub-Contractor'), ('HOMEOWNER', 'Homeowner')], default='misc', max_length=30)),
                ('category', models.CharField(choices=[('PROJECT-MANAGER', 'Project-Manager'), ('PLUMBING', 'Plumbing'), ('ELECTRICAL', 'Electrical'), ('MASONRY', 'Masonry'), ('FRAMING', 'Framing'), ('ROOFING', 'Roofing'), ('HOMEOWNER', 'Homeowner')], default='misc', max_length=30)),
                ('is_project_manager', models.BooleanField(default=False)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='FloorPlan.Project')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.TextField(max_length=300)),
                ('is_complete', models.BooleanField(default=False)),
                ('assignee', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='FloorPlan.User')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='FloorPlan.Category')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='FloorPlan.Project')),
            ],
        ),
    ]
