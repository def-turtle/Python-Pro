from tasks import process_order, say_hello

result = say_hello.delay("Andrew")
result1 = process_order.delay(1, "test@email.com")
print("Task sent:", result.id)
print("Task sent:", result1.id)