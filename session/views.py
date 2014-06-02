from django.shortcuts import render_to_response
from session.models import *

# Create your views here.
def index(request, session_id):
	session = Session.objects.get(id=session_id)

	return render_to_response('session/index.html', {
			'session_id': session_id,
			'session': session
		})