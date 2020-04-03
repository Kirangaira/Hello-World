from configparser import ConfigParser
parser = ConfigParser()
path = "issue3.config"
parser.read(path)
n = parser.get('RangeOfLoop', 'n')
lst = [print("Hello World") for i in range(int(num))]
