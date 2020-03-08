import app, unittest

class SocketIOTestCase(unittest.TestCase):
    def test_server_sends_hello(self):
        client = app.socketio.test_client(app.app)
        response = client.get_received()

        self.assertEquals(len(response), 1)
        from_server = response[0]
        self.assertEquals(
            from_server['name'], 
            "hello to client"
        )
        data = from_server['args'][0]
        self.assertEquals(data['message'], "Hey there!")
        
    def test_server_relays_message(self):
        client = app.socketio.test_client(app.app)
        client.emit('new message', {
            'my message': 'Purple is beautiful!'
        })
        response = client.get_received()
        self.assertEquals(len(response), 2)
        from_server = response[1]
        self.assertEquals(
            from_server['name'],
            'got your message'
        )
        data = from_server['args'][0]
        self.assertEquals(
            data['your message'],
            u'Purple is beautiful!'
        )

if __name__ == '__main__':
    unittest.main()
