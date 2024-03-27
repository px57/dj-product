from django.db import models

from gpm.models.base_metadata_model import BaseMetadataModel

from product.rules.stack import PRODUCT_RULESTACK

class Product(BaseMetadataModel):
    """
    A product that can be sold.

    Attributes:
        interface: The interface that the product belongs to.
        status: The status of the product.
        name: The name of the product.
        description: The description of the product.
        price: The price of the product.

    """
    interface = PRODUCT_RULESTACK.InterfaceField()

    uuid = models.CharField(
        max_length=255,
        unique=True,
        null=True,
        blank=True
    )

    profile = models.ForeignKey(
        'profiles.Profile', 
        on_delete=models.CASCADE,
        related_name='products',
        null=True,
        blank=True
    )

    status = models.CharField(
        max_length=255,
        choices=(
            ('draft', 'Draft'),
            ('active', 'Active'),
            ('inactive', 'Inactive'),
        ),
        default='draft'
    )

    name = models.CharField(
        max_length=255
    )

    description = models.TextField()
    
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2
    )

class ProductStock(BaseMetadataModel):
    """
    The stock of a product.

    Attributes:
        interface: The interface that the product stock belongs to.
        product: The product that the stock belongs to.
        stock: The amount of stock.
    """ 

    interface = PRODUCT_RULESTACK.InterfaceField()

    product = models.ForeignKey(
        Product, 
        on_delete=models.CASCADE
    )

    stock = models.IntegerField()

    unit = models.CharField(
        max_length=255,
        choices=(
            ('kg', 'Kilogram'),
            ('g', 'Gram'),
            ('l', 'Liter'),
            ('ml', 'Milliliter'),
            ('unit', 'Unit'),
        ),
        default='unit'
    )