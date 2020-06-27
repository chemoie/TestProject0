
import requests
# 更改api：
upload_url=r'http://127.0.0.1:5000/modules/upload1/'
# 更改文件名称：
data_name='tmg'
# 更改文件路径：
data_path='t.pdb'

#post请求
try:
    upload_url=upload_url
    file0={"data0" : (data_name, open(data_path, "rb"))}
    # 添加token头信息
    headers={'token':'iamtoken123456789'}
    response=requests.post(url=upload_url,files=file0,headers=headers)
    jsonbool=int(response.headers['ifjson'])
    if jsonbool==1:
        # 获取response.json对象
        res_json=response.json()
        if res_json['status']==200:
            file_name=res_json['file_name']
            file_con=res_json['file_con']
            print('filename:',file_name)
            print('filecon:',file_con)
        else:
            msg=res_json['msg']
            print('msg:',msg)
    else:
        with open('spannedfile.txt','wb') as handle:
            handle.write(response.content)
        print('文件已生成')

except Exception as e:
    print(e)




