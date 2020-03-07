from .constant import POSITION_MAP, PRO_TEAM_MAP, STATS_MAP
from .utils import json_parsing
import pdb

class Player(object):
    '''Player are part of team'''
    def __init__(self, data):

        self.name = json_parsing(data, 'fullName')
        self.playerId = json_parsing(data, 'id')
        self.position = POSITION_MAP[json_parsing(data, 'defaultPositionId') - 1]
        self.eligibleSlots = [POSITION_MAP[pos] for pos in json_parsing(data, 'eligibleSlots')]
            
        self.acquisitionType = json_parsing(data, 'acquisitionType')
        self.proTeam = PRO_TEAM_MAP[json_parsing(data, 'proTeamId')]
        self.injuryStatus = data['playerPoolEntry']['player']['injuryStatus']
        self.stats = {}

        # add available stats
        
        if 'stats' in data['playerPoolEntry']['player'].keys():
            for split in data['playerPoolEntry']['player']['stats']:
                
                if split['stats']:
                    self.stats[split['id']] = {}
                    try:
                        self.stats[split['id']] = {STATS_MAP[i]: split['stats'][i] for i in split['stats'].keys() if STATS_MAP[i] != ''}
                    except:
                        pdb.set_trace()
                        
    def __repr__(self):
        return 'Player(%s)' % (self.name, )
        
