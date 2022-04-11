import paramiko

class Connection :
    
    def __init__(self, server : str, port : int, username : str, password : str) -> None :
        
        self.ssh = paramiko.SSHClient()
        
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())        
        self.ssh.connect(server, port = port, username=username, password=password)
        