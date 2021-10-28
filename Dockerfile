FROM python:3.7-alpine
LABEL maintainer='1010562639@qq.com'
LABEL description='Clink2 Api'


# 更新pip
RUN pip install --upgrade pip --index-url https://pypi.douban.com/simple

# 工作目录
WORKDIR /usr/src/app
ADD . /usr/src/app

# pip安装依赖包
RUN pip install -r requirements.txt --index-url https://pypi.douban.com/simple


# 执行命令行,启动脚本
CMD ["python", "-m", "run_test"]

