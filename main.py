from fastapi import FastAPI
from app.import_process.api.file_import_service import app as import_app

app = FastAPI()

# 挂载文件导入服务的所有路由
app.mount("/", import_app)
