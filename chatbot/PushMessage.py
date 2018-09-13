from linebot.models import (
    TemplateSendMessage, URITemplateAction, CarouselTemplate, CarouselColumn)
from .crawl_ithome import crawl_ithome


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


def carousel_template_message():
    if len(crawl_ithome())==0:
        return "NoNews"
    else:
        # 因為carousel_template一次只能送5個tempalte
        # 例 : [[(),(),(),(),()],[(),(),()]]
        ithome_data = [crawl_ithome()[i:i+5] for i in range(0,len(crawl_ithome()),5)]

        ithome_data = [[carousel_column.createcolumn(d[3],d[0],d[1]) for d in data] for data in ithome_data]

        ithome_data = [TemplateSendMessage(alt_text='Carousel template', template=CarouselTemplate(columns=data)) for data in ithome_data]
        return ithome_data
