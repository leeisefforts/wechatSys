from web.controller.index import route_apifrom common.libs.messageService import MessageServicefrom common.libs.machineService import MachineServicefrom flask import jsonify, requestimport json@route_api.route('/messages', methods=['POST'])def msg_gets():    resp = {'code': {'errorcode': 0, 'errmsg': 'success'}}    req = request.get_json()    return jsonify(resp)@route_api.route('/message', methods=['POST'])def msg_get():    resp = {'code': {'errorcode': 0, 'errmsg': 'success'}}    req = {}    try:        req = request.get_json()    finally:        if req:            topic = req['topic'] if 'topic' in req else ''            event = req['event'] if 'event' in req else ''            msg_body = req['msg_body'] if 'msgBody' in req else ''            orderNo = json.dumps(msg_body)            # if msg_body:            #     msg_body = json.loads(msg_body)            #     orderNo = msg_body['orderNo']            msg = MessageService()            msg.__createMsg__(orderNo, event, topic)            if event == 'orderStatusChange':                mar = MachineService()                password = mar.__createcardcode__()    return jsonify(resp)@route_api.route('/cardcode', methods=['POST'])def cardcode_valid():    resp = {'resultCode': 1, 'reason': ''}    mar = MachineService()    password = mar.__createcardcode__()    # req = request.values    # machineCode = req['machineCode']    # PID = req['PID']    # CODE = req['CODE']    # mac = req['MAC']    return password