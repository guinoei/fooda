# Generated by Django 5.0.3 on 2024-03-25 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodaapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='category',
            field=models.CharField(blank=True, choices=[('Restaurant', 'Restaurant'), ('Dessert', 'Dessert'), ('"Fast Food"', '"Fast Food"')], max_length=100, null=True),
        ),
    ]