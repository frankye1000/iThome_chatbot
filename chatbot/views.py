from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, FollowEvent,TemplateSendMessage,StickerSendMessage,PostbackEvent,TextSendMessage


from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job

scheduler = BackgroundScheduler()
scheduler.add_jobstore(DjangoJobStore(), "default")

scheduler.start()
p="t"
def time_task(p):
    print("I'm a test job!")

scheduler.add_job(time_task, "cron", second=2, args=p)
register_events(scheduler)



# Create your views here.
handler = WebhookHandler('fe1c60309296f35f05cfb0001f06a672')
line_bot_api = LineBotApi('t6f/vtOEI0ww+O8zMW6alZtHq+3rhCmnb7vwin/IzFhKWSVg95r/XxJG4kWkk35cq42RgrzjxV63j2KmLZfMvTG36aE5+i3aqkrCraRbODVZrVtwZlgRp9QUqQ7ootIWqsabKGhrVC0pHEdIF5hq2wdB04t89/1O/w1cDnyilFU=')


@csrf_exempt
def callback(request):
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')

        try:
            handler.handle(body, signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()
        return HttpResponse()
    else:
        return HttpResponseBadRequest()


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # print(event)
    # response(event)
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text="您好，\n歡迎使用iThome聊天機器人"))

# @handler.add(PostbackEvent)
# def handle_postback_message(event):
#     postback(event)
#
@handler.add(FollowEvent)
def handle_follow_event(event):
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text="您好，\n歡迎使用iThome聊天機器人"))
    line_bot_api.push_message(event.source.user_id, StickerSendMessage(package_id='1', sticker_id='13'))
    line_bot_api.push_message(event.source.user_id,
                               TextSendMessage(text="每日接收最新的iThome資訊"))
    line_bot_api.push_message(event.source.user_id,
                               TextSendMessage(text="每日晚上六點準時更新"))
