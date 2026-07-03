from django.urls import path
from .views import CustomerAPIView

urlpatterns = [
    # For GET all and POST
    path('customers/', CustomerAPIView.as_view(), name='customers-list'),
    
    # For GET one, PUT, and DELETE (Requires the Primary Key ID)
    path('customers/<int:customer_id>/', CustomerAPIView.as_view(), name='customer-detail'),
]