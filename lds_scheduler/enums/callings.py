from django.db import models

class Callings(models.TextChoices):
    BISHOP = 'Bishop', 'B'
    MEMBER = 'Member', 'M'
    ELDER = 'Elder', 'E'
    QPRESIDENT = 'QPresident', 'QP'
    QCOUNSELOR = 'QCounselor', 'QC'
    JWPRESIDENT = 'JWPresident', 'JWP'
    JWCOUNSELOR = 'JWCounselor', 'JWC'
    RSPRESIDENT = 'RSPresident', 'RSP'
    RSCOUNSELOR = 'RSCounselor', 'RSC'