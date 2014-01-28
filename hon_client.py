import urllib2, urllib, json, os

class HonClient(object):

   def __init__(self, api_token="3VCXXTGAQ5B94Q0W"):
      self.__root_url = "http://api.heroesofnewerth.com/"
      self.__api_token = api_token

   def makeGetRequest(self, url, urlValues={}):
      self.addTokenParam(urlValues)
      
      full_url = url + '?' + urllib.urlencode(urlValues)
      print full_url
      req = urllib2.Request(full_url)
      req.addheaders = [('User-agent', 'Mozilla/5.0')]
      f = urllib2.urlopen(req)
      data = f.read()
      f.close()
      return data

   def getHeroes(self):
      path_suffix = "heroes/all"
      url = self.__root_url + path_suffix

      heroes = self.makeGetRequest(url)
      heroes_file = open('json_data/heroes.json', 'w')
      heroes_file.write(heroes)
      heroes_file.close()
      return heroes

   def getHeroStats(self, account_id, hero_id):
      path_suffix = "hero_statistics/ranked/accountid/" + account_id + "/heroid/" + hero_id
      url = self.__root_url + path_suffix

      hero_stats = self.makeGetRequest(url)
      hero_stats_file = open('json_data/hero_stats/' + account_id + '_' + hero_id + '.json', 'w')
      hero_stat_file.write(hero_stats)
      hero_stat_file.close()
      return hero_stats

   def getHeroStats(self, nickname, hero_id):
      path_suffix = "hero_statistics/ranked/nickname/" + urllib.quote(nickname) + "/heroid/" + hero_id
      url = self.__root_url + path_suffix

      hero_stats = self.makeGetRequest(url)
      hero_stats_file = open('json_data/hero_stats/' + nickname + '_' + hero_id + '.json', 'w')
      hero_stat_file.write(hero_stats)
      hero_stat_file.close()
      return hero_stats

   def getHeroStats(self, account_id, hero_name):
      path_suffix = "hero_statistics/ranked/accountid/" + account_id + "/name/" + urllib.quote(hero_name)
      url = self.__root_url + path_suffix

      hero_stats = self.makeGetRequest(url)
      hero_stats_file = open('json_data/hero_stats/' + account_id + '_' + hero_name + '.json', 'w')
      hero_stat_file.write(hero_stats)
      hero_stat_file.close()
      return hero_stats

   def getHeroStats(self, nickname, hero_name):
      path_suffix = "hero_statistics/ranked/nickname/" + urllib.quote(nickname) + "/name/" + urllib.quote(hero_name)
      url = self.__root_url + path_suffix

      hero_stats = self.makeGetRequest(url)
      file_name = 'json_data/hero_stats/' + nickname + '_' + hero_name + '.json'
      self.writeFile(file_name, hero_stats)
      
      return hero_stats

   def addTokenParam(self, params_dict):
      params_dict['token'] = self.__api_token

   def writeFile(self, file_name, data):
      if not os.path.exists(os.path.dirname(file_name)):
         os.makedirs(os.path.dirname(file_name))
         
      with open(file_name, "w") as f:
         f.write(data)