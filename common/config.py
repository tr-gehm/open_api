import configparser

from common import handle_path


class ReadConfig:

    def __init__(self):
        self.config=configparser.ConfigParser()
        self.config.read(handle_path.GLOBAL_FILE)
        switch=self.config.getboolean('switch','on') #读取value
        if switch: #判断value值
            self.config.read(handle_path.ONLINE_CONF, encoding='utf-8')
        else:
            self.config.read(handle_path.TEST2_CONF, encoding='utf-8')

    def get(self,section,option):
        return self.config.get(section,option)


config=ReadConfig()
if __name__ == '__main__':
    host=config.get("call_sdk", "tel")
    print(host)