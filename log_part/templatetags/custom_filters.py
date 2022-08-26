from django import template

register = template.Library()


def range_filter(value):
    return value[:10] + "...."


def phone_range_filter(value):
    return value[:4]


register.filter('range_filter', range_filter)
register.filter('phone_range_filter', phone_range_filter)
