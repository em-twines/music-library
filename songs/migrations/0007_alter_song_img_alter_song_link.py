# Generated by Django 4.1.4 on 2022-12-12 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0006_alter_song_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='img',
            field=models.CharField(default='', max_length=3000),
        ),
        migrations.AlterField(
            model_name='song',
            name='link',
            field=models.CharField(default='', max_length=3000),
        ),
    ]