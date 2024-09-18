# Generated by Django 5.1.1 on 2024-09-18 18:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('actors', '0002_alter_actors_options'),
        ('genres', '0002_alter_genre_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('year_released', models.DateField()),
                ('nationality', models.CharField(blank=True, choices=[('BRA', 'Brasil'), ('USA', 'Estados Unidos')], max_length=100, null=True)),
                ('resume', models.TextField(blank=True, null=True)),
                ('actors', models.ManyToManyField(related_name='movies_actor', to='actors.actors')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='movies_genre', to='genres.genre')),
            ],
        ),
    ]
