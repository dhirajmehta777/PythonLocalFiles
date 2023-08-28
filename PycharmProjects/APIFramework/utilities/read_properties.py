import configparser

config=configparser.RawConfigParser()
config.read(".//configurations//config.ini")

class ReadConfig:
    @staticmethod
    def getBaseURL():
        url=config.get('common info','BASE_URL')
        return  url

    @staticmethod
    def getEndPoint():
        get_endpoint = config.get('common info', 'GetEndPointPath')
        return get_endpoint

    @staticmethod
    def postEndPoint():
        post_endpoint = config.get('common info', 'PostEndPointPath')
        return post_endpoint

    @staticmethod
    def putEndPoint():
        put_endpoint = config.get('common info', 'PutEndPointPath')
        return put_endpoint

    @staticmethod
    def deleteEndPoint():
        delete_endpoint = config.get('common info', 'DeleteEndPointPath')
        return delete_endpoint