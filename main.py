from users import actions
print("Welcome to your notes assistant")


user_input = input("""What do you want to do?:

        -Login(l)
        -Sign up(s)
""")

action = actions.Actions()

if user_input == "s":
    action.register()
elif user_input == "l":
    action.login()
else:
    print("Unknown action please try again.")