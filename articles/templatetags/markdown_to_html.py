from django import template
from django.template.defaultfilters import stringfilter

import markdown

register = template.Library()


@register.filter(name="markdown")
@stringfilter
def html_formatter(value):
    """
    Django custom filter that formats a markdown formatted string to html formatted
    text
    """
    extensions = ["fenced_code", "tables", "def_list", "codehilite", "toc"]
    return markdown.markdown(value, extensions=extensions)
