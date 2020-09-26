from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
from twilio.rest import Client

def base_url():
	return 'http://127.0.0.1:8000'

def myView(request):
	return render(request, "form.html", {"Name":" Septian","base_url":base_url()})

def sendMsg(request):
	account_sid =  #register on twillio
	auth_token = #register on twillio

	client = Client(account_sid, auth_token)

	vari = str(request.GET["message"])
	to = str('whatsapp:' + request.GET["number"])
	#to = str('whatsapp:+6289636868761')

	message = client.messages.create(
					body=vari,
					from_='whatsapp:+14155238886',
					to=to
				)
	return HttpResponse('You say '+ vari +' to '+ to + '----' + str(message.sid))