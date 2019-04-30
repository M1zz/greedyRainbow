from django import template
register = template.Library()

@register.filter            # 1
def search_index(arr, i):
    return arr[int(i)]