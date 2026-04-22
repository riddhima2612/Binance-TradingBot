def validate_side(side):
    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")

def validate_order_type(order_type):
    if order_type not in ["MARKET", "LIMIT", "STOP_LIMIT"]:
        raise ValueError("Order type must be MARKET, LIMIT, or STOP_LIMIT")

def validate_price(order_type, price, stop_price):
    if order_type == "LIMIT" and price is None:
        raise ValueError("Price required for LIMIT orders")

    if order_type == "STOP_LIMIT":
        if price is None or stop_price is None:
            raise ValueError("Both price and stop_price required for STOP_LIMIT")