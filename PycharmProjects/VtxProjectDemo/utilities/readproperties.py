import configparser


config=configparser.RawConfigParser()
config.read(".//configurations//config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url=config.get('common info','baseURL')
        return  url

    @staticmethod
    def getUserName():
        usr = config.get('common info', 'username')
        return usr

    @staticmethod
    def getPassword():
        pwd = config.get('common info', 'password')
        return pwd

    @staticmethod
    def getExpectedTitleOfPage():
        title = config.get('common info', 'page_title')
        return title

