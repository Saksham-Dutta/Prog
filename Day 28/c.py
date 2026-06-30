class Movie:
    def __init__(self, title, rows, cols, price):
        self.title = title
        self.rows = rows
        self.cols = cols
        self.price = price
        # Create a 2D grid representing seats: 'O' means Available, 'X' means Booked
        self.seating_chart = [["O" for _ in range(cols)] for _ in range(rows)]

    def display_seats(self):
        print(f"\n--- Seating Chart for {self.title} ---")
        print("Screen This Way")
        print("  " + " ".join([str(c + 1) for c in range(self.cols)]))  # Column numbers
        
        for i, row in enumerate(self.seating_chart):
            # Row letter identification (A, B, C...)
            row_letter = chr(65 + i) 
            print(f"{row_letter} " + " ".join(row))
        print(" Legend: [O] Available  [X] Booked\n")

    def book_seats(self, seat_list):
        """Accepts a list of seat strings like ['A1', 'A2']"""
        total_cost = 0
        seats_to_confirm = []

        for seat in seat_list:
            seat = seat.upper().strip()
            if len(seat) < 2:
                print(f" Invalid seat format: {seat}")
                return False

            row_letter = seat[0]
            col_str = seat[1:]

            
            row_idx = ord(row_letter) - 65
             
            try:
                col_idx = int(col_str) - 1
            except ValueError:
                print(f" Invalid column format: {col_str}")
                return False

            # Validation checks
            if row_idx < 0 or row_idx >= self.rows or col_idx < 0 or col_idx >= self.cols:
                print(f" Seat {seat} is out of bounds for this theater.")
                return False
            
            if self.seating_chart[row_idx][col_idx] == "X":
                print(f" Seat {seat} is already booked!")
                return False

            seats_to_confirm.append((row_idx, col_idx))
            total_cost += self.price

        # If all requested seats are valid and free, lock them in
        for r, c in seats_to_confirm:
            self.seating_chart[r][c] = "X"
        
        print(f" Success! Booked seats: {', '.join(seat_list)}")
        print(f" Total Amount Paid: ${total_cost:.2f}")
        return True


class TicketSystem:
    def __init__(self):
        self.movies = {}

    def add_movie(self, title, rows, cols, price):
        self.movies[title.lower()] = Movie(title, rows, cols, price)

    def get_movie(self, title):
        return self.movies.get(title.lower(), None)

    def show_movies(self):
        print("\n=== NOW SHOWING ===")
        for movie in self.movies.values():
            print(f"🎬 {movie.title} | Price: ${movie.price:.2f} per seat")


# --- Interactive CLI Menu ---
def main():
    system = TicketSystem()
    
    # Pre-loading data (Movie Title, Rows, Columns, Ticket Price)
    system.add_movie("Inception", 5, 6, 12.50)  # 5 rows (A-E), 6 columns (1-6)
    system.add_movie("The Batman", 4, 8, 15.00) # 4 rows (A-D), 8 columns (1-8)

    while True:
        print("\n====== 🎟️ TICKET BOOKING SYSTEM ======")
        print("1. View Available Movies")
        print("2. View Seating Chart")
        print("3. Book Tickets")
        print("4. Exit")
        
        choice = input("Select an option (1-4): ").strip()

        if choice == "1":
            system.show_movies()

        elif choice == "2":
            system.show_movies()
            title = input("\nEnter movie name to view seats: ")
            movie = system.get_movie(title)
            if movie:
                movie.display_seats()
            else:
                print(" Movie not found.")

        elif choice == "3":
            system.show_movies()
            title = input("\nEnter movie name to book tickets: ")
            movie = system.get_movie(title)
            
            if movie:
                movie.display_seats()
                seats_input = input("Enter seats to book separated by commas (e.g., A1, A2): ")
                # Split comma-separated inputs into a clean list
                seats_to_book = [s.strip() for s in seats_input.split(",") if s.strip()]
                
                if seats_to_book:
                    movie.book_seats(seats_to_book)
                else:
                    print(" No seats entered.")
            else:
                print(" Movie not found.")

        elif choice == "4":
            print("Enjoy your movie! Goodbye!")
            break
        else:
            print(" Invalid option. Try again.")

if __name__ == "__main__":
    main()