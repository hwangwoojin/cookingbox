# Generated by Django 3.1.2 on 2020-10-17 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, help_text='요리법에 대한 사진', upload_to='')),
                ('description', models.CharField(help_text='요리법에 대한 설명', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(help_text='재료의 종류', max_length=200)),
                ('name', models.CharField(help_text='제품명', max_length=200)),
                ('image', models.ImageField(blank=True, help_text='재료의 사진', upload_to='')),
                ('amount', models.CharField(help_text='재료의 양', max_length=200)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='genre',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='recipe',
            options={'ordering': ['title']},
        ),
        migrations.AddField(
            model_name='recipe',
            name='genre',
            field=models.ManyToManyField(to='recipe.Genre'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='profile',
            field=models.ImageField(blank=True, help_text='요리에 대한 사진', upload_to=''),
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ManyToManyField(to='recipe.Product')),
            ],
        ),
        migrations.AddField(
            model_name='recipe',
            name='image',
            field=models.ManyToManyField(to='recipe.Image'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredient',
            field=models.ManyToManyField(to='recipe.Ingredient'),
        ),
    ]