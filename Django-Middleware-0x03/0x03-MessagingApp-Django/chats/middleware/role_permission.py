class RolepermissionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            if request.user.role != 'admin' and request.user.role != 'moderator':
                return HttpResponse("You do not have permission to access this resource.", status=403)
        response = self.get_response(request)
        return response