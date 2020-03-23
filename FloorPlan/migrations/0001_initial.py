# Generated by Django 3.0.4 on 2020-03-23 16:55

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('company', models.CharField(blank=True, max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('phone', phone_field.models.PhoneField(max_length=9)),
            ],
        ),
    ]
