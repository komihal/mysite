import datetime

class LogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print(f"[{datetime.datetime.now()}] {request.method} {request.path}")  # Логируем запрос
        response = self.get_response(request)
        return response