from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
import json
import random

clients = []
game = {
    "word": None,
    "drawer": None,
    'drawer_id': -1,
    "points": {},
}

words = []
with open('words.txt', 'r') as f:
    words = f.readlines()
    words = [word.lower().strip() for word in words]


def getwords():
    game['drawer_id']+=1
    game['drawer_id']%=len(clients)
    game['drawer'] = clients[game['drawer_id']]
    msg = {
        'type': 'getwords',
        'drawer': False,
        'words': random.sample(words, 5)
    }

    # TODO allow user to pick word
    game['word'] = msg['words'][0]

    for client in clients:
        if client != game['drawer']:
            client.sendMessage(json.dumps(msg))

    msg['drawer'] = True
    game['drawer'].sendMessage(json.dumps(msg))

    print("getwords ran")

class SimpleChat(WebSocket):
    def handleMessage(self):
        print(self.data)
        if not self.data:
            return
        data = json.loads(self.data)

        if game['drawer'] == None:
            getwords()


        if data["type"] == "connected":
            if data["id"] not in game["points"]:
                game["points"][data["id"]] = 0
            return

        for client in clients:
            if client != self:
                client.sendMessage(json.dumps(data))

    def handleConnected(self):
        print(self.address, "connected")
        # for client in clients:
        #    client.sendMessage(self.address[0] + u' - connected')
        clients.append(self)


        if game['drawer'] == None:
            getwords()
        else:
            self.sendMessage(json.dumps({
                'type': 'getwords',
                'drawer': False,
                'words': [game['word']]
            }))

    def handleClose(self):
        clients.remove(self)
        print(self.address, "closed")
        # for client in clients:
        #    client.sendMessage(self.address[0] + u' - disconnected')


server = SimpleWebSocketServer("", 8000, SimpleChat)
server.serveforever()
