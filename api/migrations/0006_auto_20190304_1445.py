# Generated by Django 2.1 on 2019-03-04 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20190227_1013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='skills_list',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='offer',
            name='title',
            field=models.CharField(max_length=112),
        ),
    ]
