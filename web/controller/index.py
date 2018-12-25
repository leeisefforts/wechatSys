from application import app, db
from flask import Blueprint, jsonify, request
from common.libs.wechatService import WeChatService
from common.model.wechat.OauthAccessToken import OauthAccessToken
from common.libs.WebHelper import getCurrentDate

import requests, json

route_api = Blueprint('index_page', __name__)


@route_api.route('/')
@route_api.route('/index')
def index():
    return 'Api is ready'


@route_api.route('/callback')
def callback():
    req = request.values
    code = req['code'] if 'code' in req else ''
    state = req['state'] if 'state' in req else ''
    config_mina = app.config['MINA_APP']
    url = 'https://dopen.weimob.com/fuwu/b/oauth2/token?code={0}&grant_type=authorization_code&client_id={1}&client_secret={2}&redirect_uri={3}'.format(
        code, config_mina['appid'], config_mina['appkey'], 'http://47.104.176.254/api/callback')
    r = requests.post(url=url)
    data = json.loads(r.text)
    if data['access_token']:
        info = OauthAccessToken()
        info.access_token = data['access_token']
        info.expired_time = data['expires_in']
        info.created_time = getCurrentDate()
        db.session.add(info)
        db.session.commit()

    return jsonify(data)
