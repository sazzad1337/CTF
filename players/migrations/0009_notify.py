# Generated by Django 3.2.12 on 2022-03-11 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0008_challenges'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notify',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.CharField(max_length=100)),
                ('time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]