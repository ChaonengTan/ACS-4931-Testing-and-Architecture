# Adapted from a Java code in the "Refactoring" book by Martin Fowler.

# TODO: Replace temporary variable with extracted method/query
def getBasePrice():
    return quantity * item_price
# Code snippet. Not runnable.
def get_price():
    base_price = getBasePrice()
    discount_factor = 0
    if base_price > 1000:
        discount_factor = 0.95
    else:
        discount_factor = 0.98
    return base_price * discount_factor
