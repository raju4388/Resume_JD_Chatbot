def chatbot():

    print("\n================================")
    print("   Resume-JD Matching Chatbot")
    print("================================")

    print("\nCommands:")
    print("1. analysis")
    print("2. skills")
    print("3. suggestions")
    print("4. courses")
    print("5. exit")

    while True:

        command = input("\nYou: ").lower()

        if command == "exit":
            print("Bot: Thank you!")
            break

        elif command == "analysis":
            print("Bot: Resume-JD analysis will be displayed here.")

        elif command == "skills":
            print("Bot: Matched and missing skills will be displayed here.")

        elif command == "suggestions":
            print("Bot: Resume improvement suggestions will be displayed here.")

        elif command == "courses":
            print("Bot: Recommended courses will be displayed here.")

        else:
            print("Bot: Please enter a valid command.")