# Generated by Django 4.0.4 on 2022-08-18 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_api', '0008_merge_20220818_1904'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='subject',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
