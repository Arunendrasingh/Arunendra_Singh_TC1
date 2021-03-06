# Generated by Django 3.2.8 on 2022-02-09 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('is_solved', models.BooleanField(default=False)),
                ('solved_by', models.CharField(max_length=50)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('issue_date', models.DateTimeField(auto_now_add=True)),
                ('solving_date', models.DateTimeField(null=True)),
            ],
        ),
    ]
