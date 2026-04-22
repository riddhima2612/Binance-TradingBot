from bot.client import get_client
from bot.orders import place_order
from bot.validators import *
from bot.logging_config import setup_logger

setup_logger()

print(" Binance Futures Trading Bot\n")

while True:
    symbol = input("Enter symbol (e.g. BTCUSDT): ").upper()
    if symbol:
        break
    print(" Symbol cannot be empty")

while True:
    side = input("Enter side (BUY/SELL): ").upper()
    if side in ["BUY", "SELL"]:
        break
    print(" Invalid side")


while True:
    order_type = input("Enter type (MARKET/LIMIT/STOP_LIMIT): ").upper()
    if order_type in ["MARKET", "LIMIT", "STOP_LIMIT"]:
        break
    print(" Invalid type")


while True:
    try:
        quantity = float(input("Enter quantity: "))
        if quantity > 0:
            break
        print(" Quantity must be > 0")
    except:
        print(" Invalid number")

price = None
stop_price = None


if order_type == "LIMIT":
    price = float(input("Enter price: "))

elif order_type == "STOP_LIMIT":
    price = float(input("Enter LIMIT price: "))
    stop_price = float(input("Enter STOP price: "))


try:
    validate_side(side)
    validate_order_type(order_type)
    validate_price(order_type, price, stop_price)

    print("\n Order Summary")
    print(f"Symbol: {symbol}")
    print(f"Side: {side}")
    print(f"Type: {order_type}")
    print(f"Quantity: {quantity}")
    if price:
        print(f"Price: {price}")
    if stop_price:
        print(f"Stop Price: {stop_price}")

    confirm = input("\nProceed? (yes/no): ").lower()
    if confirm != "yes":
        print(" Cancelled")
        exit()

    client = get_client()

    order = place_order(
        client,
        symbol,
        side,
        order_type,
        quantity,
        price,
        stop_price
    )

    print("\n ORDER SUCCESS")
    print("Order ID:", order.get("orderId"))
    print("Status:", order.get("status"))
    print("Executed Qty:", order.get("executedQty"))
    print("Avg Price:", order.get("avgPrice"))

except Exception as e:
    print("\n ERROR:", e)