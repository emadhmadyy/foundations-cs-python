import json


def tranformJsonToDic():
    with open("assignment_04_Emad_Hmady\graph.json") as json_file:
        data = json.load(json_file)
    return data


def printMenu():
    while True:
        print("1. Add a user to the platform.\n" +
              "2. Remove a user from the platform.\n" +
              "3. Send a friend request to another user.\n" +
              "4. Remove a friend from your list.\n" +
              "5. View your list of friends.\n" +
              "6. View the list of users on the platform.\n" +
              "7. Exit\n" +
              "- - - - - - - - - - - - - - -")
        try:
            choice_from_menu_user_input = int(input("Enter a choice: "))
            assert 1 <= choice_from_menu_user_input <= 7
            return choice_from_menu_user_input
        except ValueError:
            print("Enter an integer")
        except AssertionError:
            print("Make a choice between 1 and 7")


def addUser(dic):
    username = input("Choose your username: ")
    if (len(dic) == 0):
        dic[username] = []
    else:
        while True:
            exists = False
            for key in dic:
                if (username == key):
                    exists = True
                    break
            if (exists == True):
                print("User already exists")
                username = input("Choose another username: ")
            else:
                dic[username] = []
                break


def removeUser(dic):
    user = input(
        "Enter the username that you want to delete from the platform: ")
    while True:
        if (user in dic):
            for i in dic[user]:
                dic[i].remove(user)
            dic.pop(user)
            break
        else:
            print("User doesn't exist")
            user = input("Choose another username: ")


def addConnection(dic):
    user1 = input("Enter first username: ")
    user2 = input("Enter second username: ")
    if ((user1 in dic) and (user2 in dic)):
        if (user1 in dic[user2] or user2 in dic[user1]):
            print("These users are already connected")
        else:
            dic[user1].append(user2)
            dic[user2].append(user1)
    elif ((user1 not in dic) and (user2 not in dic)):
        print(user1 + " and " + user2 + " doesn't exist")
    elif ((user1 in dic) and (user2 not in dic)):
        print(user2 + " doesn't exist")
    else:
        print(user1 + " doesn't exist")


def removeConnection(dic):
    user1 = input("Enter first username: ")
    user2 = input("Enter second username: ")
    if ((user1 in dic) and (user2 in dic)):
        try:
            dic[user1].remove(user2)
            dic[user2].remove(user1)
        except Exception:
            print("Users aren't connected!")


def viewListOfFriends(dic):
    user = input("Enter username: ")
    if (user in dic):
        print(dic[user])
    else:
        print("User doesn't exist!")


def printAllUsers(dic):
    print(list(dic))


def transformDicToJson(dic):
    with open("assignment_04_Emad_Hmady\graph.json", "w") as jsonfile:
        json.dump(dic, jsonfile, indent=4)


def main():
    users_list = tranformJsonToDic()
    close_program = False
    while (close_program == False):
        choice_from_menu_user_input = printMenu()
        match choice_from_menu_user_input:
            case 1:
                addUser(users_list)
            case 2:
                removeUser(users_list)
            case 3:
                addConnection(users_list)
            case 4:
                removeConnection(users_list)
            case 5:
                viewListOfFriends(users_list)
            case 6:
                printAllUsers(users_list)
            case 7:
                transformDicToJson(users_list)
                close_program = True


main()
