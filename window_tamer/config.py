import yaml

class Config:
    def __init__(self, config_file):
        self.load_config(config_file)

    def load_config(self, config_file):
        with open(config_file, 'r') as file:
            config_data = yaml.safe_load(file)
            self.commands = config_data