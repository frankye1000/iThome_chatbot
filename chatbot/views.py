from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from linebot.exceptions import LineBotApiError
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, FollowEvent,StickerMessage,StickerSendMessage,TextSendMessage
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events
from linebot.models import (
    TemplateSendMessage, URITemplateAction, CarouselTemplate, CarouselColumn)
from .crawl_ithome import crawl_ithome
scheduler = BackgroundScheduler()
scheduler.add_jobstore(DjangoJobStore(), "default")
scheduler.start()


# Create your views here.
handler = WebhookHandler('654321')
line_bot_api = LineBotApi('123456789')


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

# 創一個class 可以依照不同資料數量創造不一樣長度的carousel_template
class carousel_column():
    def createcolumn(photo,title,url):
        c = CarouselColumn(
                                thumbnail_image_url = photo,
                                title=title,
                                text='想了解更多資訊\n請點擊『更多』',
                                actions=[
                                    URITemplateAction(
                                        label='更多',
                                        uri=url)])

        return c

## 整理傳送資料
def carousel_template_message():
    ithome = crawl_ithome()
    if len(ithome)==0:
        return "NoNews"
    else:
        # 因為carousel_template一次只能送5個tempalte
        # 例 : [[(),(),(),(),()],[(),(),()]]

        ithome_data = [ithome[i:i+5] for i in range(0,len(ithome),5)]

        ithome_data = [[carousel_column.createcolumn(d[3],d[0],d[1]) for d in data] for data in ithome_data]

        ithome_data = [TemplateSendMessage(alt_text='Carousel template', template=CarouselTemplate(columns=data)) for data in ithome_data]
        #[{},{},{}]
        return ithome_data





## 每天的排程
p="t"
def push_message(p):
    carousel_template = carousel_template_message()
    user_id="<user_id>"
    if carousel_template=="NoNews":
        line_bot_api.push_message(user_id, TextSendMessage(text="沒有最新新聞"))
    else:

        for template in carousel_template:
            line_bot_api.push_message( user_id, template)

scheduler.add_job(push_message , "interval", hours=12, args=p) #12小時更新一次
register_events(scheduler)


@handler.add(MessageEvent, message=StickerMessage)
def handle_message(event):
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text="您好，\n歡迎使用iThome聊天機器人"))
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text="您好，\n歡迎使用iThome聊天機器人"))
@handler.add(FollowEvent)
def handle_follow_event(event):
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text="您好，\n歡迎使用iThome聊天機器人"))
    line_bot_api.push_message(event.source.user_id, StickerSendMessage(package_id='1', sticker_id='13'))
    line_bot_api.push_message(event.source.user_id,
                               TextSendMessage(text="每日接收最新的iThome資訊"))

