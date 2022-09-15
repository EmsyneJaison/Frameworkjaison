import configparser
import selenium

class config:
    config = configparser.ConfigParser()
    config.read('../Config/ProjectConfig.ini')
    print(config['QC']['url'])

    def __init__(self,env):
        self.env=env

    def get_value(self,key):
        return self.config[self.env][key]

