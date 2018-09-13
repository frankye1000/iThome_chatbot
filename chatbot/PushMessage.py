from linebot.models import (
    TemplateSendMessage, URITemplateAction, CarouselTemplate, CarouselColumn)
from .crawl_ithome import crawl_ithome

# 因為carousel_template一次只能送5個tempalte
# =>[[(),(),(),(),()],[(),(),(),(),()]]
ithome_data = [crawl_ithome()[i:i+5] for i in range(0,len(crawl_ithome()),5)]

def carousel_template_message():

    All_carousel_template_message=[]
    if len(ithome_data)==0:
        return "NoNews"
    else:
        for data in ithome_data:

            carousel_template_message = TemplateSendMessage(
            alt_text='Carousel template',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url = data[0][3],
                        title=data[0][0],
                        text='想了解更多資訊\n請點擊『更多』',
                        actions=[
                            URITemplateAction(
                                label='更多',
                                uri = data[0][1]
                            )

                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url=data[1][3],
                        title=data[1][0],
                        text='想了解更多資訊\n請點擊『更多』',
                        actions=[
                            URITemplateAction(
                                label='更多',
                                uri=data[1][1]
                            )

                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url=data[2][3],
                        title=data[2][0],
                        text='想了解更多資訊\n請點擊『更多』',
                        actions=[
                            URITemplateAction(
                                label='更多',
                                uri=data[2][1]
                            )

                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url=data[3][3],
                        title=data[3][0],
                        text='想了解更多資訊\n請點擊『更多』',
                        actions=[
                            URITemplateAction(
                                label='更多',
                                uri=data[3][1]
                            )

                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url=data[4][3],
                        title=data[4][0],
                        text='想了解更多資訊\n請點擊『更多』',
                        actions=[
                            URITemplateAction(
                                label='更多',
                                uri=data[4][1]
                            )

                        ]
                    )

                ]))
            All_carousel_template_message.append(carousel_template_message)
    return All_carousel_template_message
