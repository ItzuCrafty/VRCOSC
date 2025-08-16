from __future__ import annotations
from pythonosc.udp_client import SimpleUDPClient

class VRCOSC:
    def __init__(self, host:str="127.0.0.1", port:int=9000) -> None:
        self.host = host
        self.port = port
        self.client = SimpleUDPClient(self.host, self.port)

    def chatbox_input(self, text:str="", immediate:bool=True, sound:bool=False) -> None:
        self.client.send_message("/chatbox/input", [text, immediate, sound])

    def chatbox_typing(self, typing:bool=True) -> None:
        self.client.send_message("/chatbox/typing", typing)
