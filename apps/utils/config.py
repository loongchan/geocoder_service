import json, os


class Config:
    """Loads geocoder_config.json and puts it into configs class variable"""
    def __init__(self):
        try:
            # get path of config file
            cur_path = os.path.dirname(__file__)
            grandma_path = os.path.dirname(os.path.dirname(cur_path))
            conf_path = os.path.join(grandma_path, "geocoder_config.json")

            conf_File = open(conf_path)
            self.configs = json.loads(conf_File.read())
            conf_File.close()
        except OSError:
            print('cannot open geocoder_config.json file')
            return None