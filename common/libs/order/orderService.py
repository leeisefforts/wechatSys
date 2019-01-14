from application import app, dbfrom common.libs.wechatService import WeChatServiceimport requests, jsonclass OrderService:    weChatService = WeChatService()    def __init__(self):        pass    def __orderlist__(self, pageNum, pageSize, keyword, orderStatuses, deliveryTypes):        accesstoken = self.weChatService.getAccessToken()        url = 'https://dopen.weimob.com/api/1_0/ec/order/queryOrderList?accesstoken={0}'.format(accesstoken)        data = {            'pageNum': pageNum,            'pageSize': pageSize,            'queryParameter': {            }        }        if keyword:            data['queryParameter']['keyword'] = [keyword]        if orderStatuses:            data['queryParameter']['orderStatuses'] = [orderStatuses]        if deliveryTypes:            data['queryParameter']['deliveryTypes'] = [deliveryTypes]        r = requests.post(url, json=data)        if r.status_code != 200 or not r.text:            return 400        data = json.loads(r.text)        return data['data']    def __orderinfo__(self, orderNo):        accesstoken = self.weChatService.getAccessToken()        url = 'https://dopen.weimob.com/api/1_0/ec/order/queryOrderDetail?accesstoken={0}'.format(accesstoken)        data = {            'orderNo': orderNo        }        r = requests.post(url, json=data)        if r.status_code != 200 or not r.text:            return 400        data = json.loads(r.text)        return data['data']    def __cancelorder__(self, orderNo, reason):        accesstoken = self.weChatService.getAccessToken()        url = 'https://dopen.weimob.com/api/1_0/ec/order/cancelOrder?accesstoken={0}'.format(accesstoken)        data = {            'orderNo': orderNo,            'specificCancelReason': reason        }        r = requests.post(url, json=data)        if r.status_code != 200 or not r.text:            return 400        data = json.loads(r.text)        return data['data']    def __deliveryOrder__(self, orderNo, cardcode):        accesstoken = self.weChatService.getAccessToken()        url = 'https://dopen.weimob.com/api/1_0/ec/order/deliveryOrder?accesstoken={0}'.format(accesstoken)        data = {            'orderNo': orderNo,            'isNeedLogistics': False,            'deliveryRemark': '您的商品提取码为：' + cardcode        }        r = requests.post(url, json=data)        if r.status_code != 200 or not r.text:            return 400        data = json.loads(r.text)        return data['data']    def __chargeOff__(self, orderNo, cardcode):        accesstoken = self.weChatService.getAccessToken()        url = 'https://dopen.weimob.com/api/1_0/ec/order/chargeOff?accesstoken={0}'.format(accesstoken)        data = {            'orderNo': orderNo,            'storeId': False,            'siteId': '',            'selfPickupCode': cardcode,            'sceneType': 3        }        r = requests.post(url, json=data)        if r.status_code != 200 or not r.text:            return 400        data = json.loads(r.text)        return data['code']