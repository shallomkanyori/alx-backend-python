from django.conf import settings
from datetime import datetime, timedelta
from django.http import HttpResponse

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

class RestrictAccessByTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        """Restricts access to the API to only be available between 9am and 6pm"""
        current_time = datetime.now()
        if current_time.hour < 9 or current_time.hour > 18:
            return HttpResponse("Sorry, this service is only available between 9am and 6pm.", status=403)
        
        response = self.get_response(request)
        return response

class OffensiveLanguageMiddleware:

    messages_by_ip = {}

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        """Track number of chat messages sent by each ip address and implement a time based limit"""
        ip_address = request.META.get('REMOTE_ADDR')
        current_time = datetime.now()
        time_limit = current_time - timedelta(minutes=1)

        if request.method != "POST":
            return self.get_response(request)

        if ip_address:
            if ip_address not in self.messages_by_ip or self.messages_by_ip[ip_address]["time"] < time_limit:
                self.messages_by_ip[ip_address] = {"count": 0, "time": current_time}
            
            self.messages_by_ip[ip_address]["count"] += 1

            if self.messages_by_ip[ip_address]["count"] > 5:
                return HttpResponse("You have exceeded the per minute limit of messages sent. Please wait a few minutes before trying again.")

        return self.get_response(request)

class RolepermissionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            if request.user.role != 'admin' and request.user.role != 'moderator':
                return HttpResponse("You do not have permission to access this resource.", status=403)
        response = self.get_response(request)
        return response