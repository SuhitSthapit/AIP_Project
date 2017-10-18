from django.shortcuts import render
from django.conf import settings
from django.shortcuts import render, HttpResponse

import requests
import json
from .forms import SubmitGithubUser
#from .serializers import SavedGithubUserSerializer


def save_githubUser(request):

	if request.method == "POST":
		form = SubmitGithubUser(request.POST)
		if form.is_valid():
			user = form.cleaned_data['name']
			req = requests.get('https://api.github.com/users/' + user)
			jsonList = []
			jsonList.append(json.loads(req.content))
			parsedData = []
			userData = {}
			for data in jsonList:
				userData['name'] = data['name']
				userData['blog'] = data['blog']
				userData['email'] = data['email']
				userData['public_gists'] = data['public_gists']
				userData['public_repos'] = data['public_repos']
				userData['avatar_url'] = data['avatar_url']
				userData['followers'] = data['followers']
				userData['following'] = data['following']
			parsedData.append(userData)
			return render(request, 'githubapi/githubuser.html', {'userData': userData})
			#return HttpResponse(parsedData)
	else:
		form = SubmitGithubUser()

	return render(request, 'githubapi/form.html', {'form': form})





