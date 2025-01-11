from datetime import datetime, timedelta
from django.http import HttpResponse

class OffensiveLanguageMiddleware:

    messages_by_ip = {}

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        """Track number of chat messages sent by each ip address and implement a time based limit"""
        ip_address = request.META.get('REMOTE_ADDR')
        current_time = datetime.now()
        time_limit = current_time - timedelta(minutes=1)

        if ip_address:
            if ip_address not in self.messages_by_ip or self.messages_by_ip[ip_address]["time"] < time_limit:
                self.messages_by_ip[ip_address] = {"count": 0, "time": current_time}
            
            self.messages_by_ip[ip_address]["count"] += 1

            if self.messages_by_ip[ip_address]["count"] > 5:
                return HttpResponse("You have exceeded the per minute limit of messages sent. Please wait a few minutes before trying again.")

        return self.get_response(request)