class BaseAuthInfo:

    # Base Auth Info #

    # API Gateway api key
    api_key = ''
    # NCP Access key
    access_key = ''
    # NCP Access secret
    access_secret = ''

    # Cloud OutBound Mailer #
    # Outbound Mailer REST End-point
    mail_ep_path = 'https://mail.apigw.ntruss.com/api/v1/mails'

    def get_api_key(self):
        return self.api_key

    def get_access_key(self):
        return self.access_key

    def get_access_secret(self):
        return self.access_secret

    def get_mail_ep_path(self):
        return self.mail_ep_path
