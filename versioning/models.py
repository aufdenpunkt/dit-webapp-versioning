# Django
from django.core.validators import RegexValidator
from django.db import models
from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver
from django.utils.translation import ugettext as _


class WebAppVersion(models.Model):
    version_number = models.CharField(
        _("Version"),
        max_length=50,
        unique=True,
        help_text=_("e.g. 1.0.0"),
        validators=[
            RegexValidator(
                regex=r"^\d\.\d\.\d$",
                message=_("Invalid format. Format must be [0-9].[0-9].[0-9]. (e.g. 1.0.0)"),
            ),
        ],
    )

    in_stores = models.BooleanField(
        _("In stores?"),
        default=False,
        help_text=_("Is this the currently available Web-App version in stores?"),
    )

    class Meta:
        verbose_name = _("Web-App Version")
        verbose_name_plural = _("Web-App Versions")
        ordering = [
            "-version_number",
        ]

    def __str__(self) -> str:
        return self.version_number


@receiver(post_save, sender=WebAppVersion)
def unset_previous_web_app_version(sender, instance, **kwargs):
    if instance.in_stores is not True:
        return
    WebAppVersion.objects.filter(in_stores=True).exclude(pk=instance.pk).update(in_stores=False)
