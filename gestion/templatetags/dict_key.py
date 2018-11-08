from django.template.defaultfilters import register

@register.filter(name='dict_key')
def dict_key(diccionario, clave):
    """
    Retorna el elemento de un diccionario, dada su clave
    como una variable.
    """
    return diccionario[clave]
