from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
import json

clients = []
game_data = {
    'points': {}
}
class SimpleChat(WebSocket):
    def handleMessage(self):
        print(self.data)
        if not self.data:
            return
        data = json.loads(self.data)

        if 'type' in data and data['type'] == 'connected':
            if data['id'] not in game_data['points']:
                game_data['points'][data['id']] = 0
        else:
            for client in clients:
                if client != self:
                    client.sendMessage(self.data)

    def handleConnected(self):
        print(self.address, 'connected')
        # for client in clients:
        #    client.sendMessage(self.address[0] + u' - connected')
        clients.append(self)

    def handleClose(self):
        clients.remove(self)
        print(self.address, 'closed')
        # for client in clients:
        #    client.sendMessage(self.address[0] + u' - disconnected')

server = SimpleWebSocketServer('', 8000, SimpleChat)
server.serveforever()
