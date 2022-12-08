# Generated by Django 4.1.3 on 2022-11-30 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_myteam'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_date', models.DateTimeField()),
                ('team_a_goal', models.IntegerField()),
                ('team_b_goal', models.IntegerField()),
                ('team_a', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='team_a_matches', to='app.team')),
                ('team_b', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='team_b_matches', to='app.team')),
            ],
        ),
    ]
