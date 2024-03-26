

from product.rules.stack import PRODUCT_RULESTACK
from product.models import Product

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
    Initialize a product.
    """
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