# Generated by Django 4.2.1 on 2023-05-25 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('p_app', '0002_personal_info_alter_profile_gender'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='personal_info',
            new_name='p_info',
        ),
    ]