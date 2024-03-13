# Generated by Django 3.2.8 on 2024-03-10 10:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('expertdb', '0002_auto_20240229_2020'),
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': '专业',
                'verbose_name_plural': '专业',
            },
        ),
        migrations.CreateModel(
            name='SectionDoctors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='major',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='schedule',
        ),
        migrations.AlterField(
            model_name='doctor',
            name='info',
            field=models.TextField(blank=True, null=True, verbose_name='介绍'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='link',
            field=models.URLField(blank=True, max_length=300, null=True, verbose_name='挂号网址'),
        ),
        migrations.DeleteModel(
            name='OutpatientSchedule',
        ),
        migrations.DeleteModel(
            name='Profession',
        ),
        migrations.AddField(
            model_name='sectiondoctors',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expertdb.doctor'),
        ),
        migrations.AddField(
            model_name='sectiondoctors',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expertdb.section'),
        ),
        migrations.AddField(
            model_name='section',
            name='doctors',
            field=models.ManyToManyField(blank=True, through='expertdb.SectionDoctors', to='expertdb.Doctor'),
        ),
    ]
