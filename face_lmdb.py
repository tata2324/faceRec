#coding=utf-8

'''
通过facenet得到的512特征写入lmdb文件中
'''

import  lmdb
import  os
import  face_comm

class face_lmdb:
    # 添加一条数据
    def add_embed_to_lmdb(self,id,vector):
        self.db_file=os.path.abspath(face_comm.get_conf('lmdb','lmdb_path'))
        id = str(id)
        evn = lmdb.open(self.db_file, map_size=int(1e12))
        wfp = evn.begin(write=True)
        wfp.put(key=id, value=face_comm.embed_to_str(vector))
        wfp.commit()
        evn.close()
    # 获取存入的数据总量
    def get_count(self):
        self.db_file=os.path.abspath(face_comm.get_conf('lmdb','lmdb_path'))
        evn = lmdb.open(self.db_file, map_size=int(1e12))
        wfp = evn.begin(write=True)
        return wfp.stat()['entries']


if __name__=='__main__':
    #插入数据
    db_file = os.path.abspath(face_comm.get_conf('lmdb', 'lmdb_path'))
    embed = face_lmdb()
    # embed.add_embed_to_lmdb(12,[1,2,0.888333,0.12343430])


    evn = lmdb.open(db_file, map_size=int(1e12))
    wfp = evn.begin(write=True)

    # 全部删除
    for key,value in wfp.cursor():
        wfp.delete(key=key)
        print key,face_comm.str_to_embed(value)

    wfp.commit()
    evn.close()

    #全部显示
    # for key,value in wfp.cursor():
    #     print key,face_comm.str_to_embed(value)
    # evn.close()


