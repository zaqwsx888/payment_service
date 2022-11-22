from django.urls import path
from .views import ItemDetailView, BuyView

urlpatterns = [
    path('item/<int:item_pk>', ItemDetailView.as_view(), name='item'),
    path('buy/<int:item_pk>', BuyView.as_view(), name='buy'),
]
