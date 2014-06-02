from django.shortcuts import render_to_response

# Create your views here.
def index(request, session_id):
	return render_to_response('session/index.html', {
			'session_id': session_id
		})