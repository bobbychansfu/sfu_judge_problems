MAX_BOOKS = 5
MAX_DAYS = 21

num_books = int(input("How many books would you like to check out? "))
wants_premium = input("Do you need any restricted premium books? (y/n) ").lower() == 'y'

if wants_premium:
  membership = "Premium"
else:
  membership = "Regular"

if num_books > MAX_BOOKS:
  print(f"Sorry, members can only check out {MAX_BOOKS} books at a time.")
else:
  print(f"Thanks! You have been issued a {membership} membership.")
  
  days = int(input("How many days would you like to keep the books? "))
  
  if days > MAX_DAYS:
    print(f"Reminder: books can only be checked out for {MAX_DAYS} days. Please return on time.")
  else:
    print("Enjoy the books!")

