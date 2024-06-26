# Generated by Django 5.0.3 on 2024-04-01 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=100)),
                ('incorrect_guesses_allowed', models.PositiveSmallIntegerField(default=2)),
                ('incorrect_guesses', models.PositiveSmallIntegerField(default=0)),
                ('guessed_letters', models.CharField(blank=True, max_length=26)),
            ],
        ),
    ]
