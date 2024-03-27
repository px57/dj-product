from product.models import Product

from uuid import uuid4

def initproduct(_in):
    """
    Initialize a product.
    """
    dbProduct = Product(
        interface=_in.label,
        uuid=str(uuid4()),
        status='draft',
        name='New Product',
        description='New Product',
        price=0.0, 
    )
    dbProduct.save()
    return dbProduct
