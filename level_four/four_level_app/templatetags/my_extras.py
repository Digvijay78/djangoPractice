from django import template

register = template.Library()


@register.filter(name = 'cut')
def cut(value, arg):
    
    
    result = value.replace(arg, 'Digvijay')
    
   
    
    
    return result

# register.filter('cut', cut)
