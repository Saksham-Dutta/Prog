import os

def clear_screen():
    
    os.system('cls' if os.name == 'nt' else 'clear')

def voting_system():
    
    candidates = {
        "1": {"name":"Blue Party", "votes": 0},
        "2": {"name":"Red Party", "votes": 0},
        "3": {"name":"Green Party", "votes": 0},
        "4": {"name":"NOTA (None of the Above)", "votes": 0}
    }
    
    
    voted_ids = set()
    
    while True:
        clear_screen()
        print("=======================================")
        print("  WELCOME TO THE DIGITAL VOTING SYSTEM ")
        print("=======================================")
        print("1. Cast your Vote")
        print("2. View Live Results (Admin Only)")
        print("3. Exit System")
        print("=======================================")
        
        choice = input("Select an option (1-3): ").strip()
        
        if choice == '1':
            clear_screen()
            print(" CAST YOUR VOTE ")
            voter_id = input("Enter your unique Voter ID: ").strip().upper()
            
            
            if not voter_id:
                print(" Voter ID cannot be empty!")
                input("\nPress Enter to return to main menu...")
                continue
                
            if voter_id in voted_ids:
                print("Access Denied: This Voter ID has already cast a ballot.")
                input("\nPress Enter to return to main menu...")
                continue
            
            print("\n--- CANDIDATES ---")
            for key, info in candidates.items():
                print(f"[{key}] {info['name']}")
                
            vote_choice = input("\nEnter the number of your choice: ").strip()
            
            if vote_choice in candidates:
                candidates[vote_choice]["votes"] += 1
                voted_ids.add(voter_id)
                print("\n🎉 Vote cast successfully! Thank you for participating.")
            else:
                print("\n Invalid choice. Your vote was not recorded.")
                
            input("\nPress Enter to return to main menu...")

        elif choice == '2':
            clear_screen()
            
            admin_pass = input("Enter Admin Password to view results: ")
            if admin_pass == "admin123":
                clear_screen()
                print("---  CURRENT VOTING RESULTS ---")
                total_votes = len(voted_ids)
                print(f"Total Turnout: {total_votes} votes\n")
                
                
                for info in candidates.values():
                    print(f" {info['name']}: {info['votes']} votes")
                print("---------------------------------")
            else:
                print(" Incorrect password. Access denied.")
                
            input("\nPress Enter to return to main menu...")

        elif choice == '3':
            print("\nShutting down voting system. Have a great day!")
            break
            
        else:
            print("Invalid selection. Please choose 1, 2, or 3.")
            input("\nPress Enter to return to main menu...")

if __name__ == "__main__":
    voting_system()
