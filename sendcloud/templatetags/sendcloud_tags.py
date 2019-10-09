import logging
from enum import IntEnum
from django import template
from django.utils.translation import ugettext_lazy as _

register = template.Library()
logger = logging.getLogger("sendcloud")


class TemplateType(IntEnum):
    Trigging = 0
    Batch = 1


ttype = {
    TemplateType.Trigging: _("trigging"),
    TemplateType.Batch: _("batch")
}


@register.filter
def template_type(value):
    # logger.info(TemplateType.Batch)
    return ttype[value]

