# -*- coding: utf-8 -*-
import lmdb

env = lmdb.open("./train")

# 参数write设置为True才可以写入
txn = env.begin(write=True)
############################################添加、修改、删除数据

# # 添加数据和键值
# txn.put(key='1', value='aaa')
# txn.put(key='2', value='bbb')
# txn.put(key='3', value='ccc')


# 通过键值删除数据
txn.delete(key='1')
#
# # 修改数据
# txn.put(key='3', value='ddd')

# 通过commit()函数提交更改
txn.commit()
############################################查询lmdb数据
txn = env.begin()

# get函数通过键值查询数据
print txn.get(str(2))

# 通过cursor()遍历所有数据和键值
for key, value in txn.cursor():
    print (key, value)

############################################


env.close()
