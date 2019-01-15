from application import app, dbfrom common.libs.WebHelper import getCurrentDatefrom common.libs.goods.goodsService import GoodsServicefrom common.model.wechat.Machine_Weimob import Machine_Weimobfrom common.model.wechat.Machine_CardCode import Machine_CardCodefrom sqlalchemy import and_import random, stringclass MachineService:    def __init__(self):        pass    def __createcardcode__(self):        src_digits = string.digits  # string_数字        src_uppercase = ['A', 'B', 'C', 'D', 'E', 'F']  # string_大写字母        for i in range(8):            # 随机生成数字、大写字母、小写字母的组成个数（可根据实际需要进行更改）            digits_num = random.randint(1, 4)            uppercase_num = random.randint(1, 8 - digits_num)            # 生成字符串            password = random.sample(src_digits, digits_num) + random.sample(src_uppercase,                                                                             uppercase_num)            # 打乱字符串            random.shuffle(password)            # 列表转字符串            new_password = ''.join(password)            return new_password    def __saveorderinfo__(self, order_info):        cardcode = self.__createcardcode__()        cardcode_isVaild = Machine_Weimob.query.filter_by(cardcode=cardcode).first()        while cardcode_isVaild:            cardcode = self.__createcardcode__()            cardcode_isVaild = Machine_Weimob.query.filter_by(cardcode=cardcode).first()        for item in order_info['itemList']:            machine = Machine_Weimob()            machine.goodsId = item["goodsId"]            machine.goods_name = item["goodsTitle"]            machine.goodscode = item['goodsCode']            machine.orderNo = order_info['orderNo']            machine.createtime = getCurrentDate()            machine.orderStatus = order_info['orderStatus']            machine.pid = order_info['merchantInfo']['pid']            machine.merchantTitle = order_info['merchantInfo']['merchantTitle']            machine.processStoreId = order_info['merchantInfo']['processStoreId']            machine.processStoreTitle = order_info['merchantInfo']['processStoreTitle']            machine.selfPickupSiteId = order_info['merchantInfo']['selfPickupSiteId']            machine.storeId = order_info['merchantInfo']['storeId']            machine.storeTitle = order_info['merchantInfo']['storeTitle']            machine.wid = order_info['buyerInfo']['wid']            machine.userNickname = order_info['buyerInfo']['userNickname']            machine.deliveryNo = order_info['deliveryDetail']['selfPickupDetail']['logisticsOrderList'][0]['deliveryNo']            machine.cardcode = machine.deliveryNo[0, 7]            db.session.add(machine)            db.session.commit()        return True    def __validcardcode__(self, order_id, cardcode, pid, vmc):        machine_cardcode = Machine_CardCode()        rule = and_(Machine_Weimob.cardcode == cardcode, Machine_Weimob.pid == pid)        list = Machine_Weimob.query.filter(rule).all()        # if list:        #     url = 'http://39.104.57.0:8079/FASTCODE'        #     data = {        #         'PTYPE': 'FASTCODE',        #         'FASTCODE': 0,        #         'VMC': vmc,        #         'USERNAME': 'woke_sub1',        #         'ID': order_id        #     }        #     for item in list:        #         data['PID'] = item.pid        return True