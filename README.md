# lecture-21-integrated-tests

Integrated test

## Testing Flask

Run the test code in `tests_flask.py`. Answer the following questions:
* What line of code creates a test client?
* What line of code retrieves the event name of a `socketio.emit` function?
* What line of code retrieves the data that `socketio.emit` function sends?
* What does `self.assertEquals(len(response), 1)` check for?
* What does `self.assertEquals(from_server['name'], "hello to client")` check for?
* If you add `print(response[1])` at the end of the function `test_server_relays_message`, what does it print?

## Testing Socket.io

Run the test code in `tests_socketio.py`. Answer the following questions:
* What line of code creates a test client?
* What line of code retrieves the event name of a `socketio.emit` function?
* What line of code retrieves the data that `socketio.emit` function sends?
* What does `self.assertEquals(len(response), 1)` check for?
* What does `self.assertEquals(from_server['name'], "hello to client")` check for?
* If you add `print(response[1])` at the end of the function `test_server_relays_message`, what does it print?

