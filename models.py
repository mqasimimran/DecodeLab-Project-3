from django.db import models

class Customer(models.Model):
    # NOT NULL is enforced by default in Django unless null=True is set.
    # UNIQUE enforces distinctness to prevent duplicates.
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True) 
    created_at = models.DateTimeField(auto_now_add=True)

    def to_dict(self):
        return {
            "id": self.id, # Primary Key generated automatically
            "name": self.name,
            "email": self.email
        }

class Order(models.Model):
    # Foreign Key establishes the 1:Many relational geometry
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    item_name = models.CharField(max_length=200)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def to_dict(self):
        return {
            "id": self.id,
            "customer_id": self.customer.id,
            "item_name": self.item_name,
            "total_price": str(self.total_price)
        }