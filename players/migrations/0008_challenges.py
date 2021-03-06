# Generated by Django 3.2.4 on 2022-02-23 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0007_players_list_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Challenges',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.CharField(max_length=100)),
                ('c_category', models.CharField(max_length=50)),
                ('c_description', models.CharField(max_length=1000)),
                ('c_point', models.IntegerField()),
                ('c_flag', models.CharField(max_length=350)),
            ],
        ),
    ]
