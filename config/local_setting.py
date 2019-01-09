APP = {
    'domain': 'http://worktech.xyz'
}

UPLOAD = {
    'ext': ['jpg', 'gif', 'bmp', 'jpeg', 'png'],
    'prefix_path': '/web/static/upload/',
    'prefix_url': '/static/upload/'
}

AUTH_COOKIE_NAME = 'UserCookie'
SERVER_PORT = '5000'
SQLALCHEMY_ECHO = False
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://bryant:leekobe24@cd-cdb-nmj4h99o.sql.tencentcdb.com:63625/wechatSys'
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_ENCODING = "utf8mb4"
SQLALCHEMY_BINDS = {
    'wechat': "mysql+pymysql://bryant:leekobe24@cd-cdb-nmj4h99o.sql.tencentcdb.com:63625/wechatSys"
}

MINA_APP = {
    'appid': '538F91180F6A814CF506865089323FCE',
    'appkey': 'E4BEF179E89C70BCC43DC08588869FBC',
    'paykey': 'TM8KwVFRlp0hsTWMQTxLplfFIzmk7csr',
    'mch_id': '1513434041',
    'callback_url': '/api/order/callback'
}

PAY_STATUS_DISPLAY_MAPPING = {
    "4": "已取消",
    "3": "已完成",
    "2": "已发货，待收货,",
    "1": "已付款，待发货",
    "0": "等待买家付款"
}
