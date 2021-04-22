from django_filters import FilterSet, CharFilter, DateFilter  # импортируем filterset, чем-то напоминающий знакомые дженерики
from django.forms import DateInput

from .models import Post




# создаём фильтр
class PostFilter(FilterSet):
    post_title = CharFilter(field_name='post_title', lookup_expr='icontains', label='Заголовок')
    post_date_time = DateFilter(field_name='post_date_time', widget=DateInput(attrs={'type': 'date'}),
                                         lookup_expr='gt', label='Позже даты')
    # Здесь в мета классе надо предоставить модель и указать поля по которым будет фильтроваться (т.е. подбираться) информация о товарах
    class Meta:
        model = Post
        fields = ['post_author']




