from django.views.decorators.csrf import csrf_exempt
from django.template.loader import get_template
from django.template import Template, Context
from django.http import HttpResponse
 
def update(request):
    if request.is_ajax():
        message = "Yes, AJAX!"
		#startpoint = request.GET
    else:
        message = "Not Ajax"

    return HttpResponse(message)

def index(request):
	routeName = 'First Route'
	t = get_template('route/routes_list.html')
	html = t.render(Context({'routeName': routeName}))
	return HttpResponse(html)