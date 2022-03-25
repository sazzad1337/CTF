# Generated by Django 3.2.12 on 2022-03-22 17:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('players', '0011_auto_20220313_1321'),
    ]

    operations = [
        migrations.CreateModel(
            name='score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now=True)),
                ('points', models.IntegerField(null=True)),
                ('solved', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='players.challenges')),
                ('solver_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='scoreboard',
        ),
    ]