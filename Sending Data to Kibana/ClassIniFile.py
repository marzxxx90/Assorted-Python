import configparser

def create_config(path):
    config = configparser.ConfigParser()
    config.add_section("RowsConfig")
    config.set("RowsConfig","StartRow","")
    config.set("RowsConfig","EndRow","")
    
    with open(path,'w') as config_file:
        config.write(config_file)
        
if __name__ == '__main__':
    path = 'config.ini'
    create_config(path)