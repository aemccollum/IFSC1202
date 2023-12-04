class User:
    def __init__(self,username,password):
        self.UserName = username
        self.Password = password
class UserList:
    def __init__(self, filename):
        self.FileName = filename
        self.User_Obj = []
    def ReadUserFile(self):
        Userfile = open("Final Project Passwords.txt")
        x = Userfile.readline()
        for line in x:
            user_userpass = line.strip().split(',')
            username = user_userpass[0]
            password = user_userpass[1]
            user = User(username, password)
        Userfile.appends(UserList)
    def WriteUserFile(self):
        write_user = open((filename),'w')
        for i in range(UserList):
            filename.write(line)
        line = filename.readline()
    def DisplayUserList(self):
        print("{:>12s} {:>12s}".format("Username","Password"))
        print("{:>12s} {:>12s}".format("-"*12,"-"*12))
        x = studentsfile.readline()
        Userfile = open("Final Project Passwords.txt")
        x = Userfile.readline()
        while x!="":
            y = x.split(",")
            User1 = UserList(y[0].strip(),y[1].strip())
            print("{:>12s}{:>12s}".format(User1.UserName, User1.Password))
    def FindUsername(self, username):
        prompt_user = (input("Enter Username: "))
        UserList.index(prompt_user)
        if "":
            return -1
    def ChangePassword(self,username,password):
        user_list.FindUsername(prompt_user)
        if prompt_user == -1:
            print("Username Not Found")
    def AddUser(self,username,password):
        prompt_user = (input("Enter Username: "))
        user_list.FindUsername(prompt_user)
        if prompt_user == -1:
            print("User already taken.")
        if prompt_user != -1:
            prompt_user.append(UserList)
    def DeleteUser(self,username):
        prompt_user = (input("Enter Username: "))
        user_list.FindUsername(prompt_user)
        if index != -1:
            del self.user_list[index]
            print("User Deleted")
        if index == -1:
            print("Username Not Found")
    def Strength(self,password):
        score = 0
        if len(password) >= 8:
            score += 1
        if index(r"[A-Z]", password):
            score += 1
        if index(r"[a-z]", password):
            score += 1
        if index(r"[0-10]", password):
            score += 1
        if index(r"[~!@#$%^&*()_+|-={}[]:;<>?/]", password):
            score += 1
        return score
    if score == 5:
        print("User Added")
    if score <= 5:
        print("This password is weak",score)
def main():
    filename = "Final Project Passwords.txt"
    user_list = UserList(filename)
    UserList.ReadUserFile()
    print("1) Add a New User")
    print("2) Delete an Existing User")
    print("3) Change Password on Existing User")
    print("4) Display All Users")
    print("5) Save Changes to File")
    print("6) Quit")
    selection = (input("Enter Selection: "))
    if selection == "1":
        prompt_user = (input("Enter Username: "))
        user_list.FindUsername(prompt_user)
        if prompt_user == 0:
            print("Username Already in Use.")
        prompt_password = (input("Enter Password: "))
        if prompt_password.Strength() <= 5:
            print("This password is weak", score)
            prompt_password = (input("Enter Password: "))
        if prompt_password.Strength() == 5:
            user_list.AddUser(prompt_user,prompt_password)
            print("User Added")
    elif selection == "2":
        prompt_user = (input("Enter Username to Delete: "))
        user_list.FindUsername(prompt_user)
        if prompt_user == -1:
            print("Username Not Found")
        else:
            user_list.DeleteUser(prompt_user)
            print("User Deleted")
    elif selection == "3":
        prompt_user = (input("Enter Username to Change Password: "))
        user_list.FindUsername(prompt_user)
        if prompt_user == -1:
            print("Username Not Found")
        else:
            user_list.ChangePassword(prompt_user)
            prompt_password = (input("Enter New Password: "))
    elif selection == "4":
        user_list.DisplayUserList()
    elif selection == "5":
        user_list.WriteUserFile()
        print("Changes Saved")
    elif selection == "6":
        exit
    else:
        print("Invalid Selection")
    