# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 17:14:29 2020
we'll create a few classes to simulate a server that's taking connections from the outside and then a load
balancer that ensures that there are enough servers to serve those connections.

To represent the servers that are taking care of the connections, we'll use a Server class. Each connection is
represented by an id, that could, for example, be the IP address of the computer connecting to the server.
For our simulation, each connection creates a random amount of load in the server, between 1 and 10.
@author: oscarjex
"""

import random

class Server:
    def __init__(self):
        """Creates a new server instance, with no active connections."""
        self.connections = {}

    def add_connection(self, connection_id):
        """Adds a new connection to this server."""
        self.connection_id=connection_id
        connection_load = random.random()*10+1
        # Add the connection to the dictionary with the calculated load
        self.connections[connection_id]=connection_load
    def close_connection(self, connection_id):
        """Closes a connection on this server."""
        # Remove the connection from the dictionary

    def load(self):
        """Calculates the current load for all connections."""
        total = 0
        for i in self.connections.items():
            if i==self.connection_id:
                total+=self.connection_id.values()
        # Add up the load for each of the connections
        
        return total

    def __str__(self):
        """Returns a string with the current load of the server"""
        return "{:.2f}%".format(self.load())
    
"""
server = Server()
server.add_connection("192.168.1.1")

print(server.load())
"""