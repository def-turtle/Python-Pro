
import time

class CustomMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start = time.time()
        request.custom_attribute = 'This is a custom attribute added by middleware'
        response = self.get_response(request)
        end = time.time()
        print(f"Request duration: {end - start}")
        return response
