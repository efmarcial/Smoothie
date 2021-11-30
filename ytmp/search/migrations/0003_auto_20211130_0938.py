# Generated by Django 3.2.9 on 2021-11-30 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_menu'),
    ]

    operations = [
        migrations.CreateModel(
            name='preview_smoothie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('discription', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Smoothie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('discription', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Snacks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('discription', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=50)),
            ],
        ),
        migrations.RenameModel(
            old_name='Menu',
            new_name='Aguas',
        ),
        migrations.RenameField(
            model_name='aguas',
            old_name='name',
            new_name='title',
        ),
    ]
