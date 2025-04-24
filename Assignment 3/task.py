def customerBooking():
    form_of_id = input("Enter form of ID (e.g., Passport, Driver's License): ")
    id_number = input("Enter ID number: ")
    name = input("Enter name: ")
    ticket_id = input("Enter ticket ID: ")
    return form_of_id, id_number, name, ticket_id

def ferry_service_total():
    form_of_id, id_number, name, ticket_id = customerBooking()
    total = 0.0
    print("\nEnter service names and their prices (type 'done' to finish):")
    while True:
        service_name = input("Service name: ")
        if service_name.lower() == "done":
            break
        try:
            price = float(input(f"Price for {service_name}: $"))
            total += price
        except ValueError:
            print("Invalid input. Please enter a numeric value for price.")
    return form_of_id, id_number, name, ticket_id, total

def booking_approval():
    form, idnum, name, ticket, total_cost = ferry_service_total()
    status = "Pending"
    approval_ref = None
    manager_decision = input("Do you approve this booking? (yes/no): ").lower()
    if manager_decision == "yes":
        status = "Approved"
        approval_ref = idnum[:3] + ticket[-2:]
    print(f"\nTotal: ${total_cost:.2f}")
    print(f"Status: {status}")
    if approval_ref:
        print(f"Approval Reference Number: {approval_ref}")

booking_approval()