from django.db import models
from django.utils.translation import ugettext_lazy as _


class Albistea(models.Model):
    izenburua = models.CharField(_('izenburua'), max_length=140)
    testua = models.TextField(_('testua'))

    def __unicode__(self):
        return self.izenburua

    class Meta:
        verbose_name = _('Albistea')
        verbose_name_plural = _('Albisteak')
