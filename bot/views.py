from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from json import JSONEncoder
from requests import post , get
# Create your views here.

bot_token = 'YOUR_TOKEN'


def send_text(chat_id,uesr_text,if_text,data_text):
    if uesr_text == if_text:
        my_data = {
            'chat_id' : int(chat_id) ,
            'type' : 'text' ,
            'data' : str(data_text),
            'form': None,
            'reply_keyboard': None,
            'inline_keyboard':None,
            }
        post("https://api.gap.im/sendMessage",data=my_data,headers={'token' : bot_token})


def send_request(chat_id,text):
    send_text(chat_id,text,"Hello","Hello my friend.")
    

@csrf_exempt
def reqst(this_equest):
    try:
        chat_id = this_equest.POST['chat_id']
        this_type = this_equest.POST['type']
        try:
            text = this_equest.POST['data']
            send_request(chat_id,text)
        except:
            pass
        return JsonResponse({"status":"ok"},JSONEncoder)
    except:
        pass
    