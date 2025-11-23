import sqlite3

def initialize_db():
    # Connect to the database file (creates it if it doesn't exist)
    conn = sqlite3.connect('stationery.db')
    cursor = conn.cursor()
    
    # Create a table to hold our data
    # SQL is the language we use to talk to the database
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            quantity INTEGER NOT NULL
        )
    ''')
    
    conn.commit() # Save the changes
    conn.close()  # Close the connection



def add_item(name, price, quantity):
    conn = sqlite3.connect('stationery.db')
    cursor = conn.cursor()
    
    # ? is a placeholder that gets filled by the variables at the end
    cursor.execute('INSERT INTO items (name, price, quantity) VALUES (?, ?, ?)', 
                   (name, price, quantity))
    
    conn.commit()
    conn.close()
    print(f"Success: '{name}' added to inventory.")



def view_items():
    conn = sqlite3.connect('stationery.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM items')
    items = cursor.fetchall() # Get all results
    
    print("\n--- CURRENT INVENTORY ---")
    print(f"{'ID':<5} {'Name':<20} {'Price':<10} {'Qty':<5}")
    print("-" * 40)
    
    for item in items:
        # item[0] is ID, item[1] is Name, etc.
        print(f"{item[0]:<5} {item[1]:<20} ${item[2]:<9} {item[3]:<5}")
    print("-" * 40)
    
    conn.close()





def update_item(item_id, new_price, new_qty):
    conn = sqlite3.connect('stationery.db')
    cursor = conn.cursor()
    
    cursor.execute('UPDATE items SET price = ?, quantity = ? WHERE id = ?', 
                   (new_price, new_qty, item_id))
    
    conn.commit()
    conn.close()
    print("Item updated successfully.")



def delete_item(item_id):
    conn = sqlite3.connect('stationery.db')
    cursor = conn.cursor()
    
    cursor.execute('DELETE FROM items WHERE id = ?', (item_id,))
    
    conn.commit()
    conn.close()
    print("Item deleted successfully.")




def main():
    initialize_db() # Make sure table exists before starting
    
    while True:
        print("\n--- STATIONERY SHOP MANAGER ---")
        print("1. Add Item")
        print("2. View Inventory")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            name = input("Enter Item Name: ")
            price = float(input("Enter Price: "))
            qty = int(input("Enter Quantity: "))
            add_item(name, price, qty)
            
        elif choice == '2':
            view_items()
            
        elif choice == '3':
            view_items() # Show items first so they know the ID
            i_id = int(input("Enter ID of item to update: "))
            n_price = float(input("Enter New Price: "))
            n_qty = int(input("Enter New Quantity: "))
            update_item(i_id, n_price, n_qty)
            
        elif choice == '4':
            view_items()
            i_id = int(input("Enter ID of item to delete: "))
            delete_item(i_id)
            
        elif choice == '5':
            print("Exiting program...")
            break
        else:
            print("Invalid choice, please try again.")

# This line starts the program
if __name__ == "__main__":
    main()  






