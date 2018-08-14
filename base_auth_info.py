class BaseAuthInfo:

    # Base Auth Info #

    # API Gateway api key
    api_key = "5wbYKROLFv38n73HWFte9xGW7zPXwah2qKuFEPgA"
    # NCP Access key
    access_key = 'qEvQEqjALeNxsOXqAa0F'
    # NCP Access secrete
    access_secrete = 'sU9ZMODPKawiR9lA2cKoKfjs9pv71pfy0eo2hkXQ'

    # Cloud OutBound Mailer #
    # Outbound Mailer REST End-point
    mail_ep_path = 'https://mail.apigw.ntruss.com/api/v1/mails'

    def get_api_key(self):
        return self.api_key

    def get_access_key(self):
        return self.access_key

    def get_access_secrete(self):
        return self.access_secrete

    def get_mail_ep_path(self):
        return self.mail_ep_path
