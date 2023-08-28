import configparser


config=configparser.RawConfigParser()
config.read(".//configurations/config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url=config.get('common info','baseURL')
        return  url

    @staticmethod
    def getLoginPageTitle():
        title = config.get('common info', 'login_page_title')
        return title

    @staticmethod
    def getUserName():
        usr = config.get('common info', 'username')
        return usr

    @staticmethod
    def getPassword():
        pwd = config.get('common info', 'password')
        return pwd

    @staticmethod
    def getTcPageHeader():
        header_tc = config.get('common info', 'tax_categorization_page_header_title')
        return header_tc