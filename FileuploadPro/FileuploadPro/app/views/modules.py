
from flask import Blueprint, request, jsonify, send_from_directory, make_response
from settings import Token

#函数包导入
from app.funs import getfile


#视图注册，api注册
modules_bp=Blueprint('modules',__name__,url_prefix='/modules')

#视图
##upload0，接收文件data0,将文件内容，文件名称j'son形式返回。异常404
@modules_bp.route('/upload0/',methods=['POST'],endpoint='upload0')
def upload0():
    rec_token=request.headers['token']
    if request.method=='POST':
        try:
            if rec_token!=Token:
                file_dict = {
                    'status': 401,
                    'msg': '请求需要验证'
                }
                response = jsonify(file_dict)
                response.headers['ifjson'] = 1
                return response
            file_obj0=request.files.get('data0')
            #获取文件名称
            file_name=file_obj0.filename
            # 获取文件内容
            file_con=file_obj0.read().decode(encoding='utf8')
            #构建字典
            file_dict={
                'status':200,
                'file_name':file_name,
                'file_con':file_con
                }
            #返回json对象
            response = jsonify(file_dict)
            response.headers['ifjson'] = 1
            return response
        except Exception as e:
            print(e)
            file_dict = {
                'status': 404,
                'msg':'失败，请重传'
            }
            response=jsonify(file_dict)
            response.headers['ifjson'] = 1
            return response
#视图upload1,接收文件data0,经过函数getfile运算，在static文件夹生成文件，并将文件返回，异常返回404
@modules_bp.route('/upload1/',methods=['POST'],endpoint='upload1')
def upload1():
    # 获取请求头token，与upload0相同
    rec_token=request.headers['token']
    if request.method=='POST':
        try:
            #token判定
            if rec_token!=Token:
                file_dict = {
                    'status': 401,
                    'msg': '请求需要验证'
                }
                response = jsonify(file_dict)
                response.headers['ifjson'] = 1
                return response
            file_obj0=request.files.get('data0')
            file_name = file_obj0.filename
            file_con = file_obj0.read().decode(encoding='utf8')
            #调用函数生成文件
            fname=getfile.get_file(file_name,file_con)
            #返回文件
            response=make_response(send_from_directory('static',fname,as_attachment=True))
            response.headers['Content-Disposition']="p_w_upload; filename=test.txt"
            response.headers['ifjson']=0
            return response
        except Exception as e:
            print(e)
            file_dict = {
                'status': 404,
                'msg':'失败，请重传'
            }
            response = jsonify(file_dict)
            response.headers['ifjson'] = 1
            return response
