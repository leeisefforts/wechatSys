from web.controller.index import route_apifrom common.libs.messageService import MessageServicefrom common.libs.machineService import MachineServicefrom common.libs.order.orderService import OrderServicefrom common.model.wechat.Machine_Weimob import Machine_Weimobfrom common.model.wechat.Machine_CardCode import Machine_CardCodefrom common.libs.WebHelper import getCurrentDatefrom flask import jsonify, requestfrom application import dbimport json, random, string@route_api.route('/messages', methods=['POST'])def msg_gets():    resp = {'code': {'errorcode': 0, 'errmsg': 'success'}}    req = request.get_json()    order = OrderService()    order_info = order.__orderinfo__('5143445018548')    return jsonify(resp)@route_api.route('/message', methods=['POST'])def msg_get():    resp = {'code': {'errorcode': 0, 'errmsg': 'success'}}    req = {}    try:        req = request.get_json()    finally:        if req:            topic = req['topic'] if 'topic' in req else ''            event = req['event'] if 'event' in req else ''            msg_body = req['msg_body'] if 'msg_body' in req else ''            str = ''            orderNo = ''            if msg_body:                if msg_body != 'message test to check callbackUrl!':                    pass # msg_body = json.loads(msg_body)                orderNo = msg_body['orderNo'] if 'orderNo' in msg_body else msg_body                if orderNo:                    msg = MessageService()                    msg.__createMsg__(orderNo, event, topic, str)                if event == 'orderStatusChange':                    mar = MachineService()                    order = OrderService()                    order_info = order.__orderinfo__(orderNo=orderNo)                    # if order_info['orderStatus'] == 1:                    mar.__saveorderinfo__(order_info=order_info)    return jsonify(resp)@route_api.route('/CARDCODE', methods=['GET', 'POST'])def cardcode_valid():    resp = {'resultCode': 1}    mar = MachineService()    req = request.values    id = req['ID'] if 'ID' in req else ''    vmc = req['VMC'] if 'VMC' in req else ''    pid = req['PID'] if 'PID' in req else ''    code = req['CODE'] if 'CODE' in req else ''    mac = req['MAC'] if 'MAC' in req else ''    if id == '' or vmc == '' or pid == '' or code == '' or mac == '':        resp['resultCode'] = 0        resp['reason'] = '缺失参数'        return jsonify(resp)    machine_cardcode = Machine_CardCode()    machine_cardcode.pid = pid    machine_cardcode.vmc = vmc    machine_cardcode.order_id = id    machine_cardcode.code = code    machine_cardcode.msg = id + '-' + vmc + '-' + 'pid=' + pid + 'code=' + code + 'mac=' + mac    machine_cardcode.createtime = getCurrentDate()    db.session.add(machine_cardcode)    db.session.commit()    try:        if mar.__validcardcode__(id, code, pid, vmc, mac):            return jsonify(resp)        resp['resultCode'] = 0        resp['reason'] = '提货码不存在'        return jsonify(resp)    finally:        pay_data = {            'ID': id,            'PID': pid,            'VMC': vmc,            'CODE': code,            'USER': 'yipao'        }        mar.product_make(pay_data=pay_data)@route_api.route('/product_make', methods=['POST'])def pro_make():    pass@route_api.route('/PRODUCT', methods=['POST'])def product_get():    resp = {'code': 0, 'reason': ''}    req = request.values    id = req['ID'] if 'ID' in req else ''    vmc = req['VMC'] if 'VMC' in req else ''    pid = req['PID'] if 'PID' in req else ''    mac = req['MAC'] if 'MAC' in req else ''    if id == '' or vmc == '' or pid == '' or mac == '':        resp['reason'] = '参数缺失'        return jsonify(resp)    return 200@route_api.route('/generCardCode')def gener_code():    mar = MachineService()    s = string.ascii_letters + string.digits    for i in range(600):        machine = Machine_Weimob()        machine.goodsId = 2147483647        machine.goods_name = '茶'        machine.goodscode = 257        machine.totalAmount = 1        machine.orderNo = i        machine.createtime = getCurrentDate()        machine.orderStatus = 2        machine.pid = 2147483647        machine.merchantTitle = '易泡智慧饮'        machine.processStoreId = 69306248        machine.processStoreTitle = '易泡智慧饮'        machine.selfPickupSiteId = 711248        machine.storeId = 69306248        machine.storeTitle = '易泡智慧饮'        machine.wid = 1213344985        machine.userNickname = '易泡智慧饮'        machine.deliveryNo = machine.cardcode = ''.join(random.sample(string.digits, 8))        db.session.add(machine)        db.session.commit()