import random
from typing import Optional
from fastapi import FastAPI

class Player:
    def __init__(self, game_id, player_id, length):
        self.game_id = game_id
        self.player_id = player_id
        self.score = 0
        self.position = 0
        self.right_answer = 0
        self.lenght = length

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

class Game:
    def __init__(self, id, key):
        self.id = id
        self.key = key

def generate_task():
    a = random.randint(10, 49)
    b = random.randint(10,49)
    return [a, b]


# length = 200
# game = [Player(1,i, length) for i in range(5)]
# for i in game:
#     data = generate_task()
#     i.right_answer = sum(data)
#     i.send_num(data)

app = FastAPI()
@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

    
