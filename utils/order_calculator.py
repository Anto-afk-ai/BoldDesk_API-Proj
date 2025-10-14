from typing import Dict, List, Optional
from const.config import ITEMS

def find_item_by_id(item_id: str) -> Optional[Dict]:
    """Find an item in the ITEMS list by its ID"""
    return next((item for item in ITEMS if item['id'] == item_id), None)

def find_item_by_name(name: str) -> Optional[Dict]:
    """Find an item in ITEMS whose name contains the given string (case-insensitive)."""
    if not name:
        return None
    q = name.strip().lower()
    return next(
        (item for item in ITEMS if q in item.get("name", "").strip().lower()),
        None
    )

def get_bulk_discount(item: Dict, quantity: int) -> float:
    """
    Get the applicable bulk discount percentage for the given quantity
    Returns the highest applicable discount
    """
    if not item or 'bulk_options' not in item:
        return 0.0
    
    applicable_discounts = [
        option['discount'] 
        for option in item['bulk_options'] 
        if quantity >= option['quantity']
    ]
    
    return max(applicable_discounts) if applicable_discounts else 0.0

def calculate_order_total(items: List[Dict[str, int]]) -> Dict:
    """
    Calculate the total cost of an order including bulk discounts
    
    Args:
        items: List of dicts with {'item_id': str, 'quantity': int}
        
    Returns:
        Dict containing:
        - subtotal (before discounts)
        - total_discount
        - final_total
        - items_detail (with individual calculations)
        - bulk_savings
    """
    subtotal = 0.0
    total_discount = 0.0
    items_detail = []
    bulk_savings = []

    for order_item in items:
        item_id = order_item.get('item_id')
        quantity = order_item.get('quantity', 0)
        
        if not item_id or quantity <= 0:
            continue
            
        item = find_item_by_name(str(item_id))
        if not item:
            continue
            
        # Calculate item subtotal before discount
        item_subtotal = item['price'] * quantity
        
        # Get applicable bulk discount
        discount_percent = get_bulk_discount(item, quantity)
        discount_amount = (item_subtotal * discount_percent / 100)
        
        # Calculate final amount for this item
        final_amount = item_subtotal - discount_amount
        
        # Add to running totals
        subtotal += item_subtotal
        total_discount += discount_amount
        
        # Add detailed item calculation
        items_detail.append({
            'item_id': item_id,
            'name': item['name'],
            'quantity': quantity,
            'unit_price': item['price'],
            'subtotal': item_subtotal,
            'discount_percent': discount_percent,
            'discount_amount': discount_amount,
            'final_amount': final_amount
        })
        
        # If there was a bulk discount, add to savings summary
        if discount_amount > 0:
            bulk_savings.append({
                'item_name': item['name'],
                'quantity': quantity,
                'discount_percent': discount_percent,
                'savings': discount_amount
            })

    final_total = subtotal - total_discount
    
    return {
        'subtotal': round(subtotal, 2),
        'total_discount': round(total_discount, 2),
        'final_total': round(final_total, 2),
        'items_detail': items_detail,
        'bulk_savings': bulk_savings
    }

def get_bulk_order_quote(items: List[Dict[str, int]]) -> Dict:
    """
    Generate a detailed quote for bulk orders
    
    Args:
        items: List of dicts with {'item_id': str, 'quantity': int}
        
    Returns:
        Dict containing the quote details and savings summary
    """
    calculation = calculate_order_total(items)
    
    # Format the response with a clear savings breakdown
    quote_response = {
        'quote_summary': {
            'original_total': calculation['subtotal'],
            'total_savings': calculation['total_discount'],
            'final_total': calculation['final_total']
        },
        'items_breakdown': calculation['items_detail'],
        'bulk_savings_summary': calculation['bulk_savings']
    }
    
    return quote_response