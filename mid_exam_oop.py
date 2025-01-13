class Star_Cinema:
    __hall_list = []

    @classmethod #it can be called on the class itself, rather than on an instance of the class.
    def entry_hall(cls, hall):
        cls.__hall_list.append(hall)


class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        super().__init__()
        self.__seats = {}  
        self.__show_list = [] 
        self.__rows = rows  
        self.__cols = cols 
        self.__hall_no = hall_no 

      
        Star_Cinema.entry_hall(self)

    def entry_show(self, show_id, movie_name, time):
        
        self.__show_list.append((movie_name, show_id, time))

        
        self.__seats[show_id] = [[0 for _ in range(self.__cols)] for _ in range(self.__rows)]

    def book_seats(self, show_id, seat_list):
        if show_id not in self.__seats:
            print("Invalid show ID!")
            return

        for row, col in seat_list:
           
            if row < 0 or row >= self.__rows or col < 0 or col >= self.__cols:
                print(f"Invalid seat: ({row}, {col})")
                continue

           
            if self.__seats[show_id][row][col] == 1:
                print(f"Seat ({row}, {col}) is already booked.")
            else:
                self.__seats[show_id][row][col] = 1
                print(f"Seat ({row}, {col}) booked for show {show_id}")

    def view_show_list(self):
        print("--------- Show List ---------")
        for movie_name, show_id, time in self.__show_list:
            print(f"MOVIE NAME: {movie_name} ({show_id}) SHOW ID:{show_id} TIME:{time}")
        print("-----------------------------")

    def view_available_seats(self, show_id):
        if show_id not in self.__seats:
            print("Invalid show ID!")
            return

        print(f"Updated Seats Matrix for Hall {self.__hall_no}:")
        for row in self.__seats[show_id]:
            print(row)



def main():
    hall1 = Hall(5, 5, "Hall 1")

  
    hall1.entry_show("111", "Jawan Maji", "11:00 AM")
    hall1.entry_show("333", "Sujon Maji", "2:00 PM")
    

    while True:
        print("\n1. VIEW ALL SHOW TODAY")
        print("2. VIEW AVAILABLE SEATS")
        print("3. BOOK TICKET")
        print("4. Exit")
        option = input("ENTER OPTION: ")

        if option == "1":
            hall1.view_show_list()
        elif option == "2":
            show_id = input("ENTER SHOW ID: ")
            hall1.view_available_seats(show_id)
        elif option == "3":
            show_id = input("Show ID: ")
            num_tickets = int(input("Number of Ticket?: "))
            seat_list = []
            for _ in range(num_tickets):
                row = int(input("Enter Seat Row: "))
                col = int(input("Enter Seat Col: "))
                seat_list.append((row, col))
            hall1.book_seats(show_id, seat_list)
        elif option == "4":
            print("Exiting...")
            break
        else:
            print("Invalid option! Please try again.")


# Run the program
if __name__ == "__main__":
    main()
