import streamlit as st
from bot.client import get_client
from bot.orders import place_order

st.title("📈 Trading Bot UI")

symbol = st.text_input("Symbol", "BTCUSDT")
side = st.selectbox("Side", ["BUY", "SELL"])
order_type = st.selectbox("Order Type", ["MARKET", "LIMIT"])

quantity = st.number_input("Quantity", min_value=0.0001)

price = None
if order_type == "LIMIT":
    price = st.number_input("Price", min_value=1.0)

if st.button("Place Order"):
    client = get_client()
    order = place_order(client, symbol, side, order_type, quantity, price)
    st.success(f"Order placed! ID: {order.get('orderId')}")