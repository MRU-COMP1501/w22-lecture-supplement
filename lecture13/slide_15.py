need_more_coffee = False
is_morning = True
still_sleeping = False

# Default order of operations: first not, then and, then or.
# You can use brackets to change or clarify the order.
order_1 = not need_more_coffee or is_morning and still_sleeping
order_2 = (not need_more_coffee or is_morning) and still_sleeping
order_3 = (not need_more_coffee) or (is_morning and still_sleeping)

print('Order 1:', order_1)
print('Order 2:', order_2)
print('Order 3:', order_3)