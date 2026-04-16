from django.shortcuts import redirect

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Список URL, доступных без авторизации
        public_urls = ['/login/', '/logout/', '/add_user/']
        
        # Проверяем, требует ли URL авторизации
        if not any(request.path.startswith(url) for url in public_urls):
            if 'user_id' not in request.session:
                return redirect('/login/')
        
        response = self.get_response(request)
        return response