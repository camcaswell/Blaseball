import requests
import json

BASE = "http://api.blaseball-reference.com/v1"

TEAMS = {
    "garages": "105bc3ff-1320-4e37-8ef0-8d595cb95dd0",
    "lovers": "b72f3061-f573-40d7-832a-5ad475bd7909",
    "millennials": "36569151-a2fb-43c1-9df7-2df512424c82",
    "pies": "23e4cbc1-e9cd-47fa-a35b-bfa06f726cb7",
    "steaks": "b024e975-1c4a-4575-8936-a3754a08806a",
    "breath mints": "adc5b394-8f76-416d-9ce9-813706877b84",
    "fridays": "979aee4a-6d80-4863-bf1c-ee1a78e06024",
    "magic": "7966eb04-efcc-499b-8f03-d13916330531",
    "moist talkers": "eb67ae5e-c4bf-46ca-bbbc-425cd34182ff",
    "shoe thieves": "bfd38797-8404-4b38-8b82-341da28b1f83",
    "firefighters": "ca3f1c8c-c025-4d8e-8eef-5be6accbeb16",
    "jazz hands": "a37f9158-7f82-46bc-908c-c9e2dda7c33b",
    "lift": "c73b705c-40ad-4633-a6ed-d357ee2e2bcf",
    "tigers": "747b8e4a-7e50-4638-a973-ea7950a3e739",
    "wild wings": "57ec08cc-0411-4643-b304-0e80dbc15ac7",
    "dale": "b63be8c2-576a-4d6e-8daf-814f8bcea96f",
    "flowers": "3f8bbb15-61c0-4e3f-8e4a-907a5fb1565e",
    "spies": "9debc64f-74b7-4ae1-a4d6-fce0144b6ea5",
    "sunbeams": "f02aeae2-5e6a-4098-9842-02d2273f25c7",
    "tacos": "878c1bf6-0d21-4659-bfee-916c8314d69c"
}

def glet(endpoint, params={}):
    return requests.get(BASE + endpoint, params).json()

# RAW DATA
def getSeasonEvents(season):
   return glet('/data/events', {"season": season})



#GAME EVENTS
def getEvents(**params):
    '''OPTIONS
    playerId: The ID of a player that must be the batter or the pitcher in each event.
    gameId: The ID of the game by which to filter results.
    pitcherId: The ID of the pitcher that must be in each event.
    batterId: The ID of the batter that must be in each event.
    type: The type of event by which to filter.
    outcomes: Include child player event records. (Boolean)
    baseRunners: Include child base runner records. (Boolean)
    sortBy: The field by which to sort. Most text and numeric columns are supported.
    sortDirection: The direction by which to sort. Must be one of ASC, DESC.
    '''
    return glet('/events', params)

def getCount(eventType, **kwargs):
    '''OPTIONS
    batterId: The ID of the batter(s) by which to filter.
    pitcherId: The ID of the pitcher(s) by which to filter.
    '''
    params = {'eventType': eventType}
    params.update(kwargs)
    return glet('/countByType', params)



#PLAYERS
def getDeceased():
    return glet('/deceased')

def getPlayerIdsByName(name, current=False):
    params = {'name': name, 'current': current}
    return [p['player_id'] for p in glet('/playerIdsByName', params)]

def getPlayerInfo(**params):
    '''OPTIONS
    playerId: The player ID of the player (takes precedence if other params are specified)
    name: The name of the player (takes precedence if slug is specified)
    slug: The url_slug of the player
    all: (default:false) If true, all historical info for the player will be returned, rather than just the current info
    '''
    return glet('/playerInfo', params)

def getTaggedPlayers():
    return glet('/taggedPlayers')

def getPlayers(shadows=False):
    params = {"includeShadows": shadows}
    return glet('/allPlayers', params)

def getPlayersForGameday(**params):
    '''OPTIONS
    season: Season to query (zero-indexed)
    day: Day to query (zero-indexed)
    '''
    return glet('/allPlayersForGameday', params)



#TEAMS
def getRoster(**params):
    '''OPTIONS
    teamId: The ID of the team (takes precedence if slug is given)
    slug: The URL slug of the team
    '''
    return glet('/currentRoster', params)

def getTeams():
    return glet('/allTeams')

def getTeamStars():
    return glet('/allTeamStars')



#STATISTICS V2
def getSeasonLeaders(**params):
    '''OPTIONS
    season: Season to query (zero-indexed)
    category: Stat category (batting, pitching, running, or fielding)
    stat: Stat to get the leaders for (as returned from /playerStats)
    order: Ordering to use for ranking (ASC or DESC)
    limit: Number of leaders to return
    '''
    return glet('/seasonLeaders', params)

def getPlayerStats(**params):
    '''OPTIONS
    category:   (required) 'batting', 'pitching', 'running', or 'fielding'
    season:     (optional) season to get stats for
    playerIds:  (required) comma-separated list of player IDs
    '''
    return glet('/playerStats', params)
