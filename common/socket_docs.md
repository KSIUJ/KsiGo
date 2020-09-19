Readme about the `client/client_socket.py` and `server/server_socket.py` files.

#### Testing the sockets:
1. Run `create_server()` function from `server_socket.py`
2. Run **simultaneously** two instances of function `create_player("username")` from `cleint_socket.py`

#### TODO
- Errors handling
    - In `commons/socket_utils.py` sending/receiving the messages is limited to messages up to 9999 chars. 
    We should make an error handling, that will raise an error when  the client will want to send a longer message.
- Implement functionality of rooms creating