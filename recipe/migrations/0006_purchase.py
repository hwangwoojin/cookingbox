# Generated by Django 3.1.2 on 2020-10-17 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0005_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_id', models.CharField(help_text='레시피 아이디', max_length=200)),
                ('user_id', models.CharField(help_text='유저 아이디', max_length=200)),
                ('product', models.TextField(help_text='구매 목록', max_length=1000)),
                ('price', models.IntegerField(help_text='구매 가격')),
            ],
        ),
    ]