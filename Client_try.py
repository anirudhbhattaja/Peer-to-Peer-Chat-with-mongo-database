import time
import threading
import socket
import pymongo
alias = input('Choose an alias >>> ')
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('192.168.240.176', 60655))

print("\n\n\n");

print("          #         #  ######   #       #######   ######   ##### ##### #######                                \n");
print("          #         #  #        #       #         #    #   #    #    # #                                      \n");
print("          #    #    #  ######   #       #         #    #   #    #    # #######                                \n");
print("          #    #    #  #        #       #         #    #   #         # #                                      \n");
print("          ##### #####  ######   ######  #######   ######   #         # #######                                \n");
print("                                                                                                           \n");

time.sleep(2)

# print("Would you like to know the chat history?")
# print("Enter 1 for yes and 0 for no")
# x = int(input())
# if(x == 1):

#     print("Enter the session number: ")
#     session_number = int(input())

#     myclient = pymongo.MongoClient("mongodb://localhost:27017/")
#     mydb = myclient["Chat_Room"]
#     mycol = mydb["User_Data"]

#     a = 0
#     for x in mycol.find():
#         if('session' in x):
#             if(x['session'] == session_number):
#                 print(x['message'])


def client_receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == "alias?":
                client.send(alias.encode('utf-8'))
            else:
                print(message)
        except:
            print('Error!')
            client.close()
            break


def client_send():
    while True:
        message = f'{alias}: {input("")}'
        client.send(message.encode('utf-8'))
        


receive_thread = threading.Thread(target=client_receive)
receive_thread.start()

send_thread = threading.Thread(target=client_send)
send_thread.start()