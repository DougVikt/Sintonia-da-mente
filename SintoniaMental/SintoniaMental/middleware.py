from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin


class AuthenticationMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path == '/':
            if request.user.is_authenticated:
                if hasattr(request.user, 'patients'):
                    return redirect('home_user', id=request.user.id, month=1, year=1)
                elif hasattr(request.user, 'professionals'):
                    return redirect('home_specialist', id=request.user.id)
            else:
                return None