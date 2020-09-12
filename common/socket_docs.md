Readme about the `client/client_socket.py` and `server/server_socket.py` files.

#### Testing the sockets:
1. Run `create_server()` function from `server_socket.py`
2. Run **simultaneously** two instances of function `create_player("username")` from `cleint_socket.py`

#### TODO
- line:41 in `server_socket.py` contains the temporary game logic, which has to be changed in the finished game
- Change the `localhost:9999` address (line:7 in `server_socket.py` and line:8 in `client_socket.py`) when we will have a server running

#### Possible problems
- [Socket Fragmented Received Data](https://stackoverflow.com/questions/57826357/socket-fragmented-received-data/57826997#57826997) 
    - [Implemented solution](https://stackoverflow.com/questions/34252273/what-is-the-difference-between-socket-send-and-socket-sendall)