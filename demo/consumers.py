from channels import Group
from demo.utils import log_to_terminal

def ws_connect(message):
    print "User connnected via Socket"


def ws_message(message):
    print "Message recieved from client side and the content is ", message.content['text']
    socketid = message.content['text']
    Group(socketid).add(message.reply_channel)
    log_to_terminal(socketid, {"info": "User added to the Channel Group"})
