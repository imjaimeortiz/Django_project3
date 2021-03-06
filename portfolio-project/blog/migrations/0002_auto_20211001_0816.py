# Generated by Django 3.2.7 on 2021-10-01 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='name',
        ),
        migrations.AddField(
            model_name='blog',
            name='body',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='blog',
            name='pub_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='title',
            field=models.CharField(default='', max_length=20),
        ),
    ]
