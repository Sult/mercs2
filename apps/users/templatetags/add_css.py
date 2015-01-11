from django import template
register = template.Library()

@register.filter
def addcss(field, css):
    return field.as_widget(attrs={"class":css})


@register.filter
def space_to_underscore(string):
    return string.replace(" ", "_")
