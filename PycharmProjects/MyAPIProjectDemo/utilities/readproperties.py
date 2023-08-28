import configparser

config=configparser.RawConfigParser()
config.read("MyAPIProjectDemo//api_testing_framwork_demo//configurations//config.ini")

class ReadConfig:
    @staticmethod
    def getBaseURL():
        url=config.get('common info','BASE_URL')
        return  url

