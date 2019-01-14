from web.controller.index import route_apifrom common.libs.messageService import MessageServicefrom common.libs.machineService import MachineServicefrom common.libs.order.orderService import OrderServicefrom common.model.wechat.Machine_CardCode import Machine_CardCodefrom common.libs.WebHelper import getCurrentDatefrom flask import jsonify, requestfrom application import dbimport json@route_api.route('/messages', methods=['POST'])def msg_gets():    resp = {'code': {'errorcode': 0, 'errmsg': 'success'}}    req = request.get_json()    return jsonify(resp)@route_api.route('/message', methods=['POST'])def msg_get():    resp = {'code': {'errorcode': 0, 'errmsg': 'success'}}    req = {}    try:        req = request.get_json()    finally:        if req:            topic = req['topic'] if 'topic' in req else ''            event = req['event'] if 'event' in req else ''            msg_body = req['msg_body'] if 'msg_body' in req else ''            orderNo = ''            if msg_body:                if msg_body != 'message test to check callbackUrl!':                    msg_body = json.loads(msg_body)                orderNo = msg_body['orderNo'] if 'orderNo' in msg_body else msg_body                if orderNo:                    msg = MessageService()                    msg.__createMsg__(orderNo, event, topic)                if event == 'orderStatusChange':                    mar = MachineService()                    order = OrderService()                    order_info = order.__orderinfo__(orderNo=orderNo)                    if order_info['orderStatus'] == 1:                        mar.__saveorderinfo__(order_info=order_info)    return jsonify(resp)@route_api.route('/cardcode', methods=['POST'])def cardcode_valid():    resp = {'resultCode': 1, 'reason': ''}    mar = MachineService()    req = request.values    id = req['ID']    vmc = req['VMC']    pid = req['PID']    code = req['CODE']    mac = req['MAC']    machine_cardcode = Machine_CardCode()    machine_cardcode.pid = pid    machine_cardcode.vmc = vmc    machine_cardcode.order_id = id    machine_cardcode.code = code    machine_cardcode.createtime = getCurrentDate()    db.session.add(machine_cardcode)    db.session.commit()    if mar.__validcardcode__(id, code, pid, vmc):        return jsonify(resp)    resp['resultCode'] = 0    resp['reason'] = '提货码不存在'    return jsonify(resp)@route_api.route('PRODUCT')def product_get():    resp = {}    return 200