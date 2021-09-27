from django.db import models

# Create your models here.

class Keep(models.Model):
    check_dt = models.DateField('Check-out Date')
    volume_nm = models.CharField('Tape Volume Name', max_length=20)
    pool_nm = models.CharField('Pool Name', max_length=20)
    cycle = models.IntegerField('Keep Cycle', default=14)
    due_dt = models.DateField('Due Date')
    safein_chk = models.CharField('Check in coffer', max_length=20, default="X")
    safeout_chk = models.CharField('Check out coffer', max_length=20, default="X")

    class Meta:
        verbose_name = 'Keep'
        verbose_name_plural = 'keeps'
        db_table = 'RemoteKeep'
        ordering = ('-check_dt','pool_nm','volume_nm',)

    def __str__(self):
        return self.volume_nm

    def __date__ (self):
        return self.check_dt