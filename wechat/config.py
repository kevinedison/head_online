WEIXIN_TOKEN = 'it'
WEIXIN_APPID = 'wx5f49a4b073b9e2b3'
WEIXIN_APPSECRET = '67b9181c0d004f4991104da57a6e28ba'

CREATE_MENU_URL = 'http://115.28.42.70/user_info/'
#CREATE_MENU_URL = 'http%3a%2f%2fwww.itcastcpp.cn%2fuser_info%2f'
HOME_URL = 'https://open.weixin.qq.com/connect/oauth2/authorize?appid=' + WEIXIN_APPID + '&redirect_uri=' + CREATE_MENU_URL + '&response_type=code&scope=snsapi_base&state=snsapi_base#wechat_redirect'
        

WEIXIN_ACCESS_TOKEN_URL = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=' + WEIXIN_APPID + '&secret=' + WEIXIN_APPSECRET
WEIXIN_ACCESS_TOKEN = ''
WEIXIN_ACCESS_TOKEN_LASTTIME = 0
WEIXIN_ACCESS_TOKEN_EXPIRES_IN = 0
