# Generated by Django 2.1.1 on 2019-02-05 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('churches', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='model_church',
            name='preachingStyle',
            field=models.CharField(choices=[('Topical', 1), ('Verse-by-verse', 2), ('Narrative', 3), ('Other', 4), ('Mix', 5)], max_length=128),
        ),
        migrations.AlterField(
            model_name='model_church',
            name='smallGroups',
            field=models.CharField(choices=[('Yes', 1), ('No', 2)], max_length=3),
        ),
        migrations.AlterField(
            model_name='model_church',
            name='sundaySchool',
            field=models.CharField(choices=[('Yes', 1), ('No', 2)], max_length=3),
        ),
    ]
