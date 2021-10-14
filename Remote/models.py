from django.db import models

# Create your models here.

class Keep(models.Model):
    Safein_CHOICES = (
        ('o', '입고확인'),
        ('x', '입고대기'),
        ('w', 'Withdrawn')
    )
    Safeout_CHOICES = (
        ('o', '출고확인'),
        ('x', '출고대기'),
        ('w', 'Withdrawn')
    )
    check_dt = models.DateField('Check-out Date')
    volume_nm = models.CharField('Tape Volume Name', max_length=20)
    pool_nm = models.CharField('Pool Name', max_length=20)
    cycle = models.IntegerField('Keep Cycle', default=14)
    due_dt = models.DateField('Due Date')
    safein_chk = models.CharField('Check in coffer', max_length=1, default="x", choices=Safein_CHOICES)
    safein_dt = models.DateField('Safe-in Date', null=True, blank=True)
    safeout_chk = models.CharField('Check out coffer', max_length=1, default="x", choices=Safeout_CHOICES)
    safeout_dt = models.DateField('Safe-out Date', null=True, blank=True)

    class Meta:
        verbose_name = 'Keep'
        verbose_name_plural = 'keeps'
        db_table = 'RemoteKeep'
        ordering = ('-check_dt','-pool_nm','volume_nm',)

    def __str__(self):
        return self.volume_nm
