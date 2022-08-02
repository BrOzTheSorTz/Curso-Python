# we'll create a few classes to simulate a 
# server that's taking connections from the 
# outside and then a load balancer that ensures
#  that there are enough servers to serve 
# those connections.

#To represent the servers that are taking 
# care of the connections, we'll use a Server
#  class. Each connection is represented by 
# an id, that could, for example, be the IP 
# address of the computer connecting to the 
# server. For our simulation, each connection 
# creates a random amount of load in the 
# server, between 1 and 10.


import random


class Server:

    #Constructor
    def __init__(self):
        """Creates a new server instance, with no active connections."""
        self.connections={}
    
    def add_connection (self, connection_id):

        connection_load = random.random()*10 +1
        #Each connection has a load 
        self.connections[connection_id]=connection_load

    def close_connection(self, connection_id):

        del self.connections[connection_id]

    def load(self):
        """Calculates the current load for all connections."""
        total = 0
        for load in self.connections.values():
            total += load
        
        return total
#Thanks to __str__ method, we van print a server instance
    def __str__ (self):
        """Returns a string with the current load of the server"""
        return "{:.2f}%".format(self.load())

server = Server()
server.add_connection("192.168.1.1")

print(server.load())

server.close_connection("192.168.1.1")
print(server.load())


# We now have a basic implementation 
# of the server class. Let's look at the basic
#  LoadBalancing class. This class will start 
# with only one server available. When a 
# connection gets added, it will randomly
#  select a server to serve that connection,
#  and then pass on the connection to the 
# 
# server. The LoadBalancing class also needs 
# to keep track of the ongoing connections 
# to be able to close them. 

class LoadBalancing:
    def __init__(self):
        #We store the connections of the servers
        # and initialize it with one server
        self.connections ={}
        self.servers = [Server()]
    
    def ensure_availability(self, server):
        """If the load of one server is bigger
        than 50 , we create anothe one"""
        if self.avg_load()+ server.load() > 50:
            return True 
        return False

    def add_connection(self, connection_id):

        #We choose a random server from the list
        server = random.choice(self.servers)

        if self.ensure_availability(server):

            new_server = Server()
            new_server.add_connection(connection_id)
            self.servers.append(new_server)
            self.connections[new_server]=connection_id

        else:
            #We dont need to add to the list 
            # because It is already

            server.add_connection(connection_id)
            self.connections[server]=connection_id
    def close_connection(self,connection_id):
        """Closes the connection on the 
        server corresponding to connection_id."""
        
        #For iterating and deleting things
        #  about a dictionary
        #we need to use a copy
        for server in self.connections.copy().keys():
            
            if self.connections.copy()[server]==connection_id:
                del self.connections[server]
                self.servers.remove(server)

    def avg_load(self):

        total = 0
        count =0
        for server in self.servers:
            total += server.load()
            count +=1

        return total/count
        
    def __str__ (self):
        """Returns a string with the load for each server."""
        #We use str(server) to print it and in this way
        # the __str__ method of the Server class
        # is executed too and we saved the load of
        # each server in a list
        loads = [str(server) for server in self.servers]
        return "[{}]".format(",".join(loads))


l = LoadBalancing()
l.add_connection("fdca:83d2::f20d")
print(l.avg_load())

l.servers.append(Server())
print(l.avg_load())

l.close_connection("fdca:83d2::f20d")
print(l.avg_load())


for connection in range(20):
    l.add_connection(connection)
print(l) #All the data should be less than 50