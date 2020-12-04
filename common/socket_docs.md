## Readme about the following files
- `client/client_socket.py` 
- `server/server_socket.py`
- `common/socket_utils.py`

#### Info
- [Python docs about sockets](https://docs.python.org/3/library/socket.html)
- Current sockets settings support IPv4 only
- Testing the sockets:
    1. Run `create_server()` function from `server_socket.py`
    2. Run **simultaneously** two instances of function `create_player("username")` from `cleint_socket.py`

#### Errors handled:
- server 
    - `server_socket.py`
        - [X] Wrong address binding in server class `__init__` won't create a server and end the game
        - [X] Timeout when waiting for players in server will print out the message and end the game
        - [X] Handled some maybe rare error with abruptly closed TCP program on the Windows client in the 
        `server.game()` loop logic
        - [X] `create_server()` function won't create any not-usable server object
- common 
    - `socket_utils.py`
        - [X] Handled the possibility of empty message received (which might cause the infinite while loop),
        by returning the "error" string that the server logic handles as a move message, which forces the player
        to remake the move. 
- client
    - `client_socket.py`
        - [X] Handled the `OSError` - in case of any operating system based problems we close the socket at the `__init__` level 
        (instead of handling the `InterruptedError` that was written before)
        - [ ] In `client/client_socket.py:33` despite we expect the one-byte message we might set the `recv` bufsize to 2 bytes, 
to best match with hardware & network realities, according to the Python docs
        - [ ] Plus, in `client/client_socket.py:12` we can think of changing the `conn.connect((host, port))` to `conn.connect_ex(
    (host, port))` - the difference is that the `connect_ex` (from Python docs): 
            >returns an error indicator instead of raising an exception for errors returned by 
            the C-level connect() call (other problems, such as “host not found,” can still 
            raise exceptions). The error indicator is 0 if the operation succeeded, 
            otherwise the value of the errno variable. This is useful to support, for example, 
            asynchronous connects.

#### TODO
- [X] Class cleanup
- [X] Errors handling check and improve
- [ ] Implement functionality of rooms creating
