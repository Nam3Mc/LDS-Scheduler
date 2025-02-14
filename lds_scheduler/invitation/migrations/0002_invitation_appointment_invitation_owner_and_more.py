# Generated by Django 5.1.6 on 2025-02-13 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0002_appointment_friend'),
        ('invitation', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='invitation',
            name='appointment',
            field=models.ManyToManyField(to='appointment.appointment'),
        ),
        migrations.AddField(
            model_name='invitation',
            name='owner',
            field=models.ManyToManyField(related_name='invitation_owner', to='users.user'),
        ),
        migrations.AlterField(
            model_name='invitation',
            name='user',
            field=models.ManyToManyField(related_name='invited', to='users.user'),
        ),
    ]
