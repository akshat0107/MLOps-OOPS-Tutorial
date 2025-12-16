class chatbook:
    __user_id = 0

    def __init__(self)->None:
        self.id = chatbook.__user_id
        chatbook.__user_id += 1
        self.__name = "Default User"
        self.username = ''
        self.password = ''
        self.loggedin = False
        # self.menu()
    

    @staticmethod
    def get_id():
        return chatbook.__user_id
    
    @staticmethod
    def set_id(val):
        chatbook.__user_id = val

    def get_id_user(self):
        return self.id
    
    def set_id_user(self,value):
        self.id = value

    def menu(self):
        user_input = input("""Welcome to chatbook! How would you like to proceed?
                           1. Press 1 to signup
                           2. Press 2 to signin
                           3. Press 3 to write a post
                           4. Press 4 to message a friend
                           5. Press any other key to exit""")
        
        if user_input=="1":
            self.signup()
        elif user_input=="2":
            self.signin()
        elif user_input=="3":
            self.mypost()
        elif user_input=="4":
            self.sendmsg()
        else:
            exit()

    def signup(self):
        email = input("enter your email here -> ")
        password = input("setup your password here -> ")
        self.username = email
        self.password = password
        print("you have signed up successfully!!\n")
        self.menu()

    def signin(self):
        if self.username=='' and self.password=='':
            print("Please signup first by pressing 1 in the main menu")

        else:
            uname = input("enter your email/user name -> ")
            pwd = input("Enter your password here -> ")
            if self.username==uname and self.password == pwd:
                print("you have signed in successfully!")
                self.loggedin = True

            else:
                print("Please input correct credentials\n")
        
        print("\n")
        self.menu()

    def mypost(self):
        if self.loggedin==True:
            txt = input("enter your message here -> ")
            print(f"following content has been posted -> {txt}")

        else:
            print("you need to signin to post something")

        print("\n")
        self.menu()


    def sendmsg(self):
        if self.loggedin==True:
            txt = input("enter your message here -> ")
            frnd = input("Whom to send the message? -> ")
            print(f"your message has been sent to {frnd}")

        else:
            print("you need to signin first to post something")

        print("\n")
        self.menu()

obj = chatbook()
