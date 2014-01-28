import json

class Hero(object):

    def __init__(self):
        self.__id = ""
        self.__disp_name = ""
        self.__description = ""
        self.__primary_attribute = ""
        self.__attack_type = ""
        self.__team = ""
         
    def toJson(self):
        hero_dict = {}
        hero_dict['hero_id'] = self.__id
        hero_dict['disp_name'] = self.__disp_name
        hero_dict['description'] = self.__description
        hero_dict['primaryattribute'] = self.__primary_attribute
        hero_dict['attacktype'] = self.__attack_type
        hero_dict['team'] = self.__team
        return json.dumps(hero_dict)
        
    def fromJson(self, hero_json):
        json_dict = json.loads(hero_json)
        self.__id = json_dict['hero_id']
        self.__disp_name = json_dict['disp_name']
        self.__description = json_dict['description']
        self.__primary_attribute = json_dict['primaryattribute']
        self.__attack_type = json_dict['attacktype']
        self.__team = json_dict['team']
      