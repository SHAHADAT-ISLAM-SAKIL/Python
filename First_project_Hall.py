class Star_Cinema:
    def __init__(self) -> None:
        self.hall_list = []

    def entry_hall(self, hall_object):
        self.hall_list.append(hall_object)

class Hall:
    def __init__(self, rows, cols, hall_no):
        self.seats1 = {}
        self.seats2 = {}
        self.show_list = []
        self._rows = rows
        self._cols = cols
        self.hall_no = hall_no

    def entry_show(self, id, movie_name, time):
       
        information = (id, movie_name, time)
        self.show_list.append(information)

    def view_show_list(self):
        print("Shows running today:")
        for show in self.show_list:
            print(f"ID: {show[0]}, Movie: {show[1]}, Time: {show[2]}PM")

    def allocate_seats(self):
        print("\nMovi ID 101 are  Availabe sit:\n")
        for i in range(self._rows):
            i = i+1
            for j in range(self._cols):
                j = j+1
                print(self.seats1.get((i, j), 0), end=" ")
            print()
        print("\nMovi ID 152 are  Availabe sit:\n")
        for i in range(self._rows):
             i = i+1
             for j in range(self._cols):
                j = j+1
                print(self.seats2.get((i, j), 0), end=" ")
             print()


    def book_seats1(self,row, col):
         key = (row, col)
         if key in self.seats1 and self.seats1[key] == '*':
          print("\nAlready booked\n")
         else:
          self.seats1[key] = '*'
          print(f'\nSuccessfully booked seat {row,col}, Movie ID: {id}\n')

    def book_seats2(self,row, col):
         key = (row, col)
         if key in self.seats2 and self.seats2[key] == '*':
          print("\nAlready booked\n")
         else:
          self.seats2[key] = '*'
          print(f'\nSuccessfully booked seat {row,col}, Movie ID: {id}\n')
        

    def view_available_seats(self):
        print("\nMovi ID 101 are  Availabe sit:\n")
        for i in range(self._rows):
            i = i+1
            for j in range(self._cols):
                j = j+1
                print(self.seats1.get((i, j), 0), end=" ")
            print()
        
        print("\nMovi ID 152 are  Availabe sit:\n")

        for i in range(self._rows):
            i = i+1
            for j in range(self._cols):
                j = j+1
                print(self.seats2.get((i, j), 0), end=" ")
            print()
           
#Admin panel:
star_cinema = Star_Cinema()
hall_no = 1
main_row = 10
main_col = 10
hall = Hall(main_row,main_col, hall_no)
star_cinema.entry_hall(hall)

hall.entry_show(101, 'Hero', 2)
hall.entry_show(152, 'Hacker', 4)
#User panel:
while True:
    print("\n1. View All Show Today")
    print("2. View Available Seats")
    print("3. Book Ticket")
    print("4. Exit\n")
    x = int(input("Enter Option :"))

    if x == 1:
        hall.view_show_list()
        hall.allocate_seats()
    elif x == 2:
        hall.view_available_seats()

    elif x == 3:
        print("\nWhic movi ticket Do You need?\n")
        id = (int(input("Enput Movie ID : ")))
        if id == 101:
         ticket = int(input("Number of seats: "))
         for _ in range(ticket):
            row = int(input("Enter a row number: "))
            col = int(input("Enter a col number: "))
            if row <= main_row and col <= main_col:
             hall.book_seats1(row, col)
            else:
                print("\nInvalid Row or column\n")

        elif id == 152:
            ticket = int(input("Number of seats: "))
            for _ in range(ticket):
             row = int(input("Enter a row number: "))
             col = int(input("Enter a col number: "))
             if row <= main_row and col <= main_col:
              hall.book_seats1(row, col)
             else:
                print("\nInvalid Row or column\n")
        else:
            print("\nInvalid id! try Again\n")

    elif x == 4:
        print("\nThank You! Come Back Again.\n")
        break
    else:
        print("\nInvalid Option! Try Again\n")
