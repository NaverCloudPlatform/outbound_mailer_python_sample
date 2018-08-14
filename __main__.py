from mail_sender import MailSender
from rss_news_parser import RssNewsParser
from datetime import datetime
import json


def main(args):

    rlt = process_mail()

    return rlt


# cloud functions : Outbound mailer
def process_mail():

    current_date = datetime.today().strftime("%Y-%m-%d")
    mail_contents = RssNewsParser().news_rss_parser('NCP+네이버클라우드플랫폼')

    mail_info = {
        "senderAddress": "no_reply@company.com",
        "title": "네이버클라우드 플랫폼 뉴스 - ${current_date}",
        "body": mail_contents,
        "recipients": [
            {
                "address": "receiver@company.com",
                "name": "홍길동",
                "type": "R",
                "parameters": {
                    "current_date": current_date
                }
            }
        ],
        "individual": True,
        "advertising": False
    }

    res = MailSender().req_email_send(mail_info)
    result = res.getcode()

    return {"result": result}


if __name__ == '__main__':
    main(None)
