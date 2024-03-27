

from product.rules.stack import PRODUCT_RULESTACK
from product.models import Product
from product.libs import initproduct

from gpm.http.decorators import load_response

@load_response(
    stack=PRODUCT_RULESTACK,
    json=True,
)
def init_product(
    request,
    res=None,
    _in=None,
    **kwargs,
):
    """
    Initialize a product, with default values.

    Args:
        request (Request): The request object.
        res (Response): The response object.
        _in (dict): The input data.
    """
    dbProduct = initproduct(_in)
    res.initialized = dbProduct.serialize(request)
    return res.success()

@load_response(
    stack=PRODUCT_RULESTACK,
)
def update_product(
    request, 
    res=None, 
    _in=None,
    **kwargs,
):
    """
    Update a product.
    """
    return res.success()