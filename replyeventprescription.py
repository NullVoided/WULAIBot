import os

from linebot.models.events import VideoPlayCompleteEvent

if os.getenv('DEVELOPMENT') is not None:
    from dotenv import load_dotenv

    load_dotenv(dotenv_path='../.env')

import sys

from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, FlexSendMessage, LocationSendMessage,
    VideoSendMessage, ImageSendMessage, StickerSendMessage,
)

app = Flask(__name__)

# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv('LINE_CHANNEL_SECRET') or 'YOUR_SECRET'
channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN') or 'YOUR_ACCESS_TOKEN'
if channel_secret is None:
    print('Specify LINE_CHANNEL_SECRET as environment variable.')
    sys.exit(1)
if channel_access_token is None:
    print('Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.')
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def message_text(event):
    message = event.message.text
    if message == 'Check Prescription':
        output = FlexSendMessage(
            alt_text='hello',
            contents={
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "nano",
      "header": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "Medicine 1",
            "color": "#ffffff",
            "align": "start",
            "size": "md",
            "gravity": "center"
          },
          {
            "type": "text",
            "text": "70%",
            "color": "#ffffff",
            "align": "start",
            "size": "xs",
            "gravity": "center",
            "margin": "lg"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "filler"
                  }
                ],
                "width": "70%",
                "backgroundColor": "#0D8186",
                "height": "6px"
              }
            ],
            "backgroundColor": "#9FD8E36E",
            "height": "6px",
            "margin": "sm"
          }
        ],
        "backgroundColor": "#27ACB2",
        "paddingTop": "19px",
        "paddingAll": "12px",
        "paddingBottom": "16px"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "1 capsule after meals",
                "color": "#8C8C8C",
                "size": "sm",
                "wrap": true
              }
            ],
            "flex": 1
          }
        ],
        "spacing": "md",
        "paddingAll": "12px"
      },
      "styles": {
        "footer": {
          "separator": false
        }
      }
    },
    {
      "type": "bubble",
      "size": "nano",
      "header": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "Medicine 2",
            "color": "#ffffff",
            "align": "start",
            "size": "md",
            "gravity": "center"
          },
          {
            "type": "text",
            "text": "30%",
            "color": "#ffffff",
            "align": "start",
            "size": "xs",
            "gravity": "center",
            "margin": "lg"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "filler"
                  }
                ],
                "width": "30%",
                "backgroundColor": "#DE5658",
                "height": "6px"
              }
            ],
            "backgroundColor": "#FAD2A76E",
            "height": "6px",
            "margin": "sm"
          }
        ],
        "backgroundColor": "#FF6B6E",
        "paddingTop": "19px",
        "paddingAll": "12px",
        "paddingBottom": "16px"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "1 tablet before sleeping",
                "color": "#8C8C8C",
                "size": "sm",
                "wrap": true
              }
            ],
            "flex": 1
          }
        ],
        "spacing": "md",
        "paddingAll": "12px"
      },
      "styles": {
        "footer": {
          "separator": false
        }
      }
    },
    {
      "type": "bubble",
      "size": "nano",
      "header": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "Medicine 2",
            "color": "#ffffff",
            "align": "start",
            "size": "md",
            "gravity": "center"
          },
          {
            "type": "text",
            "text": "100%",
            "color": "#ffffff",
            "align": "start",
            "size": "xs",
            "gravity": "center",
            "margin": "lg"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "filler"
                  }
                ],
                "width": "100%",
                "backgroundColor": "#7D51E4",
                "height": "6px"
              }
            ],
            "backgroundColor": "#9FD8E36E",
            "height": "6px",
            "margin": "sm"
          }
        ],
        "backgroundColor": "#A17DF5",
        "paddingTop": "19px",
        "paddingAll": "12px",
        "paddingBottom": "16px"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "2 capsule before meals",
                "color": "#8C8C8C",
                "size": "sm",
                "wrap": true
              }
            ],
            "flex": 1
          }
        ],
        "spacing": "md",
        "paddingAll": "12px"
      },
      "styles": {
        "footer": {
          "separator": false
        }
      }
    }
  ]
}
                }
            }
        )
     elif message == 'Medicine Reciept':
     output = FlexSendMessage(
     alt_text='hello',
     contents={
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "RECEIPT",
        "weight": "bold",
        "color": "#1DB446",
        "size": "sm"
      },
      {
        "type": "text",
        "text": "Pharmacy ",
        "weight": "bold",
        "size": "xxl",
        "margin": "md"
      },
      {
        "type": "text",
        "size": "xs",
        "color": "#aaaaaa",
        "wrap": true,
        "text": "-----------------------------------"
      },
      {
        "type": "separator",
        "margin": "xxl"
      },
      {
        "type": "box",
        "layout": "vertical",
        "margin": "xxl",
        "spacing": "sm",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "Medicine 1",
                "size": "sm",
                "color": "#555555",
                "flex": 0
              },
              {
                "type": "text",
                "text": "$15.00",
                "size": "sm",
                "color": "#111111",
                "align": "end"
              }
            ]
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "Medicine 2",
                "size": "sm",
                "color": "#555555",
                "flex": 0
              },
              {
                "type": "text",
                "text": "$7.00",
                "size": "sm",
                "color": "#111111",
                "align": "end"
              }
            ]
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "Medicine 3",
                "size": "sm",
                "color": "#555555",
                "flex": 0
              },
              {
                "type": "text",
                "text": "$12.00",
                "size": "sm",
                "color": "#111111",
                "align": "end"
              }
            ]
          },
          {
            "type": "separator",
            "margin": "xxl"
          },
          {
            "type": "box",
            "layout": "horizontal",
            "margin": "xxl",
            "contents": [
              {
                "type": "text",
                "text": "ITEMS",
                "size": "sm",
                "color": "#555555"
              },
              {
                "type": "text",
                "text": "3",
                "size": "sm",
                "color": "#111111",
                "align": "end"
              }
            ]
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "TOTAL",
                "size": "sm",
                "color": "#555555"
              },
              {
                "type": "text",
                "text": "$34.00",
                "size": "sm",
                "color": "#111111",
                "align": "end"
              }
            ]
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "CASH",
                "size": "sm",
                "color": "#555555"
              },
              {
                "type": "text",
                "text": "$40.00",
                "size": "sm",
                "color": "#111111",
                "align": "end"
              }
            ]
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "CHANGE",
                "size": "sm",
                "color": "#555555"
              },
              {
                "type": "text",
                "text": "$6.00",
                "size": "sm",
                "color": "#111111",
                "align": "end"
              }
            ]
          }
        ]
      },
      {
        "type": "separator",
        "margin": "xxl"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "margin": "md",
        "contents": [
          {
            "type": "text",
            "text": "PAYMENT ID",
            "size": "xs",
            "color": "#aaaaaa",
            "flex": 0
          },
          {
            "type": "text",
            "text": "#42069123774",
            "color": "#aaaaaa",
            "size": "xs",
            "align": "end"
          }
        ]
      }
    ]
  },
  "styles": {
    "footer": {
      "separator": true
    }
  }
}
    )
    
    
    else:
        output = TextSendMessage(text="Just echo echo~~~")
    line_bot_api.reply_message(
        event.reply_token,
        output
    )


@handler.add(VideoPlayCompleteEvent)
def handle_follow(event):
    event_name = event.video_play_complete.tracking_id
    output = 'Video fail'
    if event_name == 'video1':
        output = 'Complete'
    line_bot_api.reply_message(
        event.reply_token,
        messages=[TextSendMessage(text=output)]
    )


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
