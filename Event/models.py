from django.db import models

# Create your models here.

#from django.urls import reverse

class Log(models.Model):
    backup_dt = models.DateTimeField('Backup Date')
    schedule_tm = models.CharField('Scheduled Time', max_length=20)
    schedule_nm = models.CharField('Schedule Name', max_length=50)
    nodename = models.CharField('Schedule Name', max_length=50)
    domain_nm = models.CharField('Domain Name', max_length=50)
    start_tm = models.CharField('Start Time', max_length=20)
    end_tm = models.CharField('End Time', max_length=20)
    taken = models.IntegerField('Taken Time', default=0)
    status = models.CharField('Backup Result', max_length=20)
    returncode = models.IntegerField('Return Code')
    action = models.TextField('Action Content')
    note = models.TextField('Note')
    modify_dt = models.DateTimeField('MODIFY DATE', auto_now=True)

    class Meta:
        verbose_name = 'Log'
        verbose_name_plural = 'logs'
        db_table = 'EventLog'
        ordering = ('domain_nm','schedule_tm',)

    def __str__(self):
        return f'{self.schedule_tm} {self.schedule_nm} {self.nodename} {self.domain_nm} {self.start_tm}'
#        return '{0} {1}'.format(self.schedule_tm, self.schedule_nm)

    def __date__ (self):
        return self.backup_dt
