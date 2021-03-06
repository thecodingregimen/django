# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-27 11:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BridgeClassEnroll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enrollment_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'django_bridge_class_enroll',
            },
        ),
        migrations.CreateModel(
            name='BridgeInstructorEnroll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assignment_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'django_bridge_instructor_enroll',
            },
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('class_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('class_name', models.CharField(max_length=50)),
                ('class_description', models.CharField(max_length=50)),
                ('class_capacity', models.IntegerField(blank=True, null=True)),
                ('start_time', models.DateTimeField(blank=True, null=True)),
                ('end_time', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'django_class',
            },
        ),
        migrations.CreateModel(
            name='ClassLevel',
            fields=[
                ('level_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('level_name', models.CharField(max_length=50)),
                ('level_description', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'db_table': 'django_class_level',
            },
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('rocket_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('address', models.CharField(blank=True, max_length=50, null=True)),
                ('zip_code', models.CharField(blank=True, max_length=10, null=True)),
                ('state', models.CharField(blank=True, max_length=20, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('cell_phone', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'django_instructor',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('address', models.CharField(blank=True, max_length=50, null=True)),
                ('zip_code', models.CharField(blank=True, max_length=10, null=True)),
                ('state', models.CharField(blank=True, max_length=20, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('cell_phone', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'django_student',
            },
        ),
        migrations.AddField(
            model_name='class',
            name='level',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='nonprofit.ClassLevel'),
        ),
        migrations.AddField(
            model_name='bridgeinstructorenroll',
            name='class_field',
            field=models.ForeignKey(db_column='class_id', on_delete=django.db.models.deletion.DO_NOTHING, to='nonprofit.Class'),
        ),
        migrations.AddField(
            model_name='bridgeinstructorenroll',
            name='rocket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='nonprofit.Instructor'),
        ),
        migrations.AddField(
            model_name='bridgeclassenroll',
            name='class_field',
            field=models.ForeignKey(db_column='class_id', on_delete=django.db.models.deletion.DO_NOTHING, to='nonprofit.Class'),
        ),
        migrations.AddField(
            model_name='bridgeclassenroll',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='nonprofit.Student'),
        ),
        migrations.AlterUniqueTogether(
            name='bridgeinstructorenroll',
            unique_together=set([('rocket', 'class_field')]),
        ),
        migrations.AlterUniqueTogether(
            name='bridgeclassenroll',
            unique_together=set([('student', 'class_field')]),
        ),
    ]
