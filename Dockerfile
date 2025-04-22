# 使用 Python 3.10-slim 作为基础镜像
FROM python:3.10-slim

WORKDIR /app

# 将项目文件复制到镜像中
COPY . /app

# 安装依赖
RUN pip install --upgrade pip && pip install -r requirements.txt

# 默认执行运算程序
CMD ["python", "math_functions.py"]
