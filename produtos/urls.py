from django.urls import path
from produtos.views import (
    ProductListView,
    ProductLandingPageView,
    SuccessView,
    CancelView,
    stripe_webhook,
    StripeIntentView,
    CreateCheckoutSessionView,
)

app_name = 'produtos'

urlpatterns = [
    path('product-list', ProductListView.as_view(), name='product-list'),
    path('webhooks/stripe/', stripe_webhook, name='stripe-webhook'),
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('success/', SuccessView.as_view(), name='success'),
    path('landing-page/<int:pk>/', ProductLandingPageView.as_view(), name='landing-page'),
    path('create-checkout-session/<int:pk>/', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
    path('create-payment-intent/<int:pk>/', StripeIntentView.as_view(), name='create-payment-intent'),
    # Adicionando rota para a função redirectToProduct
    path('redirect-to-product/<int:product_id>/', ProductListView.redirectToProduct, name='redirect-to-product'),
]
