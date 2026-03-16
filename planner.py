# Agenda de pagamento

events = {}

while True:
    print("\n1 - Add event")
    print("2 - Remove event")
    print("3 - Show events")
    print("4 - Exit")
    
    choice = input("Choose an option: ")
    
    if choice == "1":
        date = input("Enter date (DD-MM): ")
        
        if date in events:
            print("This date already has a payment event.")
        else:
            value = input("Enter payment value: ")
            events[date] = value
            print("Event added.")
            
    elif choice == "2":
        date = input("Enter date to remove (DD-MM): ")
        
        if date in events:
            del events[date]
            print("Event removed.")
        else:
            print("No event found on this date.")
            
            
    elif choice =="3":
        if len(events) == 0:
            print("No events scheduled.")
        else:
            for date in events:
                print(date, "-", events[date])
                
    elif choice == "4":
        break