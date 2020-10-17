# Generated by Django 3.1.2 on 2020-10-17 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0004_auto_20201017_1653'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='제품의 이름(ex: 물)', max_length=200)),
                ('product_name', models.CharField(help_text='제품의 실제 이름(ex: 삼다수)', max_length=200)),
                ('image', models.ImageField(blank=True, help_text='제품의 이미지', upload_to='')),
                ('amount', models.CharField(help_text='제품의 양', max_length=200)),
                ('price', models.IntegerField(help_text='제품의 가격')),
            ],
        ),
    ]