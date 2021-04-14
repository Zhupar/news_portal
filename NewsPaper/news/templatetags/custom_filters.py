from django import template

register = template.Library()
# если мы не зарегистрируем наши фильтры, то Django никогда не узнает, где именно их искать и фильтры потеряются

censor_words = ['идиот', 'блять', 'сука', 'ёмоё', 'дурак']


@register.filter(
    name='censor')  # регистрируем наш фильтр под именем multiply, чтоб django понимал, что это именно фильтр, а не простая функция
def censor(
        value):  # первый аргумент здесь это то значение, к которому надо применить фильтр, второй аргумент — это аргумент фильтра, т.е. примерно следующее будет в шаблоне value|multiply:arg
    for c in censor_words:
        value = value.replace(c, '!@#$%')
    return value
