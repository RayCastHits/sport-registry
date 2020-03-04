import json

from django import template
from django.utils.safestring import mark_safe
from webpack_loader.exceptions import WebpackBundleLookupError
from webpack_loader.utils import get_as_tags

from ..template import EvaluateNode

register = template.Library()


@register.simple_tag
def get_langs_json(langs):
    result = dict()
    for lang in langs:
        result[lang[0]] = lang[1]
    return json.dumps(result)


@register.simple_tag
def vardump(var):
    return vars(var)


@register.simple_tag
def dirdump(var):
    return dir(var)


@register.simple_tag
def define(val=None):
    return val


@register.tag(name="evaluate_template")
def evaluate_template(_parser, token):
    """
    tag usage {% evaluate object.textfield %}
    """
    return EvaluateNode(token.split_contents()[1])


@register.simple_tag
def render_bundle(bundle_name, extension=None, config="DEFAULT", attrs=""):
    try:
        tags = get_as_tags(
            bundle_name, extension=extension, config=config, attrs=attrs
        )
        return mark_safe("\n".join(tags))
    except WebpackBundleLookupError:
        return ""
