# Generated by Django 3.2.8 on 2021-11-18 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='upload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('upload', models.FileField(upload_to='media')),
            ],
        ),
        migrations.DeleteModel(
            name='Feedbak',
        ),
    ]