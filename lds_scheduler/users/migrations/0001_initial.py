# Generated by Django 5.1.6 on 2025-02-10 12:46

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('calling', models.CharField(choices=[('Bishop', 'B'), ('Member', 'M'), ('Elder', 'E'), ('QPresident', 'QP'), ('QCounselor', 'QC'), ('JWPresident', 'JWP'), ('JWCounselor', 'JWC'), ('RSPresident', 'RSP'), ('RSCounselor', 'RSC')], default='Member', max_length=25)),
                ('memberId', models.BigIntegerField()),
                ('createAt', models.DateTimeField(auto_now_add=True)),
                ('image', models.CharField(max_length=255)),
            ],
        ),
    ]
