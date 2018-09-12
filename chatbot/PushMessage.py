from linebot.models import (
    TemplateSendMessage, ButtonsTemplate,
    PostbackTemplateAction, MessageTemplateAction,
    URITemplateAction, DatetimePickerTemplateAction,
    ConfirmTemplate, CarouselTemplate, CarouselColumn
)
from .crawl_ithome import crawl_ithome

def carousel_template_message():
    carousel_template_message = TemplateSendMessage(
    alt_text='Carousel template',
    template=CarouselTemplate(
        columns=[
            CarouselColumn(
                thumbnail_image_url = crawl_ithome[0][3],
                title=crawl_ithome[0][0],
                text='想了解更多資訊\n請點擊『更多』',
                actions=[
                    PostbackTemplateAction(
                        label='日期',
                        data=crawl_ithome[0][2]
                    ),
                    URITemplateAction(
                        label='更多',
                        uri = crawl_ithome[0][1]
                    )

                ]
            ),
            CarouselColumn(
                thumbnail_image_url=crawl_ithome[1][3],
                title=crawl_ithome[1][0],
                text='想了解更多資訊\n請點擊『更多』',
                actions=[
                    PostbackTemplateAction(
                        label='日期',
                        data=crawl_ithome[1][2]
                    ),
                    URITemplateAction(
                        label='更多',
                        uri=crawl_ithome[1][1]
                    )

                ]
            ),
            CarouselColumn(
                thumbnail_image_url=crawl_ithome[2][3],
                title=crawl_ithome[2][0],
                text='想了解更多資訊\n請點擊『更多』',
                actions=[
                    PostbackTemplateAction(
                        label='日期',
                        data=crawl_ithome[2][2]
                    ),
                    URITemplateAction(
                        label='更多',
                        uri=crawl_ithome[2][1]
                    )

                ]
            ),
            CarouselColumn(
                thumbnail_image_url=crawl_ithome[3][3],
                title=crawl_ithome[3][0],
                text='想了解更多資訊\n請點擊『更多』',
                actions=[
                    PostbackTemplateAction(
                        label='日期',
                        data=crawl_ithome[3][2]
                    ),
                    URITemplateAction(
                        label='更多',
                        uri=crawl_ithome[3][1]
                    )

                ]
            ),
            CarouselColumn(
                thumbnail_image_url=crawl_ithome[4][3],
                title=crawl_ithome[4][0],
                text='想了解更多資訊\n請點擊『更多』',
                actions=[
                    PostbackTemplateAction(
                        label='日期',
                        data=crawl_ithome[4][2]
                    ),
                    URITemplateAction(
                        label='更多',
                        uri=crawl_ithome[4][1]
                    )

                ]
            )






        ]))
    return carousel_template_message