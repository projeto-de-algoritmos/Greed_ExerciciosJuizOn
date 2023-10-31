from django.urls import path
from .views import IndexView, GradeView

urlpatterns = [
    # path('endereco/', MinhaView.as_view(), name='nome-url'),
    path('', IndexView.as_view(), name='inicio'),
    path('grade/', GradeView.as_view(), name='grade'),
]