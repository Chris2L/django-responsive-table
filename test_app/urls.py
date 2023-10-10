from django.urls import path

from .views import AuthorHTMxTableView, index, index_tables2

urlpatterns = [
    path('', index, name='home'),
    path('tables2/', AuthorHTMxTableView.as_view(), name='home2'),
]