#This is my views.py file
from django.shortcuts import render

# Create your views here.
def home(request):
	import json
	import requests

	api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=E5FF4825-2584-4D26-8910-6EE7A9587146")
	
	try:
		api = json.loads(api_request.content)
	except Exception as e:
		api = "Error..."
	return render(request, 'home.html', {'api': api})
def about(request):
	return render(request, 'about.html', {})