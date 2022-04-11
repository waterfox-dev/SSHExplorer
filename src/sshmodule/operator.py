from src.sshmodule.connection import Connection

import paramiko 
import time

class Operator :
    
    def __init__(self, connection : Connection) -> None:
        self.client = connection
    
    def execute(self, command : str, response = False) -> str | None:
        stdin, stdout, stderr = self.client.ssh.exec_command(command)
        if response :
            return stdout.readline()
