# Generated by Django 2.1.3 on 2018-12-07 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sections',
            name='classe',
            field=models.ManyToManyField(blank=True, related_name='section_classe', to='student.Classes'),
        ),
    ]
