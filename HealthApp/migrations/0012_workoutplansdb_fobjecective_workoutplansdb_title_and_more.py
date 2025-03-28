# Generated by Django 5.1.3 on 2024-11-16 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HealthApp', '0011_rename_workoutplans_workoutplansdb'),
    ]

    operations = [
        migrations.AddField(
            model_name='workoutplansdb',
            name='FObjecective',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='workoutplansdb',
            name='Title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='workoutplansdb',
            name='Friday',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='workoutplansdb',
            name='Monday',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='workoutplansdb',
            name='Saturday',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='workoutplansdb',
            name='Sunday',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='workoutplansdb',
            name='Thursday',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='workoutplansdb',
            name='Tuesday',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='workoutplansdb',
            name='Wednesday',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
