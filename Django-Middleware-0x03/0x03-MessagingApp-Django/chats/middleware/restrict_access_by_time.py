from datetime import datetime
from django.http import HttpResponse

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