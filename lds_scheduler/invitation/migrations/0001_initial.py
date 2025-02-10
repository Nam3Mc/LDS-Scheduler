# Generated by Django 5.1.6 on 2025-02-10 12:46

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('appoiment', '0001_initial'),
        ('friend', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('status', models.CharField(choices=[('Active', 'AT'), ('Completed', 'CO'), ('Canceled', 'CA'), ('Acepted', 'AC'), ('Rejected', 'RE'), ('Edited', 'ED'), ('Incompleted', 'IN'), ('Pending', 'PE')], default='Pending', max_length=20)),
                ('appoiment', models.ManyToManyField(to='appoiment.appoiment')),
                ('friend', models.ManyToManyField(to='friend.friend')),
                ('user', models.ManyToManyField(to='users.user')),
            ],
        ),
    ]
