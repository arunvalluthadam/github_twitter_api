from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.context_processors import csrf
import json
import requests
import oauth2

# Create your views here.
# def home(request):
# 	context = {'tweets': getTweets()}
# 	return render_to_response('index.html', context, context_instance=RequestContext(request))

def home(request):
	variables = {}
	variables.update(csrf(request))

	return render_to_response('index.html', variables)



def twitter_ajax(request):
	key = "vkAydo4HpELnLFObprDmSKl1w"
	secret = "by1IeYsc03F03qMJmx3qvwb5RbMAhAZ2RH75lQdsdY40GrfBzl"
	access = "2920577258-bj9sVQInJsr1t9pIP43PPP0KsNglx4xbXrCJBid"
	asecret = "bJBi7uKIDnJNayQNPJ3JDzbVWwKdlw1e5SDezg4IPA1F1"

	consumer = oauth2.Consumer(key=key, secret=secret)
	token = oauth2.Token(key=access, secret=asecret)
	client = oauth2.Client(consumer, token)
	# time1 = "https://api.twitter.com/1.1/statuses/home_timeline.json"
	if request.method == "POST":
		twitter_user = request.POST['twitter_text']
	else:
		twitter_user = "arun_zorse"
	time1 = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name="+ twitter_user +"&count=2"
	response, data = client.request(time1)
	tw = json.loads(data)
	print tw
	tweets = json.dumps(tw, sort_keys=True, indent=4)

	file = open("twitter_api.json", "w")
	file.write(tweets)
	file.close()
	print "data writed"

	file = open("twitter_api.json", "r")
	tweets = file.read()
	load = json.loads(tweets)
	outer_dict = []
	for i in load:
		a = i["user"]
		name = a["name"]
		text = i["text"]
		date = i["created_at"]
		inner_dict = {}
		inner_dict.update({"name": name, "text": text, "date": date})
		print inner_dict
		outer_dict.append(inner_dict)

	variables = RequestContext(request, {
		'outer_dict': outer_dict,
	})
	return render_to_response('twitter_ajax.html', variables)


def github_ajax(request):
	API_TOKEN='265890eb2870b000014a9a7c4dab504f6d961e44'

	if request.method == "POST":
		github_user = request.POST['github_text']
	else:
		github_user = "arunvalluthadam"

	URL = "https://api.github.com/users/" + github_user + "/repos"

	fields = "id"
	limit = 4

	url = URL + "?access_token=" + API_TOKEN

	r = requests.get(url).json()
	# print r
	tweets = json.dumps(r, sort_keys=True, indent=4)
	# print tweets

	file = open("github_api.json", "w")
	file.write(tweets)
	file.close()
	print "data writed"



	file = open("github_api.json", "r")
	tweets = file.read()
	load = json.loads(tweets)
	github_dict = []
	for i in load:
		name = i["name"]
		text = i["description"]
		clone_url = i["clone_url"]
		date = i["created_at"]
		inner_dict = {}
		inner_dict.update({"name": name, "text": text, "clone_url": clone_url, "date": date})
		print inner_dict
		github_dict.append(inner_dict)


	variables = RequestContext(request, {
		'github_dict': github_dict,
	})
	return render_to_response('github_ajax.html', variables)