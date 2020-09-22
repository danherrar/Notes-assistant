import users.user as model
import notes.actions

class Actions:

    def register(self):
        print("\n" + "**************ok***************")

        name = input("Please enter your name: ")
        email = input("Please enter your email: ")
        password = input("Please enter your password: ")

        user = model.User(name, email, password)
        register = user.register()

        if register[0] >= 1:
            print(f"ok!! {register[1].name} you have registered with the email {register[1].email}")
        else:
            print("Something has gone wrong, you have registered incorrectly")

    def login(self):
        print("\n" + "**************ok***************")

        try:

            email = input("Please enter your email: ")
            password = input("Please enter your password: ")

            user = model.User("", email, password)

            login = user.indentify()

            if email == login[2]:
                print(f"\nWelcome {login[1]} !!!")

                self.nextActions(login)

        except:

            print("\n")
            print("-----Failed login-------")
            print("Wrong password or email.")
            
    def nextActions(self, user):

        print("What do you want to do?:")
        print("""
        -New note(n)
        -Show note(h)
        -Delete note(e)
        -Quit(q)
        """)
        note_action = notes.actions.Actions()
        action = input()

        if action == "n":
            note_action.create(user)
            self.nextActions(user)

        elif action == "h":
            note_action.show(user)
            self.nextActions(user)

        elif action == "e":
            note_action.delete(user)
            self.nextActions(user)

        elif action == "q":
           print("bye bro")

           exit()

        else:
            print("Unknown action please try again.")
            self.nextActions(user)

        

        return None

