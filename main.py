import random
from typing import Optional
from fastapi import FastAPI
import datetime


class Player:

    def __init__(self, game_id, player_id, name):
        self.game_id: int = game_id
        self.player_id: int = player_id
        self.score = 0
        self.position = 0
        self.right_answer = 0
        self.name = name

    def check_answer(self, answer):
        if (answer == self.right_answer):
            self.score += 1

    def update(self):
        self.position += self.score
    
    def check_end(self):
        if (self.position >= self.length):
            return 1
        return 0

    def send_num(data):
        pass


class Session:

    secret_key: int = 1111
    sessions = {}

    def __init__(self, key=None):
        self.id = self._genid()
        if key == None:
            self.key = self._genkey()
        else:
            self.key = key
        self.players = []
        self.status = False

    def _genid(self):
        while True:
            id = random.randint(1000, 9999)
            if (Session.sessions.get(id) == None):
                return id

    def _genkey(self):
        key = random.randint(1000, 9999)
        return key
    
    def add_player(self, player: Player):
        self.players.append(player)
    
    def gen_player_id(self):
        if (len(self.players) == 0):
            return random.randint(0, 9)
        while (True):
            id = random.randint(0, 9)
            flag = True
            for i in self.players:
                if (i.player_id == id):
                    flag = False
                    break
            if (flag == True):
                return id


def check_game_key(game, key):
    game = Session.sessions.get(game)
    if game != None:
        if game.key == key:
            return game
    return 0

def get_all_game(key):
    if key == Session.secret_key:
        response = []
        for i in Session.sessions:
            response.append({"id":i,
                            "key": Session.sessions[i].key})
        return response
    return 0

def check_game_create_key(q):
    print(Session.secret_key, q, Session.secret_key == q)
    if q == Session.secret_key:
        game = Session()
        Session.sessions[game.id] = game
        return {"id": game.id, "key": game.key}
    return 0

def get_game_data(id: int = None, key: int = None):
    game = Session.sessions.get(id)
    response = 0
    if game != None:
        if game.key == key:
            response = {"id": game.id, 
                        "key": game.key,
                        "players": []}
            for i in game.players:
                player = {"id": i.player_id,
                        "name": i.name}
                response["players"].append(player)
    return response


app = FastAPI()
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/game/create/")
def read_key_for_create_game(q: int = None):
    response = check_game_create_key(q)
    return {"game": response}

@app.get("/game/games/")
def read_all_game(key: int = None):
    response = Session.get_all_game(key)
    return response

@app.get("/game/getdata/")
def read_game_data(id: int = None, key: int = None):
    response = get_game_data(id, key)
    return {"response": response}

@app.get("/game/connect/")
def read_data_for_connect(game: int = None, key: int = None, name: str = None):
    game = Session.check_game_key(game, key)
    response = 0
    if game != 0:
        player_id = game.gen_player_id()
        player = Player(game, player_id, name)
        game.players.append(player)
        response = 1
    return {"response": response}

