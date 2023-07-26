from django.http import HttpResponseBadRequest

# request.is_ajax() fix 
def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

# our custom decorator
def ajax_required(f):
    def wrap(request, *args, **kwargs):
        if not is_ajax(request=request):
            return HttpResponseBadRequest('Bad Request')
        return f(request, *args, **kwargs)
    wrap.__doc__=f.__doc__
    wrap.__name__=f.__name__
    return wrap