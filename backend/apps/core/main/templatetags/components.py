from django import template

register = template.Library()


@register.inclusion_tag("components/noscript.html")
def noscript(
    message: str, background: str = "rgba(0, 0, 0, .6)", color: str = "#ffffff"
) -> dict:
    return {"message": message, "background": background, "color": color}
