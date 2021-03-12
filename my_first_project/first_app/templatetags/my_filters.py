#to customixation of html tag or add css

from django import template

register = template.Library()

def my_filter(value, arg):
    return value + " " + arg


register.filter('custom_filter', my_filter)