import time
import threading
import pymongo
import socket


##hello ani
time.sleep(2)
'Chat Room Connection - Client-To-Client'
host = '172.22.0.1'
port = 60655
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Using TCP
server.bind((host, port))                                       
server.listen()
clients = []
aliases = []                                                        


myclient = pymongo.MongoClient("mongodb://localhost:27017/")       
mydb = myclient["Chat_Room"]
mycol = mydb["User_Data"]
    
a = 0
for x in mycol.find():
    if('session' in x):
        # print(x['session'])
        if(x['session']!=None):
            a = x['session']
session_number = a+1
print(session_number)


def database(message):##,session):

    # session_number = session(message)
    message = message.decode()

    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["Chat_Room"]
    mycol = mydb["User_Data"]
    insert_data = {"message":message,"session":session_number}
    x = mycol.insert_one(insert_data)
    print("Message inserted in the database!!")
    print(message)

def broadcast(message):
    for client in clients:
        client.send(message)

# Function to handle clients'connections
def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
            database(message)
            # print(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            alias = aliases[index]
            broadcast(f'{alias} has left the chat room!'.encode('utf-8'))
            aliases.remove(alias)
            break

# Main function to receive the clients connection

def receive(): 
    while True:
        print('Server is running and listening ...')
        client, address = server.accept()
        print(f'connection is established with {str(address)}')
        client.send('alias?'.encode('utf-8'))
        alias = client.recv(1024)
        aliases.append(alias)
        clients.append(client)
        print(f'The alias of this client is {alias}'.encode('utf-8'))
        broadcast(f'{alias} has connected to the chat room'.encode('utf-8'))
        client.send('you are now connected!'.encode('utf-8'))
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

if __name__ == "__main__":
    receive()
