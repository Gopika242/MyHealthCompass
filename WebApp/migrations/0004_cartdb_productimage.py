# Generated by Django 5.1 on 2024-12-05 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0003_cartdb'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartdb',
            name='ProductImage',
            field=models.ImageField(blank=True, null=True, upload_to='cart'),
        ),
    ]
