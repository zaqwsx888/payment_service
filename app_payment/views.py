import os
import stripe
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.views import View
from django.views.generic import DetailView
from app_payment.models import Item
from stripe.error import InvalidRequestError

stripe.api_key = os.environ.get('STRIPE_API_KEY')


class ItemDetailView(DetailView):
    """Представление отображающее информацию о товаре с возможностью покупки"""
    model = Item
    template_name = 'app_payment/item.html'
    pk_url_kwarg = 'item_pk'
    context_object_name = 'item'


class BuyView(View):
    """Представление для получения Stripe session id"""
    def get(self, request, *args, **kwargs):
        item_pk = self.kwargs.get('item_pk')
        try:
            item = Item.objects.get(pk=item_pk)
            session = stripe.checkout.Session.create(
                line_items=[{
                    'price_data': {
                        'currency': 'rub',
                        'product_data': {'name': item.name, },
                        'unit_amount': int(item.price * 100),
                    },
                    'quantity': 1,
                }],
                mode='payment',
                success_url=request.META['HTTP_REFERER'],
                cancel_url=request.META['HTTP_REFERER'],
            )
            return JsonResponse({'sessionId': session.id})
        except (ObjectDoesNotExist, InvalidRequestError, ) as error:
            return JsonResponse({'error': str(error)})
