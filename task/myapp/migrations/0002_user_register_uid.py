# Generated by Django 4.1.7 on 2023-05-11 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_register',
            name='uid',
            field=models.IntegerField(default=100),
            preserve_default=False,
        ),
    ]