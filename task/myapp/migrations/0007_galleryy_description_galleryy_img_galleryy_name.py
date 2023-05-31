# Generated by Django 4.2.1 on 2023-05-19 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_galleryy'),
    ]

    operations = [
        migrations.AddField(
            model_name='galleryy',
            name='description',
            field=models.CharField(default=4444, max_length=70),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='galleryy',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.AddField(
            model_name='galleryy',
            name='name',
            field=models.CharField(default=3333, max_length=50),
            preserve_default=False,
        ),
    ]
