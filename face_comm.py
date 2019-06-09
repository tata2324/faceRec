#coding=utf-8

import  ConfigParser

#写入计数值
def set_count(value):
    cf = ConfigParser.ConfigParser()
    cf.add_section('lmdb')
    cf.set('lmdb', 'point', value)
    with open("/webService/count.ini", "w+") as f:
        cf.write(f)
#读出计数值
def get_count():
    cf = ConfigParser.ConfigParser()
    cf.read('/webService/count.ini')
    return cf.get('lmdb', 'point')




#读取配置文件
def get_conf(key,value):
    cf = ConfigParser.ConfigParser()
    cf.read('/webService/config.ini')
    return cf.get(key,value)


def embed_to_str(vector):
    new_vector = [str(x) for x in vector]
    return ','.join(new_vector)


def str_to_embed(str):
    str_list = str.split(',')
    return [float(x) for x in str_list]


if __name__=='__main__':
    set_count(100)
    print get_count()
