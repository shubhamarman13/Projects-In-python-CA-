# Function to display the welcome message
def display_welcome_message():
    print("+" + "-"*38 + "+")
    print("|" + " " * 11 + "Welcome to Cricbuzz" + " " * 11 + "|")
    print("|" + " " * 38 + "|")
    print("|" + "Your one-stop destination for all cricket related things...!" + "|")
    print("+" + "-"*38 + "+")
    print()

# Function to display the main menu
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
    print("2. Back to Main Menu")

def display_current_matches():
    print("\nCurrent Matches:")
    print("+" + "-"*75 + "+")
    print("| SRI LANKA TOUR OF ENGLAND, 2024" + " " * 30 + "|")
    print("| Sri Lanka vs England, 1st Test" + " " * 29 + "|")
    print("| Aug 21 - Today  •  3:30 PM at Manchester, Emirates Old Trafford" + " " * 5 + "|")
    print("| SL236 & 326" + " " * 50 + "|")
    print("| ENG358 & 205-5" + " " * 45 + "|")
    print("| England won by 5 wkts" + " " * 47 + "|")
    print("+" + "-"*75 + "+")
    print("| NETHERLANDS T20I TRI-SERIES, 2024" + " " * 27 + "|")
    print("| Canada vs United States, 2nd T20I Match" + " " * 24 + "|")
    print("| Aug 24  •  7:30 PM at Utrecht, Sportpark Maarschalkerweerd" + " " * 4 + "|")
    print("| CAN169-5 (20 Ovs)" + " " * 53 + "|")
    print("| USA" + " " * 69 + "|")
    print("| No result - due to rain" + " " * 50 + "|")
    print("+" + "-"*75 + "+")
    print("| BANGLADESH TOUR OF PAKISTAN, 2024" + " " * 27 + "|")
    print("| Pakistan vs Bangladesh, 1st Test" + " " * 28 + "|")
    print("| Aug 21 - Today  •  10:30 AM at Rawalpindi, Rawalpindi Cricket Stadium" + " " * 2 + "|")
    print("| PAK448-6 d & 23-1" + " " * 51 + "|")
    print("| BAN565" + " " * 62 + "|")
    print("| Day 4: Stumps - Pakistan trail by 94 runs" + " " * 34 + "|")
    print("+" + "-"*75 + "+")
    print("| ICC MENS T20 WORLD CUP SUB REGIONAL EUROPE QUALIFIER C, 2024" + " " * 7 + "|")
    print("| Greece vs Cyprus, 11th Match, Group A" + " " * 31 + "|")
    print("| Aug 24  •  8:00 PM at Castel, King George V Sports Ground" + " " * 11 + "|")
    print("| GRC100 (19.4 Ovs)" + " " * 56 + "|")
    print("| CYP102-2 (12.2 Ovs)" + " " * 52 + "|")
    print("| Cyprus won by 8 wkts" + " " * 52 + "|")
    print("+" + "-"*75 + "+")
    print("| Bulgaria vs Estonia, 12th Match, Group B" + " " * 33 + "|")
    print("| Aug 24  •  8:00 PM at Port Soif, Guernsey Rovers Athletic Club Ground" + "|")
    print("| BGR129-8 (20 Ovs)" + " " * 55 + "|")
    print("| EST131-3 (17 Ovs)" + " " * 56 + "|")
    print("| Estonia won by 7 wkts" + " " * 53 + "|")
    print("+" + "-"*75 + "+")
    #print("\n2. Back to Main Menu")

def display_schedule_menu():
    print("\nSchedule Menu:")
    print("1. Upcoming Matches")
    print("2. Back to Main Menu")

def display_upcoming_matches():
    upcoming_matches = {
        "SAT, AUG 24 2024": [
            ("Bangladesh tour of Pakistan, 2024", "Pakistan vs Bangladesh, 1st Test, Day 4", "Rawalpindi Cricket Stadium, Rawalpindi", "10:30 AM", "05:00 AM GMT / 10:00 AM LOCAL"),
            ("ICC Mens T20 World Cup Sub Regional Europe Qualifier C, 2024", "Denmark vs Spain, 9th Match, Group A", "King George V Sports Ground, Castel", "3:00 PM", "09:30 AM GMT / 10:30 AM LOCAL")
        ],
        "SUN, AUG 25 2024": [
            ("Bangladesh tour of Pakistan, 2024", "Pakistan vs Bangladesh, 1st Test, Day 5", "Rawalpindi Cricket Stadium, Rawalpindi", "10:30 AM", "05:00 AM GMT / 10:00 AM LOCAL"),
            ("Netherlands T20I Tri-Series, 2024", "Netherlands vs United States, 3rd T20I Match", "Sportpark Maarschalkerweerd, Utrecht", "7:30 PM", "02:00 PM GMT / 04:00 PM LOCAL"),
            ("ICC Mens T20 World Cup Sub Regional Europe Qualifier C, 2024", "Bulgaria vs Malta, 13th Match, Group B", "King George V Sports Ground, Castel", "3:00 PM", "09:30 AM GMT / 10:30 AM LOCAL"),
            ("ICC Mens T20 World Cup Sub Regional Europe Qualifier C, 2024", "Cyprus vs Czech Republic, 14th Match, Group A", "Guernsey Rovers Athletic Club Ground, Port Soif", "3:00 PM", "09:30 AM GMT / 10:30 AM LOCAL"),
            ("ICC Mens T20 World Cup Sub Regional Europe Qualifier C, 2024", "Greece vs Spain, 16th Match, Group A", "Guernsey Rovers Athletic Club Ground, Port Soif", "8:00 PM", "02:30 PM GMT / 03:30 PM LOCAL"),
            ("ICC Mens T20 World Cup Sub Regional Europe Qualifier C, 2024", "Guernsey vs Estonia, 15th Match, Group B", "King George V Sports Ground, Castel", "8:00 PM", "02:30 PM GMT / 03:30 PM LOCAL"),
            ("Malaysia T20I Tri Nations Cup, 2024", "Kuwait vs Malaysia, 5th Match", "Selangor Turf Club, Kuala Lumpur", "8:00 AM", "02:30 AM GMT / 10:30 AM LOCAL")
        ],
        "MON, AUG 26 2024": [
            ("Netherlands T20I Tri-Series, 2024", "Netherlands vs United States, 4th T20I Match", "Sportpark Maarschalkerweerd, Utrecht", "5:30 PM", "12:00 PM GMT / 02:00 PM LOCAL"),
            ("South Africa tour of West Indies, 2024", "West Indies vs South Africa, 2nd T20I", "Brian Lara Stadium, Tarouba, Trinidad", "12:30 AM (Aug 26)", "07:00 PM GMT / 03:00 PM LOCAL"),
            ("Malaysia T20I Tri Nations Cup, 2024", "Hong Kong vs Malaysia, 6th Match", "Selangor Turf Club, Kuala Lumpur", "8:00 AM", "02:30 AM GMT / 10:30 AM LOCAL")
        ]
    }

    print("\nUpcoming Matches:")
    print("+" + "-"*75 + "+")
    for date, matches in upcoming_matches.items():
        print("| " + date + " " * (75 - len(date)) + "|")
        print("+" + "-"*75 + "+")
        for match in matches:
            print(f"| {match[0]:<40} | {match[1]:<40} | {match[2]:<25} | {match[3]:<8} | {match[4]:<28} |")
            print("+" + "-"*75 + "+")
    #print("\n2. Back to Main Menu")

def display_news_menu():
    print("\nNews Menu:")
    print("1. Latest News")
    print("2. Back to Main Menu")

def display_latest_news():
    news_items = [
        ("REPORTS • ENG V SL, 1ST TEST", "Root stars in England's jittery win in Manchester", "1h ago"),
        ("REPORTS • SRI LANKA TOUR OF ENGLAND, 2024", "England lose top-order in pursuit of 205", "4h ago"),
        ("NEWS • PAK V BAN, 1ST TEST", "Early strikes on Day 5 could seal historic win for Bangladesh, says Mehidy", "4h ago"),
        ("NEWS • BANGLADESH CRICKET", "BCB to take a call on Shakib's future after ongoing Rawalpindi Test", "5h ago"),
        ("REPORTS • BANGLADESH TOUR OF PAKISTAN, 2024", "Mushfiqur puts Bangladesh in driver's seat in Rawalpindi", "6h ago"),
        ("REPORTS • ENG V SL, 1ST TEST", "Kamindu Mendis, Dinesh Chandimal lift Sri Lanka's hopes", "7h ago"),
        ("NEWS • WOMEN'S LEAGUE 2", "Associates call for Women's League 2 after Championship snub", "7h ago"),
        ("NEWS • AUSTRALIAN CRICKET", "Josh Hazlewood ruled out of Scotland T20Is", "8h ago"),
        ("REPORTS • BANGLADESH TOUR OF PAKISTAN, 2024", "Rahim-Mehidy record stand propels Bangladesh into lead", "10h ago"),
        ("NEWS • PAK V BAN, 1ST TEST", "Rahim's ton helps Bangladesh reduce deficit", "13h ago"),
        ("REPORTS • SOUTH AFRICA TOUR OF WEST INDIES, 2024", "Pooran blitz powers West Indies to thumping win", "15h ago"),
        ("NEWS • FAREWELL", "Shikhar Dhawan announces retirement from all cricket", "17h ago"),
        ("NEWS • SRI LANKA'S TOUR OF ENGLAND, 2024", "Jamie Smith 'grateful' for mentor Ian Bell", "18h ago"),
        ("NEWS • WOMEN'S T20 WORLD CUP, 2024", "Nigar Sultana disappointed to not be playing a 'home World Cup'", "19h ago"),
        ("REPORTS • SRI LANKA TOUR OF ENGLAND 2024", "Bowlers deliver again to put England in command", "1d ago"),
        ("REPORTS • SRI LANKA TOUR OF ENGLAND, 2024", "Mathews resists but England chip away", "1d ago"),
        ("NEWS • BANGLADESH TOUR OF PAKISTAN, 2024", "Crime to get out for just 50 - Mominul on his batting", "1d ago"),
        ("REPORTS • BANGLADESH TOUR OF PAKISTAN, 2024", "Dogged Bangladesh batters fight to cut deficit", "1d ago"),
        ("NEWS • SRI LANKA TOUR OF ENGLAND, 1ST TEST", "Jamie Smith's maiden ton puts England in command", "1d ago")
    ]

    print("\nLatest News:")
    print("+" + "-"*80 + "+")
    print("| Category                                | Headline                                               | Time     |")
    print("+" + "-"*80 + "+")
    for item in news_items:
        print(f"| {item[0]:<40} | {item[1]:<50} | {item[2]:<8} |")
        print("+" + "-"*80 + "+")
    #print("\n2. Back to Main Menu")


# Function to display the teams menu
def display_teams_menu():
    print("\nTeams Menu:")
    print("1. International Teams")
    print("2. Domestic Teams")
    print("3. Back to Main Menu")

# Function to display stats (Most Runs and Most Wickets)
def display_stats(most_runs, most_wickets):
    # Most Runs
    print("\nMost Runs:")
    print("|" + "-"*81 + "|")
    print("| Player                  | Matches | Innings | Runs   | Avg   | SR    | 4s   | 6s   |")
    print("|-------------------------|---------|---------|--------|-------|-------|------|------|")
    for player, matches, innings, runs, avg, sr, fours, sixes in most_runs:
        print(f"| {player:<23} | {matches:>7} | {innings:>7} | {runs:>6} | {avg:>5.1f} | {sr:>5.1f} | {fours:>4} | {sixes:>4} |")

    # Most Wickets
    print("\nMost Wickets:")
    print("|" + "-"*77 + "|")
    print("| Player                  | Matches | Overs   | Balls  | Wkts  | Avg   | Runs  | 4-fers | 5-fers |")
    print("|-------------------------|---------|---------|--------|-------|-------|-------|--------|--------|")
    for player, matches, overs, balls, wkts, avg, runs, four_fers, five_fers in most_wickets:
        print(f"| {player:<23} | {matches:>7} | {overs:>7} | {balls:>6} | {wkts:>5} | {avg:>5.1f} | {runs:>5} | {four_fers:>6} | {five_fers:>6} |")
    
    print("+" + "-"*81 + "+")

# Function to display the full menu for a specific team
def display_team_menu(team_name, team_data):
    while True:
        print(f"\nTeam {team_name} Options:")
        print("1. Schedule")
        print("2. Result")
        print("3. Players")
        print("4. Stats")
        print("5. Back to Team Menu")

        team_option = input("Enter your choice (1-5): ").strip()

        if team_option == '1':
            print(f"\nDisplaying Schedule for Team {team_name}...")
            for date, match, venue, time in team_data["schedule"]:
                print(f"{date}: {match} at {venue} ({time})")
                
        elif team_option == '2':
            print(f"\nDisplaying Results for Team {team_name}...")
            for date, match, result in team_data["results"]:
                print(f"{date}: {match} - {result}")
                
        elif team_option == '3':
            print(f"\nDisplaying Players for Team {team_name}...")
            print("\nBATSMEN:")
            for player in team_data["players"]["batsmen"]:
                print(player)
            
            print("\nALL ROUNDER:")
            for player in team_data["players"]["all_rounders"]:
                print(player)
            
            print("\nWICKET KEEPER:")
            for player in team_data["players"]["wicket_keepers"]:
                print(player)
            
            print("\nBOWLER:")
            for player in team_data["players"]["bowlers"]:
                print(player)
            
        elif team_option == '4':
            display_stats(team_data["most_runs"], team_data["most_wickets"])

        elif team_option == '5':
            break  # Back to team menu
def display_rankings_menu():
    print("\nRankings Menu:")
    print("1. Team Rankings")
    print("2. Player Rankings")
    print("3. Back to Main Menu")
def display_boxed_text(text, width=40):
    border = "*" * (width + 4)
    lines = text.split('\n')
    boxed_text = [border]
    for line in lines:
        boxed_text.append(f"* {line.ljust(width)} *")
    boxed_text.append(border)
    return '\n'.join(boxed_text)

def display_series_menu():
    while True:
        menu_text = (
            "Series Menu\n"
            "1. ICC Mens T20 World Cup 2024\n"
            "2. Indian Premier League 2024\n"
            "3. Main Menu"
        )
        print(display_boxed_text(menu_text))

        choice = input("Select an option (1-3): ")

        if choice == '1':
            MensT20()
        elif choice == '2':
            IPL()
        elif choice == '3':
            print(display_boxed_text("Exiting..."))
            break
        else:
            print(display_boxed_text("Invalid choice. Please try again."))

def display_sub_menu_1(series_name):
    while True:
        menu_text = (
            f"{series_name} Sub-Menu\n"
            "1. Matches\n"
            "2. Table\n"
            "3. Squads\n"
            "4. Stats\n"
            "5. Back to Series Menu"
        )
        print(display_boxed_text(menu_text))

        choice = input("Select an option (1-5): ")

        if choice == '1':
            display_matches_1()
        elif choice == '2':
            display_table_1()
        elif choice == '3':
            display_t20_blast_squads_1()
        elif choice == '4':
            display_stats_1()
        elif choice == '5':
            break
        else:
            print(display_boxed_text("Invalid choice. Please try again."))

def display_sub_menu_2(series_name):
    while True:
        menu_text = (
            f"{series_name} Sub-Menu\n"
            "1. Matches\n"
            "2. Table\n"
            "3. Squads\n"
            "4. Stats\n"
            "5. Back to Series Menu"
        )
        print(display_boxed_text(menu_text))

        choice = input("Select an option (1-5): ")

        if choice == '1':
            display_matches_2()
        elif choice == '2':
            display_table_2()
        elif choice == '3':
            display_t20_blast_squads_1()
        elif choice == '4':
            display_stats_2()
        elif choice == '5':
            break
        else:
            print(display_boxed_text("Invalid choice. Please try again."))

def display_sub_menu_3(series_name):
    while True:
        menu_text = (
            f"{series_name} Sub-Menu\n"
            "1. Matches\n"
            "2. Table\n"
            "3. Squads\n"
            "4. Stats\n"
            "5. Back to Series Menu"
        )
        print(display_boxed_text(menu_text))

        choice = input("Select an option (1-5): ")

        if choice == '1':
            display_matches_3()
        elif choice == '2':
            display_table_3()
        elif choice == '3':
            display_ipl_squads()
        elif choice == '4':
            display_IPL_stats()
        elif choice == '5':
            break
        else:
            print(display_boxed_text("Invalid choice. Please try again."))

def MensT20():
    display_sub_menu_1("ICC Mens T20 World Cup 2024")

def IPL():
    display_sub_menu_3("Indian Premier League 2024")


def display_matches_1():
    matches = [
        ("1st Match", "Group A", "Lauderhill, Florida", "IND vs USA", "IND won by 8 wickets"),
        ("2nd Match", "Group A", "Edinburgh", "PAK vs CAN", "PAK won by 4 wickets"),
        ("3rd Match", "Group B", "Dubai", "AUS vs ENG", "AUS won by 6 runs"),
        ("4th Match", "Group B", "Dubai", "SCO vs NAM", "SCO won by 5 wickets"),
        ("5th Match", "Group C", "Abu Dhabi", "WI vs AFG", "WI won by 10 wickets"),
        ("6th Match", "Group C", "Abu Dhabi", "NZ vs UGA", "NZ won by 30 runs"),
        ("7th Match", "Group D", "Sharjah", "RSA vs BAN", "RSA won by 7 wickets"),
        ("8th Match", "Group D", "Sharjah", "SL vs NED", "SL won by 2 wickets"),
        ("9th Match", "Group D", "Sharjah", "NEP vs NED", "NED won by 5 wickets"),
        ("10th Match", "Group B", "Dubai", "ENG vs SCO", "ENG won by 12 runs"),
        ("Semi-Final 1", "Group Stage", "Dubai", "IND vs AFG", "IND won by 4 wickets"),
        ("Semi-Final 2", "Group Stage", "Dubai", "RSA vs WI", "RSA won by 6 wickets"),
        ("Final", "Group Stage", "Dubai", "IND vs RSA", "IND won by 8 wickets")
    ]
    print("\nMatch Details:")
    print(f"{'Match':<15} {'Stage':<15} {'Venue':<20} {'Teams':<15} {'Result':<20}")
    print("="*85)
    for match in matches:
        print(f"{match[0]:<15} {match[1]:<15} {match[2]:<20} {match[3]:<15} {match[4]:<20}")

def display_table_1():
    print("\nTable: T20 Blast 2024")

    # Super 8 Group 1
    print("\nSuper 8 Group 1")
    print(f"{'Team':<15} {'P':<3} {'W':<3} {'L':<3} {'NR':<3} {'Pts':<3} {'NRR':<5}")
    print("="*30)
    print(f"{'IND (Q)':<15} {3:<3} {3:<3} {0:<3} {0:<3} {6:<3} {+2.017:<5}")
    print(f"{'AFG (Q)':<15} {3:<3} {2:<3} {1:<3} {0:<3} {4:<3} {-0.305:<5}")
    print(f"{'AUS (E)':<15} {3:<3} {1:<3} {2:<3} {0:<3} {2:<3} {-0.331:<5}")
    print(f"{'BAN (E)':<15} {3:<3} {0:<3} {3:<3} {0:<3} {0:<3} {-1.709:<5}")

    # Super 8 Group 2
    print("\nSuper 8 Group 2")
    print(f"{'Team':<15} {'P':<3} {'W':<3} {'L':<3} {'NR':<3} {'Pts':<3} {'NRR':<5}")
    print("="*30)
    print(f"{'RSA (Q)':<15} {3:<3} {3:<3} {0:<3} {0:<3} {6:<3} {+0.780:<5}")
    print(f"{'ENG (Q)':<15} {3:<3} {2:<3} {1:<3} {0:<3} {4:<3} {+1.992:<5}")
    print(f"{'WI (E)':<15} {3:<3} {1:<3} {2:<3} {0:<3} {2:<3} {+0.686:<5}")
    print(f"{'USA (E)':<15} {3:<3} {0:<3} {3:<3} {0:<3} {0:<3} {-3.906:<5}")

    # Group D
    print("\nGroup D")
    print(f"{'Team':<15} {'P':<3} {'W':<3} {'L':<3} {'NR':<3} {'Pts':<3} {'NRR':<5}")
    print("="*30)
    print(f"{'RSA (Q)':<15} {4:<3} {4:<3} {0:<3} {0:<3} {8:<3} {+0.470:<5}")
    print(f"{'BAN (Q)':<15} {4:<3} {3:<3} {1:<3} {0:<3} {6:<3} {+0.616:<5}")
    print(f"{'SL (E)':<15} {4:<3} {1:<3} {2:<3} {1:<3} {3:<3} {+0.863:<5}")
    print(f"{'NED (E)':<15} {4:<3} {1:<3} {3:<3} {0:<3} {2:<3} {-1.358:<5}")
    print(f"{'NEP (E)':<15} {4:<3} {0:<3} {4:<3} {1:<3} {1:<3} {-0.542:<5}")

    # Group C
    print("\nGroup C")
    print(f"{'Team':<15} {'P':<3} {'W':<3} {'L':<3} {'NR':<3} {'Pts':<3} {'NRR':<5}")
    print("="*30)
    print(f"{'WI (Q)':<15} {4:<3} {4:<3} {0:<3} {0:<3} {8:<3} {+3.257:<5}")
    print(f"{'AFG (Q)':<15} {4:<3} {3:<3} {1:<3} {0:<3} {6:<3} {+1.835:<5}")
    print(f"{'NZ (E)':<15} {4:<3} {2:<3} {2:<3} {0:<3} {4:<3} {+0.415:<5}")
    print(f"{'UGA (E)':<15} {4:<3} {1:<3} {3:<3} {0:<3} {2:<3} {-4.510:<5}")
    print(f"{'PNG (E)':<15} {4:<3} {0:<3} {4:<3} {0:<3} {0:<3} {-2.107:<5}")

    # Group B
    print("\nGroup B")
    print(f"{'Team':<15} {'P':<3} {'W':<3} {'L':<3} {'NR':<3} {'Pts':<3} {'NRR':<5}")
    print("="*30)
    print(f"{'AUS (Q)':<15} {4:<3} {4:<3} {0:<3} {0:<3} {8:<3} {+2.791:<5}")
    print(f"{'ENG (Q)':<15} {4:<3} {2:<3} {1:<3} {1:<3} {5:<3} {+3.611:<5}")
    print(f"{'SCO (E)':<15} {4:<3} {2:<3} {1:<3} {1:<3} {5:<3} {+1.255:<5}")
    print(f"{'NAM (E)':<15} {4:<3} {1:<3} {3:<3} {0:<3} {2:<3} {-2.529:<5}")
    print(f"{'OMAN (E)':<15} {4:<3} {0:<3} {4:<3} {0:<3} {0:<3} {-3.062:<5}")

    # Group A
    print("\nGroup A")
    print(f"{'Team':<15} {'P':<3} {'W':<3} {'L':<3} {'NR':<3} {'Pts':<3} {'NRR':<5}")
    print("="*30)
    print(f"{'IND (Q)':<15} {4:<3} {3:<3} {0:<3} {1:<3} {7:<3} {+1.137:<5}")
    print(f"{'USA (Q)':<15} {4:<3} {2:<3} {1:<3} {1:<3} {5:<3} {+0.127:<5}")
    print(f"{'PAK (E)':<15} {4:<3} {2:<3} {2:<3} {0:<3} {4:<3} {+0.294:<5}")
    print(f"{'CAN (E)':<15} {4:<3} {1:<3} {2:<3} {1:<3} {3:<3} {-0.493:<5}")
    print(f"{'IRE (E)':<15} {4:<3} {0:<3} {3:<3} {1:<3} {1:<3} {-0.594:<5}")

def display_squads_1(series_name):
    if series_name == "T20 Blast 2024":
        display_t20_blast_squads()
    else:
        print("Squad details for this series are not available.")

def display_t20_blast_squads_1():
    print("\nIndian Squad:")
    print(f"{'Category':<20} {'Player ID':<20} {'Name':<20} {'Role':<20}")
    print("="*80)
    print(f"{'BATTERS':<20} {'rohit-sharma':<20} {'Rohit Sharma':<20} {'Batter':<20}")
    print(f"{'BATTERS':<20} {'yashasvi-jaiswal':<20} {'Yashasvi Jaiswal':<20} {'Batter':<20}")
    print(f"{'BATTERS':<20} {'virat-kohli':<20} {'Virat Kohli':<20} {'Batter':<20}")
    print(f"{'BATTERS':<20} {'suryakumar-yadav':<20} {'Suryakumar Yadav':<20} {'Batter':<20}")
    print(f"{'ALL ROUNDERS':<20} {'hardik-pandya':<20} {'Hardik Pandya':<20} {'Batting Allrounder':<20}")
    print(f"{'ALL ROUNDERS':<20} {'shivam-dube':<20} {'Shivam Dube':<20} {'Batting Allrounder':<20}")
    print(f"{'ALL ROUNDERS':<20} {'ravindra-jadeja':<20} {'Ravindra Jadeja':<20} {'Bowling Allrounder':<20}")
    print(f"{'ALL ROUNDERS':<20} {'axar-patel':<20} {'Axar Patel':<20} {'Bowling Allrounder':<20}")
    print(f"{'WICKET KEEPERS':<20} {'rishabh-pant':<20} {'Rishabh Pant':<20} {'WK-Batter':<20}")
    print(f"{'WICKET KEEPERS':<20} {'sanju-samson':<20} {'Sanju Samson':<20} {'WK-Batter':<20}")
    print(f"{'BOWLERS':<20} {'kuldeep-yadav':<20} {'Kuldeep Yadav':<20} {'Bowler':<20}")
    print(f"{'BOWLERS':<20} {'yuzvendra-chahal':<20} {'Yuzvendra Chahal':<20} {'Bowler':<20}")
    print(f"{'BOWLERS':<20} {'arshdeep-singh':<20} {'Arshdeep Singh':<20} {'Bowler':<20}")
    print(f"{'BOWLERS':<20} {'jasprit-bumrah':<20} {'Jasprit Bumrah':<20} {'Bowler':<20}")
    print(f"{'BOWLERS':<20} {'mohammed-siraj':<20} {'Mohammed Siraj':<20} {'Bowler':<20}")

    print("\nEngland Squad:")
    print(f"{'Category':<20} {'Player ID':<20} {'Name':<20} {'Role':<20}")
    print("="*80)
    print(f"{'BATTERS':<20} {'harry-brook':<20} {'Harry Brook':<20} {'Batter':<20}")
    print(f"{'BATTERS':<20} {'ben-duckett':<20} {'Ben Duckett':<20} {'Batter':<20}")
    print(f"{'ALL ROUNDERS':<20} {'moeen-ali':<20} {'Moeen Ali':<20} {'Batting Allrounder':<20}")
    print(f"{'ALL ROUNDERS':<20} {'will-jacks':<20} {'Will Jacks':<20} {'Batting Allrounder':<20}")
    print(f"{'ALL ROUNDERS':<20} {'liam-livingstone':<20} {'Liam Livingstone':<20} {'Batting Allrounder':<20}")
    print(f"{'ALL ROUNDERS':<20} {'sam-curran':<20} {'Sam Curran':<20} {'Bowling Allrounder':<20}")
    print(f"{'WICKET KEEPERS':<20} {'jos-buttler':<20} {'Jos Buttler':<20} {'WK-Batter':<20}")
    print(f"{'WICKET KEEPERS':<20} {'jonny-bairstow':<20} {'Jonny Bairstow':<20} {'WK-Batter':<20}")
    print(f"{'WICKET KEEPERS':<20} {'philip-salt':<20} {'Philip Salt':<20} {'WK-Batter':<20}")
    print(f"{'BOWLERS':<20} {'jofra-archer':<20} {'Jofra Archer':<20} {'Bowler':<20}")
    print(f"{'BOWLERS':<20} {'tom-hartley':<20} {'Tom Hartley':<20} {'Bowler':<20}")
    print(f"{'BOWLERS':<20} {'chris-jordan':<20} {'Chris Jordan':<20} {'Bowler':<20}")
    print(f"{'BOWLERS':<20} {'adil-rashid':<20} {'Adil Rashid':<20} {'Bowler':<20}")
    print(f"{'BOWLERS':<20} {'reece-topley':<20} {'Reece Topley':<20} {'Bowler':<20}")
    print(f"{'BOWLERS':<20} {'mark-wood':<20} {'Mark Wood':<20} {'Bowler':<20}")

    print("\nSouth Africa Squad:")
    print(f"{'Category':<20} {'Player ID':<20} {'Name':<20} {'Role':<20}")
    print("="*80)
    print(f"{'BATTERS':<20} {'aiden-markram':<20} {'Aiden Markram (Captain)':<20} {'Batter':<20}")
    print(f"{'BATTERS':<20} {'reeza-hendricks':<20} {'Reeza Hendricks':<20} {'Batter':<20}")
    print(f"{'BATTERS':<20} {'david-miller':<20} {'David Miller':<20} {'Batter':<20}")
    print(f"{'ALL ROUNDERS':<20} {'marco-jansen':<20} {'Marco Jansen':<20} {'Bowling Allrounder':<20}")
    print(f"{'WICKET KEEPERS':<20} {'quinton-de-kock':<20} {'Quinton de Kock':<20} {'WK-Batter':<20}")
    print(f"{'WICKET KEEPERS':<20} {'heinrich-klaasen':<20} {'Heinrich Klaasen':<20} {'WK-Batter':<20}")
    print(f"{'WICKET KEEPERS':<20} {'ryan-rickelton':<20} {'Ryan Rickelton':<20} {'WK-Batter':<20}")
    print(f"{'WICKET KEEPERS':<20} {'tristan-stubbs':<20} {'Tristan Stubbs':<20} {'WK-Batter':<20}")
    print(f"{'BOWLERS':<20} {'ottneil-baartman':<20} {'Ottneil Baartman':<20} {'Bowler':<20}")
    print(f"{'BOWLERS':<20} {'gerald-coetzee':<20} {'Gerald Coetzee':<20} {'Bowler':<20}")
    print(f"{'BOWLERS':<20} {'bjorn-fortuin':<20} {'Bjorn Fortuin':<20} {'Bowler':<20}")
    print(f"{'BOWLERS':<20} {'keshav-maharaj':<20} {'Keshav Maharaj':<20} {'Bowler':<20}")
    print(f"{'BOWLERS':<20} {'anrich-nortje':<20} {'Anrich Nortje':<20} {'Bowler':<20}")
    print(f"{'BOWLERS':<20} {'kagiso-rabada':<20} {'Kagiso Rabada':<20} {'Bowler':<20}")
    print(f"{'BOWLERS':<20} {'tabraiz-shamsi':<20} {'Tabraiz Shamsi':<20} {'Bowler':<20}")

    print("\nAustralia Squad:")
    print(f"{'Category':<20} {'Player ID':<20} {'Name':<20} {'Role':<20}")
    print("="*80)
    print(f"{'BATTERS':<20} {'tim-david':<20} {'Tim David':<20} {'Batter':<20}")
    print(f"{'BATTERS':<20} {'travis-head':<20} {'Travis Head':<20} {'Batter':<20}")
    print(f"{'BATTERS':<20} {'david-warner':<20} {'David Warner':<20} {'Batter':<20}")
    print(f"{'ALL ROUNDERS':<20} {'mitchell-marsh':<20} {'Mitchell Marsh (Captain)':<20} {'Batting Allrounder':<20}")
    print(f"{'ALL ROUNDERS':<20} {'cameron-green':<20} {'Cameron Green':<20} {'Batting Allrounder':<20}")
    print(f"{'ALL ROUNDERS':<20} {'glenn-maxwell':<20} {'Glenn Maxwell':<20} {'Batting Allrounder':<20}")
    print(f"{'ALL ROUNDERS':<20} {'marcus-stoinis':<20} {'Marcus Stoinis':<20} {'Batting Allrounder':<20}")
    print(f"{'ALL ROUNDERS':<20} {'ashton-agar':<20} {'Ashton Agar':<20} {'Bowling Allrounder':<20}")
    print(f"{'WICKET KEEPERS':<20} {'josh-inglis':<20} {'Josh Inglis':<20} {'WK-Batter':<20}")
    print(f"{'WICKET KEEPERS':<20} {'matthew-wade':<20} {'Matthew Wade':<20} {'WK-Batter':<20}")
    print(f"{'BOWLERS':<20} {'pat-cummins':<20} {'Pat Cummins':<20} {'Bowler':<20}")
    print(f"{'BOWLERS':<20} {'nathan-ellis':<20} {'Nathan Ellis':<20} {'Bowler':<20}")
    print(f"{'BOWLERS':<20} {'josh-hazlewood':<20} {'Josh Hazlewood':<20} {'Bowler':<20}")
    print(f"{'BOWLERS':<20} {'mitchell-starc':<20} {'Mitchell Starc':<20} {'Bowler':<20}")
    print(f"{'BOWLERS':<20} {'adam-zampa':<20} {'Adam Zampa':<20} {'Bowler':<20}")


def display_stats_1():
    print("\nT20 Blast 2024 Stats")

    # Most Runs
    print("\nMost Runs:")
    print(f"{'Batter':<20} {'M':<5} {'I':<5} {'R':<5} {'Avg':<10}")
    print("="*45)
    print(f"{'Gurbaz':<20} {8:<5} {8:<5} {281:<5} {35.12:<10}")
    print(f"{'Rohit':<20} {8:<5} {8:<5} {257:<5} {36.71:<10}")
    print(f"{'Head':<20} {7:<5} {7:<5} {255:<5} {42.50:<10}")
    print(f"{'de Kock':<20} {9:<5} {9:<5} {243:<5} {27.00:<10}")
    print(f"{'Ibrahim Zadran':<20} {8:<5} {8:<5} {231:<5} {28.88:<10}")
    print(f"{'Pooran':<20} {7:<5} {7:<5} {228:<5} {38.00:<10}")
    print(f"{'Andries Gous':<20} {6:<5} {6:<5} {219:<5} {43.80:<10}")
    print(f"{'Jos Buttler':<20} {8:<5} {7:<5} {214:<5} {42.80:<10}")
    print(f"{'Suryakumar Yadav':<20} {8:<5} {8:<5} {199:<5} {28.43:<10}")
    print(f"{'Klaasen':<20} {9:<5} {8:<5} {190:<5} {31.67:<10}")
    print(f"{'Salt':<20} {8:<5} {7:<5} {188:<5} {37.60:<10}")
    print(f"{'Warner':<20} {7:<5} {7:<5} {178:<5} {29.67:<10}")
    print(f"{'Pant':<20} {8:<5} {8:<5} {171:<5} {24.43:<10}")
    print(f"{'David Miller':<20} {9:<5} {8:<5} {169:<5} {28.17:<10}")
    print(f"{'Stoinis':<20} {7:<5} {5:<5} {169:<5} {42.25:<10}")

    # Highest Scores
    print("\nHighest Scores:")
    print(f"{'Batter':<20} {'HS':<5} {'Balls':<6} {'SR':<6} {'Vs':<5}")
    print("="*40)
    print(f"{'Pooran':<20} {98:<5} {53:<6} {184.91:<6} {'AFG':<5}")
    print(f"{'Aaron Jones':<20} {94:<5} {40:<6} {235.00:<6} {'CAN':<5}")
    print(f"{'Rohit':<20} {92:<5} {41:<6} {224.39:<6} {'AUS':<5}")
    print(f"{'Salt':<20} {87:<5} {47:<6} {185.11:<6} {'WI':<5}")
    print(f"{'Jos Buttler':<20} {83:<5} {38:<6} {218.42:<6} {'USA':<5}")
    print(f"{'Shai Hope':<20} {82:<5} {39:<6} {210.26:<6} {'USA':<5}")
    print(f"{'Andries Gous':<20} {80:<5} {47:<6} {170.21:<6} {'RSA':<5}")
    print(f"{'Gurbaz':<20} {80:<5} {56:<6} {142.86:<6} {'NZ':<5}")
    print(f"{'Head':<20} {76:<5} {43:<6} {176.74:<6} {'IND':<5}")
    print(f"{'Gurbaz':<20} {76:<5} {45:<6} {168.89:<6} {'UGA':<5}")
    print(f"{'Kohli':<20} {76:<5} {59:<6} {128.81:<6} {'RSA':<5}")
    print(f"{'de Kock':<20} {74:<5} {40:<6} {185.00:<6} {'USA':<5}")
    print(f"{'Ibrahim Zadran':<20} {70:<5} {46:<6} {152.17:<6} {'UGA':<5}")
    print(f"{'Sherfane Rutherford':<20} {68:<5} {39:<6} {174.36:<6} {'NZ':<5}")
    print(f"{'Head':<20} {68:<5} {49:<6} {138.78:<6} {'SCO':<5}")

    # Best Batting Average
    print("\nBest Batting Average:")
    print(f"{'Batter':<20} {'M':<5} {'I':<5} {'R':<5} {'Avg':<10}")
    print("="*45)
    print(f"{'Berrington':<20} {4:<5} {3:<5} {102:<5} {102.00:<10}")
    print(f"{'Harry Brook':<20} {8:<5} {4:<5} {145:<5} {72.50:<10}")
    print(f"{'Brandon McMullen':<20} {4:<5} {3:<5} {140:<5} {70.00:<10}")
    print(f"{'Shai Hope':<20} {3:<5} {3:<5} {107:<5} {53.50:<10}")
    print(f"{'Hardik Pandya':<20} {8:<5} {6:<5} {144:<5} {48.00:<10}")
    print(f"{'Roston Chase':<20} {6:<5} {3:<5} {94:<5} {47.00:<10}")
    print(f"{'Andries Gous':<20} {6:<5} {6:<5} {219:<5} {43.80:<10}")
    print(f"{'Jos Buttler':<20} {8:<5} {7:<5} {214:<5} {42.80:<10}")
    print(f"{'Head':<20} {7:<5} {7:<5} {255:<5} {42.50:<10}")
    print(f"{'Stoinis':<20} {7:<5} {5:<5} {169:<5} {42.25:<10}")
    print(f"{'Munsey':<20} {4:<5} {4:<5} {124:<5} {41.33:<10}")
    print(f"{'Babar Azam':<20} {4:<5} {4:<5} {122:<5} {40.67:<10}")
    print(f"{'Aaron Jones':<20} {6:<5} {6:<5} {162:<5} {40.50:<10}")
    print(f"{'Sherfane Rutherford':<20} {7:<5} {6:<5} {121:<5} {40.33:<10}")
    print(f"{'Pooran':<20} {7:<5} {7:<5} {228:<5} {38.00:<10}")

    # Best Batting Strike Rate
    print("\nBest Batting Strike Rate:")
    print(f"{'Batter':<20} {'M':<5} {'I':<5} {'R':<5} {'SR':<10}")
    print("="*45)
    print(f"{'Shai Hope':<20} {3:<5} {3:<5} {107:<5} {187.72:<10}")
    print(f"{'Brandon McMullen':<20} {4:<5} {3:<5} {140:<5} {170.73:<10}")
    print(f"{'Russell':<20} {7:<5} {6:<5} {78:<5} {165.96:<10}")
    print(f"{'Stoinis':<20} {7:<5} {5:<5} {169:<5} {164.08:<10}")
    print(f"{'Salt':<20} {8:<5} {7:<5} {188:<5} {159.32:<10}")
    print(f"{'Jos Buttler':<20} {8:<5} {7:<5} {214:<5} {158.52:<10}")
    print(f"{'Head':<20} {7:<5} {7:<5} {255:<5} {158.39:<10}")
    print(f"{'Harry Brook':<20} {8:<5} {4:<5} {145:<5} {157.61:<10}")
    print(f"{'Rohit':<20} {8:<5} {8:<5} {257:<5} {156.71:<10}")
    print(f"{'Hardik Pandya':<20} {8:<5} {6:<5} {144:<5} {151.58:<10}")
    print(f"{'Andries Gous':<20} {6:<5} {6:<5} {219:<5} {151.03:<10}")
    print(f"{'Delany':<20} {3:<5} {3:<5} {60:<5} {150.00:<10}")
    print(f"{'Tim David':<20} {7:<5} {5:<5} {61:<5} {148.78:<10}")
    print(f"{'Sherfane Rutherford':<20} {7:<5} {6:<5} {121:<5} {147.56:<10}")
    print(f"{'Livingstone':<20} {8:<5} {4:<5} {72:<5} {146.94:<10}")

    # Most Wickets
    print("\nMost Wickets:")
    print(f"{'Bowler':<20} {'M':<5} {'O':<5} {'W':<5} {'Avg':<10}")
    print("="*45)
    print(f"{'Fazalhaq Farooqi':<20} {8:<5} {25.2:<5} {17:<5} {9.41:<10}")
    print(f"{'Arshdeep Singh':<20} {8:<5} {30.0:<5} {17:<5} {12.65:<10}")
    print(f"{'Bumrah':<20} {8:<5} {29.4:<5} {15:<5} {8.27:<10}")
    print(f"{'Nortje':<20} {9:<5} {35.0:<5} {15:<5} {13.40:<10}")
    print(f"{'Rashid Khan':<20} {8:<5} {29.0:<5} {14:<5} {12.79:<10}")
    print(f"{'Rishad Hossain':<20} {7:<5} {25.0:<5} {14:<5} {13.86:<10}")
    print(f"{'Naveen-ul-Haq':<20} {8:<5} {26.4:<5} {13:<5} {12.31:<10}")
    print(f"{'Rabada':<20} {9:<5} {31.0:<5} {13:<5} {15.00:<10}")
    print(f"{'Zampa':<20} {7:<5} {28.0:<5} {13:<5} {14.38:<10}")
    print(f"{'Alzarri Joseph':<20} {7:<5} {24.3:<5} {13:<5} {13.62:<10}")
    print(f"{'Tanzim Hasan Sakib':<20} {7:<5} {24.0:<5} {11:<5} {13.55:<10}")
    print(f"{'Maharaj':<20} {8:<5} {28.0:<5} {11:<5} {15.91:<10}")
    print(f"{'Russell':<20} {7:<5} {20.1:<5} {11:<5} {12.82:<10}")
    print(f"{'Shamsi':<20} {5:<5} {16.5:<5} {11:<5} {11.64:<10}")
    print(f"{'Hardik Pandya':<20} {8:<5} {25.0:<5} {11:<5} {17.36:<10}")

    # Most Fifties
    print("\nMost Fifties:")
    print(f"{'Batter':<20} {'M':<5} {'I':<5} {'R':<5} {'50s':<5}")
    print("="*30)
    print(f"{'Gurbaz':<20} {8:<5} {8:<5} {281:<5} {3:<5}")
    print(f"{'Rohit':<20} {8:<5} {8:<5} {257:<5} {3:<5}")
    print(f"{'Head':<20} {7:<5} {7:<5} {255:<5} {2:<5}")
    print(f"{'de Kock':<20} {9:<5} {9:<5} {243:<5} {2:<5}")
    print(f"{'Ibrahim Zadran':<20} {8:<5} {8:<5} {231:<5} {2:<5}")
    print(f"{'Andries Gous':<20} {6:<5} {6:<5} {219:<5} {2:<5}")
    print(f"{'Suryakumar Yadav':<20} {8:<5} {8:<5} {199:<5} {2:<5}")
    print(f"{'Warner':<20} {7:<5} {7:<5} {178:<5} {2:<5}")
    print(f"{'Stoinis':<20} {7:<5} {5:<5} {169:<5} {2:<5}")
    print(f"{'Brandon McMullen':<20} {4:<5} {3:<5} {140:<5} {2:<5}")
    print(f"{'Pooran':<20} {7:<5} {7:<5} {228:<5} {1:<5}")
    print(f"{'Jos Buttler':<20} {8:<5} {7:<5} {214:<5} {1:<5}")
    print(f"{'Klaasen':<20} {9:<5} {8:<5} {190:<5} {1:<5}")
    print(f"{'Salt':<20} {8:<5} {7:<5} {188:<5} {1:<5}")
    print(f"{'David Miller':<20} {9:<5} {8:<5} {169:<5} {1:<5}")

# Call the function to display stats

def display_ipl_squads():
    # Royal Challengers Bangalore Squad
    print("\nRoyal Challengers Bangalore Squad:")
    print(f"{'Category':<20} {'Player ID':<20} {'Name':<20} {'Role':<20}")
    print("="*80)
    
    # BATTERS
    print(f"{'BATTERS':<20} {'suyash-prabhudessai':<20} {'Suyash Prabhudessai':<20} {'Batter':<20}")
    print(f"{'BATTERS':<20} {'rajat-patidar':<20} {'Rajat Patidar':<20} {'Batter':<20}")
    print(f"{'BATTERS':<20} {'virat-kohli':<20} {'Virat Kohli':<20} {'Batter':<20}")
    print(f"{'BATTERS':<20} {'faf-du-plessis':<20} {'Faf du Plessis (Captain)':<20} {'Batter':<20}")
    
    # ALL ROUNDERS
    print(f"{'ALL ROUNDERS':<20} {'glenn-maxwell':<20} {'Glenn Maxwell':<20} {'Batting Allrounder':<20}")
    print(f"{'ALL ROUNDERS':<20} {'mahipal-lomror':<20} {'Mahipal Lomror':<20} {'Batting Allrounder':<20}")
    print(f"{'ALL ROUNDERS':<20} {'cameron-green':<20} {'Cameron Green':<20} {'Batting Allrounder':<20}")
    print(f"{'ALL ROUNDERS':<20} {'manoj-bhandage':<20} {'Manoj Bhandage':<20} {'Batting Allrounder':<20}")
    print(f"{'ALL ROUNDERS':<20} {'saurav-chauhan':<20} {'Saurav Chauhan':<20} {'Batting Allrounder':<20}")
    print(f"{'ALL ROUNDERS':<20} {'swapnil-singh':<20} {'Swapnil Singh':<20} {'Bowling Allrounder':<20}")
    print(f"{'ALL ROUNDERS':<20} {'tom-curran':<20} {'Tom Curran':<20} {'Bowling Allrounder':<20}")
    
    # WICKET KEEPERS
    print(f"{'WICKET KEEPERS':<20} {'dinesh-karthik':<20} {'Dinesh Karthik':<20} {'WK-Batter':<20}")
    print(f"{'WICKET KEEPERS':<20} {'anuj-rawat':<20} {'Anuj Rawat':<20} {'WK-Batter':<20}")
    
    # BOWLERS
    print(f"{'BOWLERS':<20} {'karn-sharma':<20} {'Karn Sharma':<20} {'Bowler':<20}")
    print(f"{'BOWLERS':<20} {'vijaykumar-vyshak':<20} {'Vijaykumar Vyshak':<20} {'Bowler':<20}")
    print(f"{'BOWLERS':<20} {'alzarri-joseph':<20} {'Alzarri Joseph':<20} {'Bowler':<20}")
    print(f"{'BOWLERS':<20} {'yash-dayal':<20} {'Yash Dayal':<20} {'Bowler':<20}")
    print(f"{'BOWLERS':<20} {'rajan-kumar':<20} {'Rajan Kumar':<20} {'Bowler':<20}")
    print(f"{'BOWLERS':<20} {'mayank-dagar':<20} {'Mayank Dagar':<20} {'Bowler':<20}")
    print(f"{'BOWLERS':<20} {'lockie-ferguson':<20} {'Lockie Ferguson':<20} {'Bowler':<20}")
    print(f"{'BOWLERS':<20} {'mohammed-siraj':<20} {'Mohammed Siraj':<20} {'Bowler':<20}")
    print(f"{'BOWLERS':<20} {'himanshu-sharma':<20} {'Himanshu Sharma':<20} {'Bowler':<20}")
    print(f"{'BOWLERS':<20} {'akash-deep':<20} {'Akash Deep':<20} {'Bowler':<20}")

    # Chennai Super Kings Squad
    print("\nChennai Super Kings Squad:")
    print(f"{'Category':<20} {'Player ID':<20} {'Name':<20} {'Role':<20}")
    print("="*80)
    
    # BATTERS
    print(f"{'BATTERS':<20} {'ruturaj-gaikwad':<20} {'Ruturaj Gaikwad (Captain)':<20} {'Batter':<20}")
    print(f"{'BATTERS':<20} {'ajinkya-rahane':<20} {'Ajinkya Rahane':<20} {'Batter':<20}")
    print(f"{'BATTERS':<20} {'shaik-rasheed':<20} {'Shaik Rasheed':<20} {'Batter':<20}")
    print(f"{'BATTERS':<20} {'sameer-rizvi':<20} {'Sameer Rizvi':<20} {'Batter':<20}")
    
    # ALL ROUNDERS
    print(f"{'ALL ROUNDERS':<20} {'shivam-dube':<20} {'Shivam Dube':<20} {'Batting Allrounder':<20}")
    print(f"{'ALL ROUNDERS':<20} {'ravindra-jadeja':<20} {'Ravindra Jadeja':<20} {'Bowling Allrounder':<20}")
    print(f"{'ALL ROUNDERS':<20} {'mohammed-nabi':<20} {'Mohammed Nabi':<20} {'Bowling Allrounder':<20}")
    print(f"{'ALL ROUNDERS':<20} {'michael-bracewell':<20} {'Michael Bracewell':<20} {'Bowling Allrounder':<20}")
    print(f"{'ALL ROUNDERS':<20} {'simarjeet-singh':<20} {'Simarjeet Singh':<20} {'Bowling Allrounder':<20}")
    
    # WICKET KEEPERS
    print(f"{'WICKET KEEPERS':<20} {'ms-dhoni':<20} {'MS Dhoni':<20} {'WK-Batter':<20}")
    print(f"{'WICKET KEEPERS':<20} {'devon-conway':<20} {'Devon Conway':<20} {'WK-Batter':<20}")
    
    # BOWLERS
    print(f"{'BOWLERS':<20} {'deepak-chahar':<20} {'Deepak Chahar':<20} {'Bowler':<20}")
    print(f"{'BOWLERS':<20} {'maheesh-theekshana':<20} {'Maheesh Theekshana':<20} {'Bowler':<20}")
    print(f"{'BOWLERS':<20} {'matheesha-pathirana':<20} {'Matheesha Pathirana':<20} {'Bowler':<20}")
    print(f"{'BOWLERS':<20} {'mohammed-shami':<20} {'Mohammed Shami':<20} {'Bowler':<20}")
    print(f"{'BOWLERS':<20} {'tushar-deshpande':<20} {'Tushar Deshpande':<20} {'Bowler':<20}")
    print(f"{'BOWLERS':<20} {'mukesh-choudhary':<20} {'Mukesh Choudhary':<20} {'Bowler':<20}")
    print(f"{'BOWLERS':<20} {'prashant-solanki':<20} {'Prashant Solanki':<20} {'Bowler':<20}")

def display_matches_3():
    
    matches = [
        ("1st Match", "Chennai, MA Chidambaram Stadium", "RCB vs CSK", "RCB: 173-6 (20) | CSK: 176-4 (18.4)", "CSK won by 6 wkts"),
        ("2nd Match", "Chandigarh, Maharaja Yadavindra Singh International Cricket Stadium, Mullanpur", "DC vs PBKS", "DC: 174-9 (20) | PBKS: 177-6 (19.2)", "PBKS won by 4 wkts"),
        ("3rd Match", "Kolkata, Eden Gardens", "KKR vs SRH", "KKR: 208-7 (20) | SRH: 204-7 (20)", "KKR won by 4 runs"),
        ("4th Match", "Jaipur, Sawai Mansingh Stadium", "RR vs LSG", "RR: 193-4 (20) | LSG: 173-6 (20)", "RR won by 20 runs"),
        ("5th Match", "Ahmedabad, Narendra Modi Stadium", "GT vs MI", "GT: 168-6 (20) | MI: 162-9 (20)", "GT won by 6 runs"),
        ("6th Match", "Bengaluru, M.Chinnaswamy Stadium", "PBKS vs RCB", "PBKS: 176-6 (20) | RCB: 178-6 (19.2)", "RCB won by 4 wkts"),
        ("7th Match", "Chennai, MA Chidambaram Stadium", "CSK vs GT", "CSK: 206-6 (20) | GT: 143-8 (20)", "CSK won by 63 runs"),
        ("8th Match", "Hyderabad, Rajiv Gandhi International Stadium", "SRH vs MI", "SRH: 277-3 (20) | MI: 246-5 (20)", "SRH won by 31 runs"),
        ("9th Match", "Jaipur, Sawai Mansingh Stadium", "RR vs DC", "RR: 185-5 (20) | DC: 173-5 (20)", "RR won by 12 runs"),
        ("10th Match", "Bengaluru, M.Chinnaswamy Stadium", "RCB vs KKR", "RCB: 182-6 (20) | KKR: 186-3 (16.5)", "KKR won by 7 wkts"),
        ("11th Match", "Lucknow, Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium", "LSG vs PBKS", "LSG: 199-8 (20) | PBKS: 178-5 (20)", "LSG won by 21 runs"),
        ("12th Match", "Ahmedabad, Narendra Modi Stadium", "SRH vs GT", "SRH: 162-8 (20) | GT: 168-3 (19.1)", "GT won by 7 wkts"),
        ("13th Match", "Visakhapatnam, Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium", "DC vs CSK", "DC: 191-5 (20) | CSK: 171-6 (20)", "DC won by 20 runs"),
        ("14th Match", "Mumbai, Wankhede Stadium", "MI vs RR", "MI: 125-9 (20) | RR: 127-4 (15.3)", "RR won by 6 wkts"),
        ("15th Match", "Bengaluru, M.Chinnaswamy Stadium", "LSG vs RCB", "LSG: 181-5 (20) | RCB: 153 (19.4)", "LSG won by 28 runs"),
        ("16th Match", "Visakhapatnam, Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium", "KKR vs DC", "KKR: 272-7 (20) | DC: 166 (17.2)", "KKR won by 106 runs"),
        ("17th Match", "Ahmedabad, Narendra Modi Stadium", "GT vs PBKS", "GT: 199-4 (20) | PBKS: 200-7 (19.5)", "PBKS won by 3 wkts"),
        ("18th Match", "Hyderabad, Rajiv Gandhi International Stadium", "CSK vs SRH", "CSK: 165-5 (20) | SRH: 166-4 (18.1)", "SRH won by 6 wkts"),
        ("19th Match", "Jaipur, Sawai Mansingh Stadium", "RCB vs RR", "RCB: 183-3 (20) | RR: 189-4 (19.1)", "RR won by 6 wkts"),
        ("20th Match", "Mumbai, Wankhede Stadium", "MI vs DC", "MI: 234-5 (20) | DC: 205-8 (20)", "MI won by 29 runs"),
        ("21st Match", "Lucknow, Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium", "LSG vs GT", "LSG: 163-5 (20) | GT: 130 (18.5)", "LSG won by 33 runs"),
        ("22nd Match", "Chennai, MA Chidambaram Stadium", "KKR vs CSK", "KKR: 137-9 (20) | CSK: 141-3 (17.4)", "CSK won by 7 wkts"),
        ("23rd Match", "Chandigarh, Maharaja Yadavindra Singh International Cricket Stadium, Mullanpur", "SRH vs PBKS", "SRH: 182-9 (20) | PBKS: 180-6 (20)", "SRH won by 2 runs"),
        ("24th Match", "Jaipur, Sawai Mansingh Stadium", "RR vs GT", "RR: 196-3 (20) | GT: 199-7 (20)", "GT won by 3 wkts"),
        ("25th Match", "Mumbai, Wankhede Stadium", "RCB vs MI", "RCB: 196-8 (20) | MI: 199-3 (15.3)", "MI won by 7 wkts"),
        ("26th Match", "Lucknow, Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium", "LSG vs DC", "LSG: 167-7 (20) | DC: 170-4 (18.1)", "DC won by 6 wkts"),
        ("27th Match", "Chandigarh, Maharaja Yadavindra Singh International Cricket Stadium, Mullanpur", "PBKS vs RR", "PBKS: 147-8 (20) | RR: 152-7 (19.5)", "RR won by 3 wkts"),
        ("28th Match", "Kolkata, Eden Gardens", "LSG vs KKR", "LSG: 161-7 (20) | KKR: 162-2 (15.4)", "KKR won by 8 wkts"),
        ("29th Match", "Mumbai, Wankhede Stadium", "CSK vs MI", "CSK: 206-4 (20) | MI: 186-6 (20)", "CSK won by 20 runs"),
        ("30th Match", "Bengaluru, M.Chinnaswamy Stadium", "SRH vs RCB", "SRH: 287-3 (20) | RCB: 262-7 (20)", "SRH won by 25 runs"),
        ("31st Match", "Kolkata, Eden Gardens", "KKR vs RR", "KKR: 223-6 (20) | RR: 224-8 (20)", "RR won by 2 wkts"),
        ("32nd Match", "Ahmedabad, Narendra Modi Stadium", "GT vs DC", "GT: 89 (17.3) | DC: 92-4 (8.5)", "DC won by 6 wkts"),
        ("33rd Match", "Chandigarh, Maharaja Yadavindra Singh International Cricket Stadium, Mullanpur", "MI vs PBKS", "MI: 192-7 (20) | PBKS: 183 (19.1)", "MI won by 9 runs"),
        ("34th Match", "Lucknow, Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium", "CSK vs LSG", "CSK: 176-6 (20) | LSG: 180-2 (19)", "LSG won by 8 wkts"),
        ("35th Match", "Delhi, Arun Jaitley Stadium", "SRH vs DC", "SRH: 266-7 (20) | DC: 199 (19.1)", "SRH won by 67 runs"),
        ("36th Match", "Kolkata, Eden Gardens", "KKR vs RCB", "KKR: 207-5 (20) | RCB: 200-7 (20)", "KKR won by 7 runs"),
        ("37th Match", "Chennai, MA Chidambaram Stadium", "CSK vs RR", "CSK: 184-8 (20) | RR: 186-7 (19.3)", "RR won by 3 wkts"),
        ("38th Match", "Mumbai, Wankhede Stadium", "MI vs SRH", "MI: 203-8 (20) | SRH: 206-4 (18.4)", "SRH won by 6 wkts"),
        ("39th Match", "Delhi, Arun Jaitley Stadium", "DC vs KKR", "DC: 182-7 (20) | KKR: 183-3 (17.5)", "KKR won by 7 wkts"),
        ("40th Match", "Hyderabad, Rajiv Gandhi International Stadium", "GT vs RR", "GT: 173-9 (20) | RR: 175-4 (19.4)", "RR won by 6 wkts"),
        ("41st Match", "Chennai, MA Chidambaram Stadium", "CSK vs RCB", "CSK: 177-6 (20) | RCB: 181-7 (19.5)", "RCB won by 3 wkts"),
        ("42nd Match", "Ahmedabad, Narendra Modi Stadium", "GT vs MI", "GT: 191-3 (20) | MI: 198-5 (20)", "MI won by 7 runs"),
        ("Final Match", "Mumbai, Wankhede Stadium", "MI vs RCB", "MI: 246-8 (20) | RCB: 251-5 (19.5)", "RCB won by 5 wkts")
    ]

    print("\nUpcoming Cricket Matches:")
    for match in matches:
        print(f"\nMatch: {match[0]}")
        print(f"Venue: {match[1]}")
        print(f"Teams: {match[2]}")
        print(f"Scores: {match[3]}")
        print(f"Result: {match[4]}")

def display_table_3():
    print("\nTable: IPL 2024")

    print(f"{'Team':<15} {'P':<3} {'W':<3} {'L':<3} {'NR':<3} {'Pts':<3} {'NRR':<5}")
    print("="*30)
    print(f"{'KKR (Q)':<15} {14:<3} {9:<3} {3:<3} {2:<3} {20:<3} {+1.428:<5}")
    print(f"{'SRH (Q)':<15} {14:<3} {8:<3} {5:<3} {1:<3} {17:<3} {+0.414:<5}")
    print(f"{'RR (Q)':<15} {14:<3} {8:<3} {5:<3} {1:<3} {17:<3} {+0.273:<5}")
    print(f"{'RCB (Q)':<15} {14:<3} {7:<3} {7:<3} {0:<3} {14:<3} {+0.459:<5}")
    print(f"{'CSK (E)':<15} {14:<3} {7:<3} {7:<3} {0:<3} {14:<3} {+0.392:<5}")
    print(f"{'DC (E)':<15} {14:<3} {7:<3} {7:<3} {0:<3} {14:<3} {-0.377:<5}")
    print(f"{'LSG (E)':<15} {14:<3} {7:<3} {7:<3} {0:<3} {14:<3} {-0.667:<5}")
    print(f"{'GT (E)':<15} {14:<3} {5:<3} {7:<3} {2:<3} {12:<3} {-1.063:<5}")
    print(f"{'PBKS (E)':<15} {14:<3} {5:<3} {9:<3} {0:<3} {10:<3} {-0.353:<5}")
    print(f"{'MI (E)':<15} {14:<3} {4:<3} {10:<3} {0:<3} {8:<3} {-0.318:<5}")


def display_IPL_stats():
    print("\nMost Runs")
    print(f"{'Batter':<20} {'M':<5} {'I':<5} {'R':<5} {'Avg':<10}")
    print("="*50)
    print(f"{'Kohli':<20} {15:<5} {15:<5} {741:<5} {61.75:<10}")
    print(f"{'Ruturaj Gaikwad':<20} {14:<5} {14:<5} {583:<5} {53.00:<10}")
    print(f"{'Riyan Parag':<20} {15:<5} {14:<5} {573:<5} {52.09:<10}")
    print(f"{'Head':<20} {15:<5} {15:<5} {567:<5} {40.50:<10}")
    print(f"{'Samson':<20} {15:<5} {15:<5} {531:<5} {48.27:<10}")
    print(f"{'Sai Sudharsan':<20} {12:<5} {12:<5} {527:<5} {47.91:<10}")
    print(f"{'Rahul':<20} {14:<5} {14:<5} {520:<5} {37.14:<10}")
    print(f"{'Pooran':<20} {14:<5} {14:<5} {499:<5} {62.38:<10}")
    print(f"{'Narine':<20} {14:<5} {14:<5} {488:<5} {34.86:<10}")
    print(f"{'Abhishek Sharma':<20} {16:<5} {16:<5} {484:<5} {32.27:<10}")
    print(f"{'Klaasen':<20} {16:<5} {15:<5} {479:<5} {39.92:<10}")
    print(f"{'Pant':<20} {13:<5} {13:<5} {446:<5} {40.55:<10}")
    print(f"{'du Plessis':<20} {15:<5} {15:<5} {438:<5} {29.20:<10}")
    print(f"{'Salt':<20} {12:<5} {12:<5} {435:<5} {39.55:<10}")
    print(f"{'Yashasvi Jaiswal':<20} {15:<5} {15:<5} {435:<5} {31.07:<10}")

    print("\nBest Batting Average")
    print(f"{'Batter':<20} {'M':<5} {'I':<5} {'R':<5} {'Avg':<10}")
    print("="*50)
    print(f"{'Pooran':<20} {14:<5} {14:<5} {499:<5} {62.38:<10}")
    print(f"{'Kohli':<20} {15:<5} {15:<5} {741:<5} {61.75:<10}")
    print(f"{'Tristan Stubbs':<20} {14:<5} {13:<5} {378:<5} {54.00:<10}")
    print(f"{'Dhoni':<20} {14:<5} {11:<5} {161:<5} {53.67:<10}")
    print(f"{'Ruturaj Gaikwad':<20} {14:<5} {14:<5} {583:<5} {53.00:<10}")
    print(f"{'Riyan Parag':<20} {15:<5} {14:<5} {573:<5} {52.09:<10}")
    print(f"{'Samson':<20} {15:<5} {15:<5} {531:<5} {48.27:<10}")
    print(f"{'Sai Sudharsan':<20} {12:<5} {12:<5} {527:<5} {47.91:<10}")
    print(f"{'Venkatesh Iyer':<20} {14:<5} {13:<5} {370:<5} {46.25:<10}")
    print(f"{'Ravindra Jadeja':<20} {14:<5} {11:<5} {267:<5} {44.50:<10}")
    print(f"{'Shashank Singh':<20} {14:<5} {14:<5} {354:<5} {44.25:<10}")
    print(f"{'Tilak Varma':<20} {13:<5} {13:<5} {416:<5} {41.60:<10}")
    print(f"{'Arshad Khan':<20} {4:<5} {4:<5} {83:<5} {41.50:<10}")
    print(f"{'Pant':<20} {13:<5} {13:<5} {446:<5} {40.55:<10}")
    print(f"{'Head':<20} {15:<5} {15:<5} {567:<5} {40.50:<10}")

    print("\nBest Batting Strike Rate")
    print(f"{'Batter':<20} {'M':<5} {'I':<5} {'R':<5} {'SR':<10}")
    print("="*50)
    print(f"{'Romario Shepherd':<20} {6:<5} {5:<5} {57:<5} {271.43:<10}")
    print(f"{'Jake Fraser-McGurk':<20} {9:<5} {9:<5} {330:<5} {234.04:<10}")
    print(f"{'Dhoni':<20} {14:<5} {11:<5} {161:<5} {220.55:<10}")
    print(f"{'Abhishek Sharma':<20} {16:<5} {16:<5} {484:<5} {204.22:<10}")
    print(f"{'Ramandeep Singh':<20} {14:<5} {9:<5} {125:<5} {201.61:<10}")
    print(f"{'Head':<20} {15:<5} {15:<5} {567:<5} {191.55:<10}")
    print(f"{'Tristan Stubbs':<20} {14:<5} {13:<5} {378:<5} {190.91:<10}")
    print(f"{'Karthik':<20} {15:<5} {13:<5} {326:<5} {187.36:<10}")
    print(f"{'Russell':<20} {14:<5} {9:<5} {222:<5} {185.00:<10}")
    print(f"{'Lomror':<20} {10:<5} {10:<5} {125:<5} {183.82:<10}")
    print(f"{'Salt':<20} {12:<5} {12:<5} {435:<5} {182.01:<10}")
    print(f"{'Rossouw':<20} {8:<5} {8:<5} {211:<5} {181.90:<10}")
    print(f"{'Narine':<20} {14:<5} {14:<5} {488:<5} {180.74:<10}")
    print(f"{'Pooran':<20} {14:<5} {14:<5} {499:<5} {178.21:<10}")
    print(f"{'Naman Dhir':<20} {7:<5} {7:<5} {140:<5} {177.22:<10}")

    print("\nMost Sixes")
    print(f"{'Batter':<20} {'M':<5} {'I':<5} {'R':<5} {'6s':<5}")
    print("="*50)
    print(f"{'Abhishek Sharma':<20} {16:<5} {16:<5} {484:<5} {42:<5}")
    print(f"{'Kohli':<20} {15:<5} {15:<5} {741:<5} {38:<5}")
    print(f"{'Klaasen':<20} {16:<5} {15:<5} {479:<5} {38:<5}")
    print(f"{'Pooran':<20} {14:<5} {14:<5} {499:<5} {36:<5}")
    print(f"{'Riyan Parag':<20} {15:<5} {14:<5} {573:<5} {33:<5}")
    print(f"{'Narine':<20} {14:<5} {14:<5} {488:<5} {33:<5}")
    print(f"{'Rajat Patidar':<20} {15:<5} {13:<5} {395:<5} {33:<5}")
    print(f"{'Head':<20} {15:<5} {15:<5} {567:<5} {32:<5}")
    print(f"{'Shivam Dube':<20} {14:<5} {14:<5} {396:<5} {28:<5}")
    print(f"{'Jake Fraser-McGurk':<20} {9:<5} {9:<5} {330:<5} {28:<5}")
    print(f"{'Tristan Stubbs':<20} {14:<5} {13:<5} {378:<5} {26:<5}")
    print(f"{'Pant':<20} {13:<5} {13:<5} {446:<5} {25:<5}")
    print(f"{'Samson':<20} {15:<5} {15:<5} {531:<5} {24:<5}")
    print(f"{'Salt':<20} {12:<5} {12:<5} {435:<5} {24:<5}")
    print(f"{'Rohit':<20} {14:<5} {14:<5} {417:<5} {23:<5}")

    print("\nMost Fours")
    print(f"{'Batter':<20} {'M':<5} {'I':<5} {'R':<5} {'4s':<5}")
    print("="*50)
    print(f"{'Head':<20} {15:<5} {15:<5} {567:<5} {64:<5}")
    print(f"{'Kohli':<20} {15:<5} {15:<5} {741:<5} {62:<5}")
    print(f"{'Ruturaj Gaikwad':<20} {14:<5} {14:<5} {583:<5} {58:<5}")
    print(f"{'Yashasvi Jaiswal':<20} {15:<5} {15:<5} {435:<5} {54:<5}")
    print(f"{'Narine':<20} {14:<5} {14:<5} {488:<5} {50:<5}")
    print(f"{'Salt':<20} {12:<5} {12:<5} {435:<5} {50:<5}")
    print(f"{'Samson':<20} {15:<5} {15:<5} {531:<5} {48:<5}")
    print(f"{'Sai Sudharsan':<20} {12:<5} {12:<5} {527:<5} {48:<5}")
    print(f"{'du Plessis':<20} {15:<5} {15:<5} {438:<5} {47:<5}")
    print(f"{'Rahul':<20} {14:<5} {14:<5} {520:<5} {45:<5}")
    print(f"{'Rohit':<20} {14:<5} {14:<5} {417:<5} {45:<5}")
    print(f"{'Riyan Parag':<20} {15:<5} {14:<5} {573:<5} {40:<5}")
    print(f"{'Stoinis':<20} {14:<5} {14:<5} {388:<5} {39:<5}")
    print(f"{'Shubman Gill':<20} {12:<5} {12:<5} {426:<5} {37:<5}")
    print(f"{'Abhishek Sharma':<20} {16:<5} {16:<5} {484:<5} {36:<5}")

# Main program
def main():
    display_welcome_message()
    cricket_teams = {
        "India": {
            "schedule": [
                ("Sep 19, Thu - Sep 23, Mon", "India vs Bangladesh, 1st Test", "MA Chidambaram Stadium, Chennai", "04:00 AM GMT / 09:30 AM LOCAL"),
                ("Sep 27, Fri - Oct 01, Tue", "India vs Bangladesh, 2nd Test", "Green Park, Kanpur", "04:00 AM GMT / 09:30 AM LOCAL"),
                ("Oct 06, Sun", "India vs Bangladesh, 1st T20I", "New Madhavrao Scindia Cricket Stadium, Gwalior", "01:30 PM GMT / 07:00 PM LOCAL"),
                ("Oct 09, Wed", "India vs Bangladesh, 2nd T20I", "Arun Jaitley Stadium, Delhi", "01:30 PM GMT / 07:00 PM LOCAL"),
                ("Oct 12, Sat", "India vs Bangladesh, 3rd T20I", "Rajiv Gandhi International Stadium, Hyderabad", "01:30 PM GMT / 07:00 PM LOCAL"),
                ("Oct 16, Wed - Oct 20, Sun", "India vs New Zealand, 1st Test", "M.Chinnaswamy Stadium, Bengaluru", "04:00 AM GMT / 09:30 AM LOCAL")
            ],
            "results": [
                ("Aug 07, Wed", "Sri Lanka vs India, 3rd ODI", "Sri Lanka won by 110 runs"),
                ("Aug 04, Sun", "Sri Lanka vs India, 2nd ODI", "Sri Lanka won by 32 runs"),
                ("Aug 02, Fri", "Sri Lanka vs India, 1st ODI", "Match tied"),
                ("Jul 30, Tue", "India vs Sri Lanka, 3rd T20I", "Match tied (India won the super over)"),
                ("Jul 28, Sun", "Sri Lanka vs India, 2nd T20I", "India won by 7 wkts (2nd innings reduced to 8 ovs due to rain, DLS target 78)"),
                ("Jul 27, Sat", "India vs Sri Lanka, 1st T20I", "India won by 43 runs"),
                ("Jul 14, Sun", "India vs Zimbabwe, 5th T20I", "India won by 42 runs"),
                ("Jul 13, Sat", "Zimbabwe vs India, 4th T20I", "India won by 10 wkts"),
                ("Jul 10, Wed", "India vs Zimbabwe, 3rd T20I", "India won by 23 runs"),
                ("Jul 07, Sun", "India vs Zimbabwe, 2nd T20I", "India won by 100 runs")
            ],
            "players": {
                "batsmen": [
                    "Virat Kohli", "Rohit Sharma", "Shikhar Dhawan", "Shubman Gill",
                    "Shreyas Iyer", "Manish Pandey", "Mayank Agarwal", "Prithvi Shaw",
                    "Cheteshwar Pujara", "Ajinkya Rahane", "Ruturaj Gaikwad"
                ],
                "all_rounders": [
                    "Hardik Pandya", "Hanuma Vihari", "Ravindra Jadeja", "Ravichandran Ashwin"
                ],
                "wicket_keepers": [
                    "KL Rahul", "Sanju Samson", "Wriddhiman Saha", "Rishabh Pant"
                ],
                "bowlers": [
                    "Mohammed Shami", "Jasprit Bumrah", "Kuldeep Yadav", "Yuzvendra Chahal",
                    "Navdeep Saini", "Shardul Thakur", "Umesh Yadav", "Mohammed Siraj"
                ]
            },
            "most_runs": [
        ("Sachin Tendulkar", 200, 329, 15921, 54.0, 54.0, 2058, 69),
        ("Rahul Dravid", 163, 284, 13265, 53.0, 43.0, 1652, 21),
        ("Sunil Gavaskar", 125, 214, 10122, 51.0, 66.0, 1016, 26),
        ("Virat Kohli", 113, 191, 8848, 49.0, 56.0, 991, 26),
        ("VVS Laxman", 134, 225, 8781, 46.0, 49.0, 1135, 5),
        ("Virender Sehwag", 103, 178, 8503, 49.0, 82.0, 1219, 90),
        ("Sourav Ganguly", 113, 188, 7212, 42.0, 51.0, 900, 57),
        ("Cheteshwar Pujara", 103, 176, 7195, 44.0, 44.0, 863, 16),
        ("Dilip Vengsarkar", 116, 185, 6868, 42.0, 60.0, 560, 17),
        ("Mohammad Azharuddin", 99, 147, 6215, 45.0, 63.0, 720, 19),
        ("Gundappa Viswanath", 91, 155, 6080, 42.0, 76.0, 616, 6),
        ("Kapil Dev", 131, 184, 5248, 31.0, 95.0, 587, 61),
        ("Ajinkya Rahane", 85, 144, 5077, 38.0, 50.0, 579, 35),
        ("MS Dhoni", 90, 144, 4876, 38.0, 59.0, 544, 78),
        ("Mohinder Amarnath", 69, 113, 4378, 43.0, 86.0, 330, 21),
        ("Gautam Gambhir", 58, 104, 4154, 42.0, 51.0, 517, 10),
        ("Rohit Sharma", 59, 101, 4138, 45.0, 57.0, 452, 84)
    ],
    "most_wickets": [
        ("Anil Kumble", 132, 6808, 40850, 619, 30.0, 18355, 31, 35),
        ("Ravichandran Ashwin", 100, 4361, 26166, 516, 24.0, 12255, 25, 36),
        ("Kapil Dev", 131, 4623, 27740, 434, 30.0, 12867, 17, 23),
        ("Harbhajan Singh", 103, 4763, 28580, 417, 32.0, 13537, 16, 25),
        ("Ishant Sharma", 105, 3193, 19160, 311, 32.0, 10078, 10, 11),
        ("Zaheer Khan", 92, 3131, 18785, 311, 33.0, 10247, 15, 11),
        ("Ravindra Jadeja", 72, 2872, 17233, 294, 24.0, 7096, 13, 13),
        ("Bishan Bedi", 67, 3441, 20650, 266, 29.0, 7637, 13, 14),
        ("Bhagwath Chandrasekhar", 58, 2550, 15299, 242, 30.0, 7199, 12, 16),
        ("Javagal Srinath", 67, 2517, 15104, 236, 30.0, 7196, 8, 10),
        ("Mohammed Shami", 64, 1919, 11515, 229, 28.0, 6346, 12, 6),
        ("Erapalli Prasanna", 49, 2262, 13575, 189, 30.0, 5742, 17, 10),
        ("Umesh Yadav", 57, 1496, 8979, 170, 31.0, 5263, 6, 3),
        ("Vinoo Mankad", 44, 2389, 14338, 162, 32.0, 5236, 10, 8),
        ("Jasprit Bumrah", 36, 1197, 7182, 159, 21.0, 3291, 4, 10)
    ]

        },
        "Australia": {
            "schedule": [
                ("Sep 15, Sun - Sep 19, Thu", "Australia vs New Zealand, 1st Test", "Gabba, Brisbane", "08:00 AM GMT / 06:00 PM LOCAL"),
                ("Sep 23, Mon - Sep 27, Fri", "Australia vs New Zealand, 2nd Test", "Adelaide Oval, Adelaide", "08:00 AM GMT / 06:00 PM LOCAL"),
                ("Oct 05, Sat", "Australia vs England, 1st T20I", "Sydney Cricket Ground, Sydney", "09:00 AM GMT / 07:00 PM LOCAL"),
                ("Oct 08, Tue", "Australia vs England, 2nd T20I", "Melbourne Cricket Ground, Melbourne", "09:00 AM GMT / 07:00 PM LOCAL"),
                ("Oct 11, Fri", "Australia vs England, 3rd T20I", "Perth Stadium, Perth", "09:00 AM GMT / 07:00 PM LOCAL")
            ],
            "results": [
                ("Aug 10, Sat", "Australia vs South Africa, 1st ODI", "South Africa won by 8 wickets"),
                ("Aug 07, Wed", "Australia vs South Africa, 2nd ODI", "Australia won by 4 wickets"),
                ("Jul 30, Tue", "Australia vs South Africa, 3rd ODI", "Australia won by 6 wickets"),
                ("Jul 25, Thu", "Australia vs South Africa, 4th ODI", "Match tied")
            ],
            "players": {
                "batsmen": [
                    "Steve Smith", "David Warner", "Marnus Labuschagne", "Usman Khawaja",
                    "Travis Head", "Will Pucovski", "Aaron Finch", "Matthew Renshaw"
                ],
                "all_rounders": [
                    "Mitchell Marsh", "Glenn Maxwell", "Marcus Stoinis", "James Faulkner"
                ],
                "wicket_keepers": [
                    "Alex Carey", "Josh Inglis"
                ],
                "bowlers": [
                    "Pat Cummins", "Mitchell Starc", "Josh Hazlewood", "Nathan Lyon",
                    "Adam Zampa", "Kane Richardson", "James Pattinson"
                ]
            },
            
    "most_runs": [
        ("Ricky Ponting", 168, 287, 13378, 52.0, 59.0, 1509, 73),
        ("Allan Border", 156, 265, 11174, 51.0, 41.0, 1161, 28),
        ("Steve Waugh", 168, 260, 10927, 51.0, 49.0, 1175, 20),
        ("Steven Smith", 109, 195, 9685, 57.0, 54.0, 1063, 54),
        ("David Warner", 112, 205, 8786, 45.0, 70.0, 1036, 69),
        ("Michael Clarke", 115, 198, 8643, 49.0, 56.0, 977, 39),
        ("Matthew Hayden", 103, 184, 8625, 51.0, 60.0, 1049, 82),
        ("Mark Waugh", 128, 209, 8029, 42.0, 52.0, 844, 41),
        ("Justin Langer", 105, 182, 7696, 45.0, 54.0, 912, 40),
        ("Mark Taylor", 104, 186, 7525, 44.0, 41.0, 727, 9),
        ("David Boon", 107, 190, 7422, 44.0, 41.0, 822, 2),
        ("Greg Chappell", 87, 151, 7110, 54.0, 54.0, 755, 16),
        ("Sir Donald Bradman", 52, 80, 6996, 100.0, 71.0, 681, 6),
        ("Michael Hussey", 79, 137, 6235, 52.0, 50.0, 685, 39),
        ("Adam Gilchrist", 96, 137, 5570, 48.0, 82.0, 677, 100)
    ],
    "most_wickets": [
        ("Shane Warne", 145, 6784, 40705, 708, 25.0, 17995, 48, 37),
        ("Glenn McGrath", 124, 4874, 29248, 563, 22.0, 12186, 28, 29),
        ("Nathan Lyon", 129, 5460, 32761, 530, 30.0, 16052, 24, 24),
        ("Mitchell Starc", 89, 2903, 17417, 358, 28.0, 9932, 20, 14),
        ("Dennis Lillee", 70, 2836, 17017, 355, 24.0, 8493, 23, 23),
        ("Mitchell Johnson", 73, 2667, 16001, 313, 28.0, 8891, 16, 12),
        ("Brett Lee", 76, 2755, 16531, 310, 31.0, 9554, 17, 10),
        ("Craig McDermott", 71, 2764, 16586, 291, 29.0, 8332, 17, 14),
        ("Josh Hazlewood", 70, 2429, 14577, 273, 25.0, 6778, 10, 12),
        ("Pat Cummins", 62, 2102, 12614, 269, 23.0, 6063, 16, 12),
        ("Jason Gillespie", 71, 2372, 14234, 259, 26.0, 6770, 8, 8),
        ("Richie Benaud", 63, 2729, 16374, 248, 27.0, 6704, 16, 16),
        ("Garth McKenzie", 60, 2631, 15785, 246, 30.0, 7328, 7, 16),
        ("Ray Lindwall", 61, 1971, 11828, 228, 23.0, 5251, 8, 12),
        ("Peter Siddle", 67, 2318, 13907, 221, 31.0, 6777, 8, 8),
        ("Clarrie Grimmett", 37, 2409, 14453, 216, 24.0, 5231, 7, 21),
        ("Merv Hughes", 53, 2047, 12285, 212, 28.0, 6017, 14, 7),
        ("Stuart MacGill", 44, 1873, 11237, 208, 29.0, 6038, 9, 12)
    ]


        },
        "England": {
            "schedule": [
                ("Sep 19, Thu - Sep 23, Mon", "England vs India, 1st Test", "Lord's, London", "10:00 AM GMT"),
                ("Sep 27, Fri - Oct 01, Tue", "England vs India, 2nd Test", "Old Trafford, Manchester", "10:00 AM GMT"),
                ("Oct 05, Sat", "England vs South Africa, 1st T20I", "The Rose Bowl, Southampton", "05:00 PM GMT"),
                ("Oct 08, Tue", "England vs South Africa, 2nd T20I", "Edgbaston, Birmingham", "05:00 PM GMT"),
                ("Oct 11, Fri", "England vs South Africa, 3rd T20I", "Trent Bridge, Nottingham", "05:00 PM GMT")
            ],
            "results": [
                ("Aug 12, Mon", "England vs Australia, 1st ODI", "England won by 2 runs"),
                ("Aug 15, Thu", "England vs Australia, 2nd ODI", "Australia won by 8 wickets"),
                ("Aug 18, Sun", "England vs Australia, 3rd ODI", "England won by 5 wickets"),
                ("Jul 20, Sat", "England vs Pakistan, 5th ODI", "England won by 11 runs"),
                ("Jul 17, Wed", "England vs Pakistan, 4th ODI", "Pakistan won by 2 wickets"),
                ("Jul 14, Sun", "England vs Pakistan, 3rd ODI", "England won by 5 runs")
            ],
            "players": {
                "batsmen": [
                    "Joe Root", "Ben Stokes", "Jos Buttler", "Jonny Bairstow",
                    "Ollie Pope", "Dom Sibley", "Rory Burns", "Haseeb Hameed"
                ],
                "all_rounders": [
                    "Ben Stokes", "Chris Woakes", "Sam Curran", "Moeen Ali"
                ],
                "wicket_keepers": [
                    "Jos Buttler", "Jonny Bairstow", "Ben Foakes"
                ],
                "bowlers": [
                    "James Anderson", "Stuart Broad", "Jofra Archer", "Mark Wood",
                    "Chris Woakes", "Sam Curran", "Olly Stone"
                ]
            },
            "most_runs": [
        ("Sir Alastair Cook", 161, 291, 12472, 45.0, 47.0, 1441, 11),
        ("Joe Root", 144, 263, 12131, 50.0, 57.0, 1312, 44),
        ("Graham Gooch", 118, 215, 8900, 43.0, 49.0, 1079, 25),
        ("Alec Stewart", 133, 235, 8463, 40.0, 49.0, 1121, 10),
        ("David Gower", 117, 204, 8231, 44.0, 51.0, 979, 10),
        ("Kevin Pietersen", 104, 181, 8181, 47.0, 62.0, 985, 81),
        ("Sir Geoff Boycott", 108, 193, 8114, 48.0, 40.0, 771, 8),
        ("Mike Atherton", 115, 212, 7728, 38.0, 37.0, 904, 4),
        ("Ian Bell", 118, 205, 7727, 43.0, 49.0, 918, 39),
        ("Sir Colin Cowdrey", 114, 188, 7624, 44.0, 131.0, 752, 13),
        ("Wally Hammond", 85, 140, 7249, 58.0, 97.0, 512, 27),
        ("Sir Andrew Strauss", 100, 178, 7037, 41.0, 49.0, 867, 10),
        ("Graham Thorpe", 100, 179, 6744, 45.0, 46.0, 778, 9),
        ("Ben Stokes", 105, 190, 6508, 36.0, 60.0, 759, 131),
        ("Jonny Bairstow", 100, 178, 6042, 36.0, 59.0, 721, 56)
    ],
    "most_wickets": [
        ("James Anderson", 188, 6673, 40037, 704, 26.0, 18627, 32, 32),
        ("Stuart Broad", 167, 5616, 33698, 604, 28.0, 16719, 28, 20),
        ("Sir Ian Botham", 102, 3550, 21303, 383, 28.0, 10878, 17, 27),
        ("Bob Willis", 90, 2700, 16201, 325, 25.0, 8190, 12, 16),
        ("Fred Trueman", 67, 2448, 14690, 307, 22.0, 6625, 19, 17),
        ("Derek Underwood", 86, 3464, 20784, 297, 26.0, 7674, 13, 17),
        ("Graeme Swann", 60, 2558, 15349, 255, 30.0, 7642, 14, 17),
        ("Brian Statham", 70, 2495, 14972, 252, 25.0, 6261, 9, 9),
        ("Matthew Hoggard", 67, 2318, 13909, 248, 31.0, 7564, 13, 7),
        ("Sir Alec Bedser", 51, 2425, 14554, 236, 25.0, 5876, 11, 15),
        ("Andy Caddick", 62, 2259, 13558, 234, 30.0, 6999, 9, 13),
        ("Darren Gough", 58, 1970, 11821, 229, 28.0, 6503, 14, 9),
        ("Steve Harmison", 62, 2198, 13192, 222, 32.0, 7091, 11, 8),
        ("Andrew Flintoff", 78, 2458, 14747, 219, 33.0, 7303, 10, 3),
        ("Moeen Ali", 68, 2101, 12610, 204, 37.0, 7612, 13, 5),
        ("Ben Stokes", 105, 1966, 11795, 203, 32.0, 6507, 8, 4)
    ]
        },
        "New Zealand": {
            "schedule": [
                ("Sep 15, Sun - Sep 19, Thu", "New Zealand vs South Africa, 1st Test", "Basin Reserve, Wellington", "10:00 AM GMT"),
                ("Sep 23, Mon - Sep 27, Fri", "New Zealand vs South Africa, 2nd Test", "Hagley Oval, Christchurch", "10:00 AM GMT"),
                ("Oct 05, Sat", "New Zealand vs Bangladesh, 1st T20I", "Eden Park, Auckland", "06:00 AM GMT"),
                ("Oct 08, Tue", "New Zealand vs Bangladesh, 2nd T20I", "Bay Oval, Mount Maunganui", "06:00 AM GMT"),
                ("Oct 11, Fri", "New Zealand vs Bangladesh, 3rd T20I", "Seddon Park, Hamilton", "06:00 AM GMT")
            ],
            "results": [
                ("Aug 10, Sat", "New Zealand vs Pakistan, 1st ODI", "Pakistan won by 5 runs"),
                ("Aug 12, Mon", "New Zealand vs Pakistan, 2nd ODI", "New Zealand won by 2 wickets"),
                ("Aug 15, Thu", "New Zealand vs Pakistan, 3rd ODI", "New Zealand won by 6 wickets"),
                ("Jul 30, Tue", "New Zealand vs Sri Lanka, 1st T20I", "Sri Lanka won by 10 runs"),
                ("Jul 28, Sun", "New Zealand vs Sri Lanka, 2nd T20I", "New Zealand won by 35 runs"),
                ("Jul 25, Thu", "New Zealand vs Sri Lanka, 3rd T20I", "New Zealand won by 7 wickets")
            ],
            "players": {
                "batsmen": [
                    "Kane Williamson", "Ross Taylor", "Martin Guptill", "Tom Latham",
                    "Devdutt Padikkal", "Henry Nicholls", "James Neesham", "Will Young"
                ],
                "all_rounders": [
                    "James Neesham", "Mitchell Santner", "Kyle Jamieson", "Colin de Grandhomme"
                ],
                "wicket_keepers": [
                    "Tom Latham", "Blair Tickner"
                ],
                "bowlers": [
                    "Trent Boult", "Tim Southee", "Kyle Jamieson", "Matt Henry",
                    "Mitchell Santner", "Lockie Ferguson", "Ish Sodhi"
                ]
            },
            "most_runs": [
        ("Kane Williamson", 100, 176, 8743, 55.0, 51.0, 971, 24),
        ("Ross Taylor", 112, 196, 7684, 44.0, 59.0, 932, 55),
        ("Stephen Fleming", 111, 189, 7172, 40.0, 46.0, 917, 26),
        ("Brendon McCullum", 101, 176, 6453, 39.0, 65.0, 776, 107),
        ("Martin Crowe", 77, 131, 5444, 45.0, 45.0, 659, 27),
        ("Tom Latham", 80, 142, 5419, 40.0, 47.0, 617, 19),
        ("John Wright", 82, 148, 5334, 38.0, 36.0, 630, 10),
        ("Nathan Astle", 81, 137, 4702, 37.0, 50.0, 612, 39),
        ("Daniel Vettori", 112, 172, 4523, 30.0, 58.0, 557, 17),
        ("BJ Watling", 75, 117, 3790, 38.0, 43.0, 429, 8),
        ("Bev Congdon", 61, 114, 3448, 32.0, 79.0, 267, 12),
        ("Chris Cairns", 62, 104, 3320, 34.0, 57.0, 365, 87),
        ("Sir Richard Hadlee", 86, 134, 3124, 27.0, 67.0, 343, 33),
        ("Craig McMillan", 55, 91, 3116, 38.0, 55.0, 367, 54),
        ("Glenn Turner", 41, 73, 2991, 45.0, 74.0, 265, 0),
        ("Henry Nicholls", 56, 87, 2973, 37.0, 50.0, 322, 9),
    ],
    "most_wickets": [
    ("Daniel Vettori", 291, 2303, 13820, 297, 32, 9495, 7, 2),
    ("Kyle Mills", 170, 1371, 8230, 240, 27, 6485, 8, 1),
    ("Tim Southee", 161, 1346, 8075, 221, 34, 7447, 5, 3),
    ("Trent Boult", 114, 1030, 6180, 211, 24, 5146, 10, 6),
    ("Chris Harris", 250, 1778, 10667, 203, 38, 7613, 2, 1),
    ("Chris Cairns", 214, 1355, 8132, 200, 33, 6557, 3, 1),
    ("Jacob Oram", 160, 1152, 6911, 173, 29, 5048, 3, 2),
    ("Sir Richard Hadlee", 115, 1019, 6118, 158, 22, 3407, 1, 5),
    ("Shane Bond", 82, 716, 4295, 147, 21, 3070, 7, 4),
    ("Matt Henry", 82, 713, 4277, 141, 26, 3722, 10, 2),
    ("Ewen Chatfield", 114, 1011, 6065, 140, 26, 3618, 3, 1),
    ("Scott Styris", 188, 1019, 6114, 137, 35, 4839, 4, 1),
    ("Danny Morrison", 96, 764, 4586, 126, 28, 3470, 1, 2),
    ("Martin Snedden", 93, 754, 4525, 114, 28, 3237, 1, 0),
    ("Gavin Larsen", 121, 1061, 6368, 113, 35, 4000, 1, 0),
    ("Daryl Tuffey", 94, 722, 4333, 110, 32, 3534, 2, 0),
    ("Mitchell Santner", 104, 812, 4875, 107, 37, 3960, 0, 2),
    ("Chris Pringle", 64, 552, 3314, 103, 24, 2459, 2, 1),
    ("Nathan Astle", 223, 808, 4850, 99, 38, 3809, 1, 0),
    ("Lockie Ferguson", 65, 550, 3300, 99, 32, 3124, 2, 1),
    ("Lance Cairns", 78, 658, 3951, 89, 31, 2717, 2, 1)
]
        },
        "West Indies": {
            "schedule": [
                ("Sep 15, Sun - Sep 19, Thu", "West Indies vs Pakistan, 1st Test", "Queen's Park Oval, Port of Spain", "10:00 AM GMT"),
                ("Sep 23, Mon - Sep 27, Fri", "West Indies vs Pakistan, 2nd Test", "Sabina Park, Kingston", "10:00 AM GMT"),
                ("Oct 05, Sat", "West Indies vs Sri Lanka, 1st T20I", "Kensington Oval, Bridgetown", "08:00 PM GMT"),
                ("Oct 08, Tue", "West Indies vs Sri Lanka, 2nd T20I", "Warner Park, Basseterre", "08:00 PM GMT"),
                ("Oct 11, Fri", "West Indies vs Sri Lanka, 3rd T20I", "Sir Vivian Richards Stadium, North Sound", "08:00 PM GMT")
            ],
            "results": [
                ("Aug 10, Sat", "West Indies vs South Africa, 1st ODI", "South Africa won by 7 wickets"),
                ("Aug 12, Mon", "West Indies vs South Africa, 2nd ODI", "West Indies won by 8 runs"),
                ("Aug 15, Thu", "West Indies vs South Africa, 3rd ODI", "South Africa won by 4 wickets"),
                ("Jul 30, Tue", "West Indies vs England, 1st T20I", "West Indies won by 12 runs"),
                ("Jul 28, Sun", "West Indies vs England, 2nd T20I", "England won by 6 wickets"),
                ("Jul 25, Thu", "West Indies vs England, 3rd T20I", "West Indies won by 5 runs")
            ],
            "players": {
                "batsmen": [
                    "Chris Gayle", "Kieron Pollard", "Evin Lewis", "Shimron Hetmyer",
                    "Nicholas Pooran", "Darren Bravo", "Jason Holder", "Roston Chase"
                ],
                "all_rounders": [
                    "Jason Holder", "Kieron Pollard", "Roston Chase", "Andre Russell"
                ],
                "wicket_keepers": [
                    "Nicholas Pooran", "Shai Hope"
                ],
                "bowlers": [
                    "Sunil Narine", "Jason Holder", "Kemar Roach", "Alzarri Joseph",
                    "Odean Smith", "Andre Russell", "Shannon Gabriel"
                ]
            },
            "most_runs": [
        ("Brian Lara", 131, 232, 11953, 52.0, 79.0, 1184, 34),
        ("Sir Vivian Richards", 121, 187, 8540, 50.0, 55.0, 784, 35),
        ("Shivnarine Chanderpaul", 164, 268, 10842, 45.0, 69.0, 1170, 30),
        ("Chris Gayle", 103, 162, 10480, 37.0, 91.0, 734, 22),
        ("Desmond Haynes", 116, 238, 7487, 42.0, 49.0, 948, 26),
        ("Sir Garfield Sobers", 93, 179, 8032, 57.0, 85.0, 1420, 26),
        ("Sir Clive Lloyd", 102, 188, 7515, 46.0, 70.0, 929, 19),
        ("Rohan Kanhai", 79, 139, 6331, 51.0, 43.0, 702, 14),
        ("Richie Richardson", 128, 224, 5655, 43.0, 78.0, 812, 19),
        ("Marlon Samuels", 71, 125, 5302, 44.0, 62.0, 548, 22),
        ("Kraigg Brathwaite", 54, 93, 3619, 40.0, 21.0, 362, 10),
        ("Sir Everton Weekes", 48, 114, 4455, 58.0, 32.0, 361, 7),
        ("Carl Hooper", 102, 169, 5462, 36.0, 60.0, 741, 20)
    ],
    "most_wickets": [
        ("Courtney Walsh", 132, 5002, 23621, 519, 28.0, 18120, 43, 15),
        ("Sir Curtly Ambrose", 98, 4051, 20565, 405, 25.0, 14308, 38, 22),
        ("Malcolm Marshall", 81, 3821, 17618, 376, 25.0, 12620, 31, 20),
        ("Joel Garner", 58, 2953, 13752, 259, 26.0, 10607, 22, 15),
        ("Michael Holding", 60, 2457, 11319, 249, 23.0, 7937, 19, 17),
        ("Fidel Edwards", 55, 1873, 8525, 166, 27.0, 6181, 13, 5),
        ("Shannon Gabriel", 55, 1804, 9524, 162, 32.0, 6827, 15, 4),
        ("Devendra Bishoo", 58, 2272, 12112, 152, 29.0, 7351, 11, 5),
        ("Sulieman Benn", 57, 2127, 10267, 144, 30.0, 6145, 7, 2),
        ("Ravi Rampaul", 64, 1990, 10235, 139, 31.0, 7103, 8, 4)
    ]
        },
        "South Africa": {
            "schedule": [
                ("Sep 15, Sun - Sep 19, Thu", "South Africa vs New Zealand, 1st Test", "Newlands, Cape Town", "09:30 AM GMT"),
                ("Sep 23, Mon - Sep 27, Fri", "South Africa vs New Zealand, 2nd Test", "SuperSport Park, Centurion", "09:30 AM GMT"),
                ("Oct 05, Sat", "South Africa vs Bangladesh, 1st T20I", "St George's Park, Port Elizabeth", "05:00 PM GMT"),
                ("Oct 08, Tue", "South Africa vs Bangladesh, 2nd T20I", "Kingsmead, Durban", "05:00 PM GMT"),
                ("Oct 11, Fri", "South Africa vs Bangladesh, 3rd T20I", "Wanderers Stadium, Johannesburg", "05:00 PM GMT")
            ],
            "results": [
                ("Aug 10, Sat", "South Africa vs Australia, 1st ODI", "South Africa won by 8 wickets"),
                ("Aug 12, Mon", "South Africa vs Australia, 2nd ODI", "Australia won by 4 wickets"),
                ("Aug 15, Thu", "South Africa vs Australia, 3rd ODI", "South Africa won by 6 wickets"),
                ("Jul 30, Tue", "South Africa vs Zimbabwe, 1st T20I", "South Africa won by 18 runs"),
                ("Jul 28, Sun", "South Africa vs Zimbabwe, 2nd T20I", "South Africa won by 10 runs"),
                ("Jul 25, Thu", "South Africa vs Zimbabwe, 3rd T20I", "South Africa won by 6 wickets")
            ],
            "players": {
                "batsmen": [
                    "Hashim Amla", "AB de Villiers", "Faf du Plessis", "Quinton de Kock",
                    "Rassie van der Dussen", "Temba Bavuma", "David Miller", "Aiden Markram"
                ],
                "all_rounders": [
                    "Andile Phehlukwayo", "Chris Morris", "Dwaine Pretorius", "Jean-Paul Duminy"
                ],
                "wicket_keepers": [
                    "Quinton de Kock", "Heinrich Klaasen"
                ],
                "bowlers": [
                    "Kagiso Rabada", "Lungi Ngidi", "Dale Steyn", "Anrich Nortje",
                    "Keshav Maharaj", "Tabraiz Shamsi", "Sisanda Magala"
                ]
            },
            "most_runs": [
        ("Jacques Kallis", 165, 278, 13206, 55.0, 46.0, 1477, 96),
        ("Hashim Amla", 124, 215, 9282, 47.0, 50.0, 1170, 14),
        ("Graeme Smith", 116, 203, 9253, 49.0, 60.0, 1164, 24),
        ("AB de Villiers", 114, 191, 8765, 51.0, 55.0, 1024, 64),
        ("Gary Kirsten", 101, 176, 7289, 45.0, 43.0, 922, 12),
        ("Herschelle Gibbs", 90, 154, 6167, 42.0, 50.0, 887, 47),
        ("Mark Boucher", 146, 204, 5498, 31.0, 50.0, 654, 20),
        ("Dean Elgar", 86, 152, 5347, 38.0, 48.0, 684, 26),
        ("Daryll Cullinan", 70, 115, 4554, 44.0, 49.0, 548, 25),
        ("Faf du Plessis", 69, 118, 4163, 40.0, 46.0, 516, 21),
        ("Shaun Pollock", 108, 156, 3781, 32.0, 53.0, 412, 35),
        ("Hansie Cronje", 68, 111, 3714, 36.0, 45.0, 409, 33),
        ("Ashwell Prince", 66, 104, 3665, 42.0, 44.0, 397, 13)
    ],
    "most_wickets": [
    ("Dale Steyn", 93, 3101, 18608, 439, 23, 10077, 27, 26),
    ("Shaun Pollock", 108, 4059, 24353, 421, 23, 9733, 23, 16),
    ("Makhaya Ntini", 101, 3472, 20834, 390, 29, 11242, 19, 18),
    ("Allan Donald", 72, 2586, 15519, 330, 22, 7344, 11, 20),
    ("Morne Morkel", 86, 2749, 16498, 309, 28, 8550, 18, 8),
    ("Kagiso Rabada", 64, 1964, 11788, 299, 22, 6603, 14, 14),
    ("Jacques Kallis", 165, 3362, 20172, 291, 33, 9497, 7, 5),
    ("Vernon Philander", 64, 1898, 11391, 224, 22, 5000, 8, 13),
    ("Keshav Maharaj", 52, 1679, 10075, 171, 31, 5264, 6, 9),
    ("Hugh Tayfield", 37, 1852, 11116, 170, 26, 4405, 5, 14),
    ("Paul Adams", 45, 1475, 8850, 134, 33, 4405, 5, 4),
    ("Trevor Goddard", 41, 1768, 10612, 123, 26, 3226, 2, 5),
    ("Andre Nel", 36, 1271, 7630, 123, 32, 3919, 4, 3),
    ("Peter Pollock", 28, 1034, 6206, 116, 24, 2806, 1, 9),
    ("Neil Adcock", 26, 918, 5507, 104, 21, 2195, 5, 5),
    ("Paul Harris", 37, 1468, 8809, 103, 38, 3901, 3, 3)
]

        }
    }
    
    
       

    while True:
        display_main_menu()
        option = input("Enter your choice (1-7): ").strip()

        if option == '1':
            while True:
                display_live_scores_menu()
                sub_choice = input("Enter your choice (1-2): ")
                if sub_choice == '1':
                    display_current_matches()
                elif sub_choice == '2':
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and 2.")
        
        elif option == '2':
            while True:
                display_schedule_menu()
                sub_choice = input("Enter your choice (1-2): ")
                if sub_choice == '1':
                    display_upcoming_matches()
                elif sub_choice == '2':
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and 2.")
        
        elif option == '3':
            while True:
                display_news_menu()
                sub_choice = input("Enter your choice (1-2): ")
                if sub_choice == '1':
                    display_latest_news()
                elif sub_choice == '2':
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and 2.")

            

        elif option == '4':
            display_series_menu()
            

        elif option == '5':
            while True:
                display_teams_menu()
                team_option = input("Enter your choice (1-6): ").strip()

                if team_option == '1':
                    print("International Teams:")
                    for idx, team in enumerate(cricket_teams.keys(), 1):
                        print(f"{idx}. {team}")
                    
                    team_choice = input("Select a team by number: ").strip()
                    selected_team = list(cricket_teams.keys())[int(team_choice) - 1]
                    display_team_menu(selected_team, cricket_teams[selected_team])
                    
                elif team_option == '2':
                    print("Displaying Domestic Teams...in Maintaince")
                    teams = [
    "Chennai Super Kings",
    "Delhi Capitals",
    "Punjab Kings",
    "Kolkata Knight Riders",
    "Mumbai Indians",
    "Rajasthan Royals",
    "Royal Challengers Bengaluru",
    "Sunrisers Hyderabad"
]

                    for index, team in enumerate(teams, start=1):
                        print(index, team)
                    
                elif team_option == '3':
                    break  # Back to Main Menu

        elif option == '6':
            while True:
                display_rankings_menu()
                sub_choice = input("\nEnter your choice: ")
                
                if sub_choice == '1':
                    print("\n***Displaying Team Rankings***")
                    print("\n1. ODI Rankings")
                    print("2. T20I Rankings")
                    print("3. TEST Rankings")
                    
                    team_ranking_choice = input("\nEnter your choice: ")
                    print("\n1. ODI Rankings")
                    print("2. T20I Rankings")
                    print("3. TEST Rankings")
                    
                    if team_ranking_choice == '1':   #1 = ODI, 2 = T20, 3 = TEST
                        print("\n\n                 *** Displaying Top 10 ODI Teams ***")
                        print("\nRank         Team             Matches           Rating          Points")
                        print("\n 1          India               45               118            5298\n 2          Australia           34               116            3936\n 3          South Africa        30               112            3357\n 4          Pakistan            26               106            2762\n 5          New Zealand         33               101            3349\n 6          Sri Lanka           50                97            4825\n 7          England             28                95            2672\n 8          Bangladesh          40                86            3453\n 9          Afghanistan         31                80            2477\n 10         West Indies         32                69            2205")
                        
                    elif team_ranking_choice == '2':
                        print("\n\n                 *** Displaying Top 10 T20I Teams ***")
                        print("\nRank         Team             Matches            Rating          Points")
                        print("\n 1          India               63                267           16835\n 2          Australia           40                256           10241\n 3          England             39                253            9876\n 4          West Indies         46                252           11604\n 5          South Africa        35                251           18777\n 6          New Zealand         49                247           12113\n 7          Pakistan            46                241           11097\n 8          Sri Lanka           40                229            9159\n 9          Bangladesh          50                225           11253\n 10         Afghanistan         39                223            8682")  
                        
                    elif team_ranking_choice == '3':
                        print("\n\n                 *** Displaying Top 10 TEST Teams ***")
                        print("\nRank         Team             Matches          Rating          Points")
                        print("\n 1          Australia           30              124            3715\n 2          India               26              120            3108\n 3          England             34              108            3679\n 4          South Africa        21              104            2179\n 5          New Zealand         22               96            2121\n 6          Pakistan            17               89            1519\n 7          Sri Lanka           18               83            1501\n 8          West Indies         26               77            1992\n 9          Bangladesh          17               53             906\n 10         Ireland              5               26             131")
                        
                elif sub_choice == '2':
                    print("\nDisplaying Player Rankings...")
                    print("1. ODI Rankings")
                    print("2. T20I Rankings")
                    print("3. TEST Rankings")
                    
                    player_ranking_choice = input("\nEnter your choice: ")
                    print("1. ODI Rankings")
                    print("2. T20I Rankings")
                    print("3. TEST Rankings")

                    if player_ranking_choice == '1':    #1 = ODI, 2 = T20, 3 = TEST
                        
                        print("\n   *** Displaying Top 10 ODI Batters ***  ")
                        print("\n  Rank              Player                     Points")
                        print("\n   1              Babar Azam                    824\n   2              Rohit Sharma                  765\n   3              Shubhman Gill                 763\n   4              Harry Tector                  746\n   5              Virat Kohli                   746\n   6              Daryl Mitchell                728\n   7              David Warner                  723\n   8              Pathum Nissanka               708\n   9              Dawid Malan                   707\n   10             Rassie van der Dussen         701                                                                      \n\n ") 
                        
                        print("    *** Displaying Top 10 ODI Bowlers ***")
                        print("\n  Rank         Player                   Points")
                        print("\n   1         Keshav Maharaj               716\n   2         Josh Hazlewood               688\n   3         Adam Zampa                   686\n   4         Kuldeep Yadav                665\n   5         Bernard Scholtz              657\n   6         Mohammad Nabi                656\n   7         Shaheen Afridi               650\n   8         Jasprit Bumrah               645\n   9         Mohammad Siraj               643\n   10        Trent Boult                  642\n\n")                           
                                                                      
                        print("*** Displaying Top 10 ODI All Rounders ***")
                        print("\n  Rank         Player                 Points")
                        print("\n   1          Mohammad Nabi             320\n   2          Shakib Al Hasan           292\n   3          Sikandar Raza             288\n   4          Assad Vala                248\n   5          Rashid Khan               239\n   6          Gerhard Erasmus           238\n   7          Glenn Maxwell             237\n   8          Mitchell Santner          233\n   9          Mehidy Hasan Miraz        230\n   10         Zeeshan Maqsood           229\n")
                        
                    elif player_ranking_choice == '2':    #1 = ODI, 2 = T20, 3 = TEST
                        
                        print("\n    *** Displaying Top 10 T20I Batters ***")
                        print("\n  Rank           Player                Points")
                        print("\n   1           Travis Head              844\n   2           Surya K Yadav            805\n   3           Philip Salt              797\n   4           Yashasvi Jaiswal         757\n   5           Babar Azam               755\n   6           Mohammad Rizwan          746\n   7           Jos Butler               716\n   8           Ruturaj Gaikwad          664\n   9           Brandon King             656\n   10          Johnson Charles          655")
                        
                        print("\n\n    *** Displaying Top 10 T20I Bowlers ***")
                        print("\n  Rank           Player                Points")
                        print("\n   1           Adil Rashid              718\n   2           Anrich Nortje            675\n   3           Rashid Khan              668\n   4           Wanindu Hasaranga        663\n   5           Josh Hazlewood           662\n   6           Akeal Hosein             659\n   7           Adam Zampa               654\n   8           Fazalhaq Farooqi         645\n   9           Maheesh Teekshana        645\n   10          Ravi Bishnoi             640")
                        
                        print("\n\n    *** Displaying Top 10 T20I All Rounders ***")
                        print("\n  Rank           Player                Points")
                        print("\n   1          Marcus Stoinis            211\n   2          Sikandar Raza             208\n   3          Shakib Al Hasan           206\n   4          Wanindu Hasaranga         205\n   5          Mohammad Nabi             204\n   6          Deependra S. Airee        199\n   7          Hardik Pandya             187\n   8          Liam Livingstone          186\n   9          Aiden Markram             174\n   10         Moeen Ali                 174")
                        
                    elif player_ranking_choice == '3':    #1 = ODI, 2 = T20, 3 = TEST
                        print("\n   *** Displaying Top 10 TEST Batters ***")
                        print("\n  Rank           Player                Points")
                        print("\n   1           Joe Root                 872\n   2           Kane Williamson          859\n   3           Babar Azam               768\n   4           Daryl Mitchell           767\n   5           Steven Smith             757\n   6           Rohit Sharma             751\n   7           Harry Brook              749\n   8           Yashasvi Jaiswal         740\n   9           Dimuth Karunaratne       739\n   10          Virat Kohli              737")
                        
                        print("\n\n    ***Displaying Top 10 TEST Bowlers ***")
                        print("\n  Rank           Player                Points")
                        print("\n   1           R. Ashwin                870\n   2           Josh Hazlewood           847\n   3           Jasprit Bumrah           847\n   4           Kagiso Rabada            820\n   5           Pat Cummins              820\n   6           Nathan Lyon              801\n   7           Ravindra Jadeja          788\n   8           Shaheen Afridi           733\n   9           Kyle Jamieson            729\n   10          Prabath Jayasuriya       724")
                        
                        print("\n\n  *** Displaying Top 10 TEST All Rounders ***")
                        print("\n  Rank           Player                Points")
                        print("\n   1         Ravindra Jadeja            444\n   2         R. Ashwin                  322\n   3         Shakib Al Hasan            310\n   4         Joe Root                   284\n   5         Axar Patel                 270\n   6         Ben Stokes                 266\n   7         Jason Holder               265\n   8         Pat Cummins                245\n   9         Chris Woakes               237\n   10        Marco Jansen               225")

                        
                elif sub_choice == '3':
                        main()
                        
                else:
                    print("Invalid choice. Please enter a number between 1 and 3.4")


        elif option == '7':
            print("Thank you for using Cricbuzz! Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
    
# Run the main program
main()
