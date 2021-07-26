# Generated by Django 2.2.4 on 2021-07-26 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20210723_1900'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartment',
            name='contact_number',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='apartment_img',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
