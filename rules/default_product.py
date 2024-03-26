

from django.utils import timezone
import os
from notification.rules.stack import PRODUCT_RULESTACK
from gpm.interfaces.interfaces import InterfaceManager
import PIL

class DefaultRuleClass(InterfaceManager):
    """
    The default rule class. 
    """

    """
    The label to identify the rule interface.
    """
    label = 'DEFAULT'

    """
    The allow flag to enable or disable the rule.
    """
    allow = True


