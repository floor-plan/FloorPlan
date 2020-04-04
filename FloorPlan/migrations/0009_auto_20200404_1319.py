# Generated by Django 3.0.5 on 2020-04-04 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FloorPlan', '0008_merge_20200404_0108'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.TextField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(choices=[('PLUMBING', 'Plumbing'), ('ELECTRICAL', 'Electrical'), ('MASONRY', 'Masonry'), ('FRAMING', 'Framing'), ('ROOFING', 'Roofing'), ('TILING', 'Tiling'), ('HOMEOWNER', 'Homeowner'), ('MISC', 'Misc')], default='HOMEOWNER', max_length=30),
        ),
        migrations.AddField(
            model_name='project',
            name='project_categories',
            field=models.ManyToManyField(to='FloorPlan.ProjectCategory'),
        ),
    ]
