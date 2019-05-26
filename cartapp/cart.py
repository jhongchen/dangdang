class Info():
    '''
    订单项类
    属性：
        face：该书的图片
        name:该书的名字
        number：该订单项有几本书
        state：该订单项时否在购物车中，False时在回收站中
    方法：
        移除：将该订单项移除至回收站
        恢复：将回收站中的订单项恢复至购物车中
    '''
    def __init__(self,product,amount):
        self.id = product.id
        self.face = product.face
        self.name = product.name
        self.amount = amount
        self.dangdang_price = product.dangdang_price        # 当当价
        self.price = product.price                          # 原价
        self.total_price = product.dangdang_price * amount  # 订单项当当价总计
        self.state = True



class Cart:
    '''
    购物车类
    属性：
        lst：购物车列表，存放被选的一个至多个order_info对象
        价格；当当价格&原价（总价）
        amount：总数量
    方法：
        查询：查询出所有的订单项，即返回购物车&回收站列表
        添加：往 购物车列表 中添加新的order_info对象
        数量变更：将某个条目的数量变更
        计算价格：计算购物车列表中的总价
    '''
    def __init__(self):
        self.lst = []           # 全部订单项列表
        self.dangdang_price = 0 # 当当总价
        self.price = 0          # 原价总价
        self.amounts = 0        # 购物车总数量

    def add(self,info):
        '添加至购物车'
        for i in self.lst:
            if i.id == info.id: # 当购物车中有该商品时
                if i.state:     #当该订单项在购物车列表时，将其数量相加
                    i.amount += info.amount
                else:           #当该订单项在回收站时，将其数量置1，然后经其state变为True
                    i.amount = 1
                    i.state = True
                break
        else:                   #当购物车中没有该商品时，将订单项添加至购物车
            self.lst.append(info)
        self.change()

    def remove(self,info_id):
        '移入回收站'
        self.find(info_id).state = False    #修改其state即可
        self.change()                       #然后同步更新购物车数据

    def recover(self,info_id):
        '从回收站恢复'
        self.find(info_id).state = True
        self.change()

    def change_amount(self,info_id,new_amount):
        '变更订单项中的数量'
        self.find(info_id).amount = new_amount
        self.change()

    def change(self):
        '内容变更，同步更新其相关信息'
        self.dangdang_price = 0
        self.price = 0
        self.amounts = 0
        for item in self.lst:
            if item.state:
                self.dangdang_price += item.dangdang_price * item.amount     #购物车当当价总计
                self.price += item.price * item.amount   #原价总计
                self.amounts += item.amount              #数量总计
                item.total_price = item.dangdang_price * item.amount    # 订单项的总价

    def find(self,info_id):
        '根据id查找某个订单项'
        info_id = (info_id if isinstance(info_id,int) else int(info_id))
        for i in self.lst:
            if i.id == info_id:
                return i
        return False

    # def __del__(self):
    #     '存疑'
    #     for item in self.__list:
    #         item.delete()
    #     for item in self.__dellist:
    #         item.delete()
    #     super(Crat, self).__del__()