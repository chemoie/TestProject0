from flask import Flask
import settings
from app.views.modules import modules_bp


def create_app():
    #创建flask  app
    app=Flask(__name__)
    #settings文件导入
    app.config.from_object(settings)
    #modules模块蓝图注册
    app.register_blueprint(modules_bp)
    return app