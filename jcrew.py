#!/usr/bin/env python
#
# A Zapier trigger to monitor J.Crew product availability
# https://github.com/jacobbudin/zapier-jcrew-trigger


product_id = '85231' # Nike Killshot 2
size = '13 MEDIUM'   # Size, as text, shown on product page
color = None         # If only one color, this is optional


import requests


def get_product_sku(product_id, size, color=None):
    """Get product's SKU
    
    Args:
        product_id (str): J.Crew's product ID (as found in the product URL)
        size (str): The product size, exactly as it appears on the product page
        color (str): The product color
    
    Returns:
        str: J.Crew SKU for the specific color and size of a product
    
    Raises:
        Exception: The provided arguments are do not correspond to an SKU
    """

    product = requests.get('https://www.jcrew.com/data/v1/US/products/%s' % product_id)
    product.raise_for_status()
    product_json = product.json()

    # Check size exists
    if size not in product_json['sizesList']:
        raise Exception("Not a valid size; valid sizes are: %s", ', '.join(product_json['sizesList']))
    
    # Select default color
    if color is None and len(product_json['colorsList']) == 1:
        color = product_json['defaultColorCode']

    # Check color exists
    if color not in product_json['colorsMap'].keys():
        raise Exception("Not a valid color; valid colors are: %s", ', '.join(product_json['colorsMap'].keys()))
    
    return product_json['sizesMap'][size][color]


def get_product_availability(product_id, sku):
    """Get product's availability
    
    Args:
        product_id (str): J.Crew's product ID (as found in the product URL)
        sku (str): J.Crew's SKU for the specific color and size of a product
        
    Returns:
        bool: Whether SKU is in stock
        
    Raises:
        Exception: The availability couldn't be determined
    """

    inventory = requests.get('https://www.jcrew.com/data/v1/US/products/inventory/%s' % product_id)
    inventory.raise_for_status()
    inventory_json = inventory.json()

    product = inventory_json['inventory'][sku]

    if 'inStock' in product:
        return product['inStock']

    if 'quantity' in product:
        return bool(product['quantity'])

    raise Exception("Could not find `inStock` or `quantity` keys")


sku = get_product_sku(product_id, size, color)
is_available = get_product_availability(product_id, sku)
output = {'is_available': is_available}
