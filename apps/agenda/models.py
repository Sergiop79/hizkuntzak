from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse


class Ebentua(models.Model):
    ebentua = models.CharField(_('ebentua'), max_length=140)
    data = models.DateTimeField(_('data'))
    lekua = models.CharField(_('lekua'), max_length=140)

    def get_absolute_url(self):
        return reverse('ebentua-detail', kwargs={'pk': self.pk})

    def __unicode__(self):
        return self.ebentua

    class Meta:
        verbose_name = _('Ebentua')
        verbose_name_plural = _('Ebentuak')
