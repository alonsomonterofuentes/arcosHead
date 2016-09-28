import ConfigParser

class conf():

    def __init__(self,path):
        self.path= path
        self.getConfig(path)
        
    def getConfig(self,path):
        """
        Creates the config object
        """
        self.config = ConfigParser.ConfigParser()
        self.config.read(path)


    def getSetting(self,section, setting):
        """
        Returns value of a setting
        """
        value = self.config.get(section, setting)
        print "{section} {setting} is {value}".format(
        section=section, setting=setting, value=value)
        return value

