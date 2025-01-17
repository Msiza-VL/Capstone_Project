# Generated by Django 5.1.3 on 2025-01-12 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_type', models.CharField(choices=[('Running', 'Running'), ('Cycling', 'Cycling'), ('Weightlifting', 'Weightlifting')], max_length=50)),
                ('duration', models.PositiveIntegerField(help_text='Duration in minutes')),
                ('distance', models.FloatField(blank=True, help_text='Distance in kilometres', null=True)),
                ('calories_burned', models.PositiveIntegerField()),
                ('date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Activities',
            },
        ),
    ]
