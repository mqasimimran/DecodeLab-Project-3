
import json
from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import Customer

@method_decorator(csrf_exempt, name='dispatch')
class CustomerAPIView(View):
    
    # READ = HTTP GET = SQL SELECT
    def get(self, request, customer_id=None):
        if customer_id:
            try:
                customer = Customer.objects.get(id=customer_id)
                return JsonResponse({"status": "success", "data": customer.to_dict()}, status=200)
            except Customer.DoesNotExist:
                return JsonResponse({"error": "Not Found"}, status=404)
        else:
            customers = [c.to_dict() for c in Customer.objects.all()]
            return JsonResponse({"status": "success", "data": customers}, status=200)

    # CREATE = HTTP POST = SQL INSERT
    def post(self, request):
        try:
            body = json.loads(request.body)
            # The Gatekeeper: Basic Validation
            if not body.get('name') or not body.get('email'):
                return JsonResponse({"error": "Bad Request", "message": "Name and email required."}, status=400)
            
            new_customer = Customer.objects.create(
                name=body['name'], 
                email=body['email']
            )
            return JsonResponse({"status": "success", "data": new_customer.to_dict()}, status=201)
        except Exception as e:
            return JsonResponse({"error": "Internal Error", "message": str(e)}, status=500)

    # UPDATE = HTTP PUT = SQL UPDATE
    def put(self, request, customer_id):
        try:
            customer = Customer.objects.get(id=customer_id)
            body = json.loads(request.body)
            
            # Update fields if provided
            customer.name = body.get('name', customer.name)
            customer.email = body.get('email', customer.email)
            customer.save()
            
            return JsonResponse({"status": "success", "data": customer.to_dict()}, status=200)
        except Customer.DoesNotExist:
            return JsonResponse({"error": "Not Found"}, status=404)

    # DELETE = HTTP DELETE = SQL DELETE
    def delete(self, request, customer_id):
        try:
            customer = Customer.objects.get(id=customer_id)
            customer.delete()
            # 204 No Content is the standard status for a successful deletion
            return JsonResponse({"status": "success", "message": "Customer deleted."}, status=204)
        except Customer.DoesNotExist:
            return JsonResponse({"error": "Not Found"}, status=404)