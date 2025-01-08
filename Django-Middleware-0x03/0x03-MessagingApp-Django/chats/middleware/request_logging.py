from django.conf import settings
from datetime import datetime

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        """Logs each request and the user that made it"""

        file_path = f"{settings.BASE_DIR}/requests.log"
        user = request.user

        with open(file_path, "a") as f:
            f.write(f"{datetime.now()} - User: {user} - Path: {request.path}\n")

        response = self.get_response(request)
        return response