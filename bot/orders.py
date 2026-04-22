import logging

def place_order(client, symbol, side, order_type, quantity, price=None, stop_price=None):
    try:
        logging.info(f"Placing {order_type} order: {side} {quantity} {symbol}")

        if order_type == "MARKET":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )

        elif order_type == "LIMIT":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

        elif order_type == "STOP_LIMIT":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="STOP",
                quantity=quantity,
                price=price,
                stopPrice=stop_price,
                timeInForce="GTC"
            )

        else:
            raise ValueError("Invalid order type")

        logging.info(f"Order Response: {order}")
        return order

    except Exception as e:
        logging.error(f"Error placing order: {str(e)}")
        raise