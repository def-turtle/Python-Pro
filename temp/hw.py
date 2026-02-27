def handle_status(code):
    match code:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Server Error"
        case _:
            return "Unknown status"
print(handle_status(200))  # Output: OK
print(handle_status(404))  # Output: Not Found