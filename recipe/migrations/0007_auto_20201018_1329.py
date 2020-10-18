# Generated by Django 3.1.2 on 2020-10-18 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0006_purchase'),
    ]

    operations = [
        migrations.CreateModel(
            name='SecretIngredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='재료의 이름', max_length=200)),
                ('amount', models.CharField(help_text='재료의 양', max_length=200)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='recipe',
            name='secret_ingredient',
            field=models.ManyToManyField(to='recipe.SecretIngredient'),
        ),
    ]