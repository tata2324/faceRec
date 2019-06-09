# coding=utf-8
import face_handler
from bottle import default_app, get, run, post, request
from beaker.middleware import SessionMiddleware
import time, os, face_comm, json

# 设置session参数
session_opts = {
    'session.type': 'file',
    'session.cookie_expires': 3600,
    'session.data_dir': '/tmp/sessions/simple',
    'session.auto': True
}

@post("/query")
def upload():
    start = time.time()
    uploadfile = request.files.get('photo') # 获取上传的文件
    uploadfile.save("upload.jpg", overwrite=True)# overwrite参数是指覆盖同名文件
    path = os.getcwd() + '/upload.jpg'
    re = face_handler.query_face(path)
    use_time = str(time.time() - start)
    result = {
        "time": use_time,
        "id": re[0],
        "distance": re[1]
    }
    return json.dumps(result)

@post("/insert")
def insert():
    start = time.time()
    uploadfile = request.files.get('photo') # 获取上传的文件
    uploadfile.save("upload.jpg", overwrite=True)# overwrite参数是指覆盖同名文件
    path = os.getcwd() + '/upload.jpg'
    id = get_id()
    re = face_handler.add_face_index(id, path)
    if re:
        pass
    else:
        id = 0
    result = {
        "id": id
    }
    return json.dumps(result)

def get_id():
    id = int(face_comm.get_count())
    id = id + 1
    face_comm.set_count(id)
    print id
    return int(id)


# 函数主入口
if __name__ == '__main__':
    app_argv = SessionMiddleware(default_app(), session_opts)
    run(app=app_argv, host='0.0.0.0', port=9090,debug=True)
