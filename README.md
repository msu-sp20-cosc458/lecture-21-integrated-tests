# lecture-19-integrated-tests

Integrated test

## Run the tests

Run the test code in `tests_socketio.py` file. Answer the following questions:
* What is the line of code connects creates a test client?
* What is the line of code retrieves the event name of the socket.io emit function?

## Write more tests and fix the buggy code!

Look at function `get_chatbot_response` inside `functions.py`.

It's a buggy function that I slapped together real quick. Given a particular
user input, it's intended to return what a chatbot would say.

There are four commands -- `hello`, `add`, `divide`, and `say`, and they should
all be usable like your chatbot would be!

(As an example, `get_chatbot_response("Hello")` should return `"Hey there!"`.)

Modify `tests/unit_tests.py` and write and run some unit tests that
codify expected input/output combinations for this function.

As you write and run the tests, you'll find bugs in the code. Fix them and
write tests for your fixes :)

## Finished?

Get a head start with continuous integraton. Read the following article:
* https://www.martinfowler.com/articles/continuousIntegration.html
