import Users
import Posts
import Comments


def main():
    user1 = Users.User('Lia','022556688')
    pic = Posts.Image(user1,'my pic','03/03/2024','jpg')
    comm = Comments.Comment(user1,pic,'nice one')

    pic.add_post()
    pic.react('good')
    comm.add_comment(user1)
    comm.view_comments()


if __name__ == '__main__':
    main()
