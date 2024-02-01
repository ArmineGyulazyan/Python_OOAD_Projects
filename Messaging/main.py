import Users
import Conversations
import Messages

def main():

    user1 = Users.User('Lia','012336655')
    user2 = Users.User('Mia','012636635')
    user3 = Users.User('Tia','012633335')
    conv = Conversations.Conversation('handipum',user1)
    text_msg = Messages.Text(['good','haha','stupid'],txtt='hello')
    text_msg2 = Messages.Text(['good','haha','eh'],txtt='jamy 2-in aygu mot')
    conv.add_user(user2)
    conv.add_user(user3)
    conv.is_part(user2)
    conv.send_message(user2,text_msg)
    conv.search_messages(user2,text_msg)
    conv.send_message(user3,text_msg2)


if __name__ == '__main__':
    main()
