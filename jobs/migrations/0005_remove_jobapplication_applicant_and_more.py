# Generated by Django 4.1.7 on 2023-03-06 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_jobapplication'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobapplication',
            name='applicant',
        ),
        migrations.RemoveField(
            model_name='jobapplication',
            name='applied_at',
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='email',
            field=models.EmailField(default='Unknown', max_length=254),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='name',
            field=models.CharField(default='Unknown', max_length=255),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='cover_letter',
            field=models.TextField(blank=True),
        ),
    ]
