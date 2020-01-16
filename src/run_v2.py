from v2.gamego import User, main


if __name__ == "__main__":
    user = User(1, "D2emon")
    program_name = "abermud"

    main(user, program_name, user.name)
