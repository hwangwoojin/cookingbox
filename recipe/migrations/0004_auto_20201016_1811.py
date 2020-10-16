# Generated by Django 3.1.2 on 2020-10-16 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0003_recipe_profile'),
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
        migrations.AddField(
            model_name='recipe',
            name='image',
            field=models.ManyToManyField(to='recipe.Image'),
        ),
    ]