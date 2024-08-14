def display_welcome_message():
    print("+" + "-"*38 + "+")
    print("|" + " " * 11 + "Welcome to Cricbuzz" + " " * 11 + "|")
    print("|" + " " * 38 + "|")
    print("|" + "Your one-stop destination for all things cricket!" + "|")
    print("+" + "-"*38 + "+")
    print()

def display_main_menu():
    print("+" + "-"*38 + "+")
    print("|" + " " * 14 + "Cricbuzz Menu" + " " * 14 + "|")
    print("|" + " " * 38 + "|")
    print("| 1. Live Scores" + " " * 23 + "|")
    print("| 2. Schedule" + " " * 26 + "|")
    print("| 3. News" + " " * 30 + "|")
    print("| 4. Series" + " " * 28 + "|")
    print("| 5. Teams" + " " * 29 + "|")
    print("| 6. Rankings" + " " * 26 + "|")
    print("| 7. Exit" + " " * 31 + "|")
    print("+" + "-"*38 + "+")

def display_live_scores_menu():
    print("\nLive Scores Menu:")
    print("1. Current Matches")
    print("2. Recent Matches")
    print("3. Upcoming Matches")
    print("4. Back to Main Menu")

def display_schedule_menu():
    print("\nSchedule Menu:")
    print("1. Upcoming Matches")
    print("2. Team Schedules")
    print("3. Series Schedules")
    print("4. Back to Main Menu")

def display_news_menu():
    print("\nNews Menu:")
    print("1. Latest News")
    print("2. Top Stories")
    print("3. Back to Main Menu")

def display_series_menu():
    print("\nSeries Menu:")
    print("1. Current Series")
    print("2. Upcoming Series")
    print("3. Back to Main Menu")

def display_teams_menu():
    print("\nTeams Menu:")
    print("1. International Teams")
    print("2. Domestic Teams")
    print("3. Back to Main Menu")

def display_rankings_menu():
    print("\nRankings Menu:")
    print("1. Team Rankings")
    print("2. Player Rankings")
    print("3. Back to Main Menu")

def main():
    display_welcome_message()
    
    while True:
        display_main_menu()
        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            while True:
                display_live_scores_menu()
                sub_choice = input("Enter your choice (1-4): ")
                if sub_choice == '1':
                    print("Displaying Current Matches...")
                elif sub_choice == '2':
                    print("Displaying Recent Matches...")
                elif sub_choice == '3':
                    print("Displaying Upcoming Matches...")
                elif sub_choice == '4':
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and 4.")
        
        elif choice == '2':
            while True:
                display_schedule_menu()
                sub_choice = input("Enter your choice (1-4): ")
                if sub_choice == '1':
                    print("Displaying Upcoming Matches...")
                elif sub_choice == '2':
                    print("Displaying Team Schedules...")
                elif sub_choice == '3':
                    print("Displaying Series Schedules...")
                elif sub_choice == '4':
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and 4.")

        elif choice == '3':
            while True:
                display_news_menu()
                sub_choice = input("Enter your choice (1-3): ")
                if sub_choice == '1':
                    print("Displaying Latest News...")
                elif sub_choice == '2':
                    print("Displaying Top Stories...")
                elif sub_choice == '3':
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and 3.")

        elif choice == '4':
            while True:
                display_series_menu()
                sub_choice = input("Enter your choice (1-3): ")
                if sub_choice == '1':
                    print("Displaying Current Series...")
                elif sub_choice == '2':
                    print("Displaying Upcoming Series...")
                elif sub_choice == '3':
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and 3.")

        elif choice == '5':
            while True:
                display_teams_menu()
                sub_choice = input("Enter your choice (1-3): ")
                if sub_choice == '1':
                    print("Displaying International Teams...")
                elif sub_choice == '2':
                    print("Displaying Domestic Teams...")
                elif sub_choice == '3':
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and 3.")

        elif choice == '6':
            while True:
                display_rankings_menu()
                sub_choice = input("Enter your choice (1-3): ")
                if sub_choice == '1':
                    print("Displaying Team Rankings...")
                elif sub_choice == '2':
                    print("Displaying Player Rankings...")
                elif sub_choice == '3':
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and 3.")

        elif choice == '7':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()
