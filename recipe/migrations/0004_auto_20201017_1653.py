# Generated by Django 3.1.2 on 2020-10-17 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0003_auto_20201017_1516'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_id', models.CharField(help_text='요리법의 아이디', max_length=200)),
                ('user_id', models.CharField(help_text='유저 아이디', max_length=200)),
            ],
        ),
        migrations.AlterModelOptions(
            name='ingredient',
            options={'ordering': ['name']},
        ),
    ]
