#!/usr/bin/env python3
# Author Mikhail Ibrahim
# Date 2025/05/21
# Filename: hst_store_simulator.py
# Description: Crash-proof Python program allowing users to calculate HST or explore dynamic virtual stores.
# Calculates 13% HST on items, provides menu navigation, and simulates new inventory shipments each store visit.

import random


# Function to calculate total with HST
def calculate_total_with_tax(price):
    tax = price * 0.13
    total = price + tax
    return total


# Store item database
store_items = {
    "1": {
        "name": "Grocery Store",
        "items": [
            {
                "name": "Organic Apples",
                "price": 4.99,
                "desc": "Crisp, juicy, locally grown apples.",
            },
            {
                "name": "Almond Milk",
                "price": 3.49,
                "desc": "Unsweetened and dairy-free.",
            },
            {
                "name": "Eggs (Dozen)",
                "price": 5.19,
                "desc": "Farm-fresh, free-range eggs.",
            },
            {
                "name": "Peanut Butter",
                "price": 6.75,
                "desc": "Natural smooth peanut butter.",
            },
        ],
    },
    "2": {
        "name": "Electronics Store",
        "items": [
            {
                "name": "Bluetooth Speaker",
                "price": 59.99,
                "desc": "Portable speaker with 10-hour battery.",
            },
            {
                "name": "Smartphone",
                "price": 899.99,
                "desc": "Latest-gen Android with AMOLED display.",
            },
            {
                "name": "Laptop",
                "price": 1249.99,
                "desc": "Powerful i7 with 16GB RAM and SSD.",
            },
            {
                "name": "Wireless Headphones",
                "price": 199.99,
                "desc": "Noise-cancelling and water-resistant.",
            },
        ],
    },
    "3": {
        "name": "Vehicle Dealership",
        "items": [
            {
                "name": "Dodge Hellcat SRT",
                "price": 150450.00,
                "desc": "Supercharged V8, 717 horsepower.",
            },
            {
                "name": "Toyota Corolla",
                "price": 23495.00,
                "desc": "Reliable compact sedan.",
            },
            {
                "name": "Tesla Model 3",
                "price": 44990.00,
                "desc": "Electric with autopilot features.",
            },
            {
                "name": "Lamborghini Urus SE",
                "price": 272000.00,
                "desc": "Luxury performance SUV.",
            },
        ],
    },
    "4": {
        "name": "Clothing Store",
        "items": [
            {
                "name": "Designer Jacket",
                "price": 249.99,
                "desc": "Waterproof and wind-resistant.",
            },
            {"name": "Sneakers", "price": 179.99, "desc": "Air-cushioned for comfort."},
            {"name": "Graphic Tee", "price": 34.99, "desc": "100% organic cotton."},
            {
                "name": "Leather Boots",
                "price": 299.99,
                "desc": "Handcrafted, genuine leather.",
            },
        ],
    },
}


# Fun store simulation
def fun_mode():
    print("\n🎉 Welcome to Fun Mode! Explore our virtual stores.")

    for key in store_items:
        print(f"{key}. {store_items[key]['name']}")

    # Store selection
    while True:
        store_choice = input("Select a store (1-4): ")
        if store_choice in store_items:
            break
        else:
            print("Invalid store selection. Please choose a number between 1 and 4.")

    selected_store = store_items[store_choice]
    store_name = selected_store["name"]

    # Randomize inventory for this visit
    inventory = random.sample(selected_store["items"], k=4)

    print(f"\n🛍️ Welcome to the {store_name}!")
    print("Here are the items currently in stock:\n")
    for i, item in enumerate(inventory, start=1):
        print(f"{i}. {item['name']} - ${item['price']:.2f}")

    while True:
        try:
            item_choice = int(input("\nSelect an item to learn more (1-4): "))
            if 1 <= item_choice <= 4:
                selected_item = inventory[item_choice - 1]
                break
            else:
                print("Invalid choice. Please pick between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    print(f"\nℹ️ {selected_item['name']} - {selected_item['desc']}")

    # Ask to buy
    while True:
        buy = input("Would you like to purchase this item? (yes/no): ").lower()
        if buy in ["yes", "no"]:
            break
        print("Please enter yes or no.")

    if buy == "yes":
        total = calculate_total_with_tax(selected_item["price"])
        print("\n💰 Purchase Summary:")
        print(f"Subtotal: ${selected_item['price']:.2f}")
        print(f"HST (13%): ${selected_item['price'] * 0.13:.2f}")
        print(f"Total: ${total:.2f}")
    else:
        print("👍 No worries! Maybe next time.")

    print(
        "\n🛒 Thank you for visiting! The store inventory will be refreshed next time."
    )


# Manual tax calculator
def manual_mode():
    print("\n🔢 Manual Mode: Calculate total with HST from any price.")
    while True:
        try:
            price = float(input("Enter the price of your item: $"))
            if price <= 0:
                print("Price must be greater than zero.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    total = calculate_total_with_tax(price)
    print("\n📊 HST Calculation:")
    print(f"Subtotal: ${price:.2f}")
    print(f"HST (13%): ${price * 0.13:.2f}")
    print(f"Total with HST: ${total:.2f}")


# Main menu
def main():
    print("📦 Welcome to the HST Calculator and Store Simulator!")
    print("This program helps you calculate totals with tax or shop in fun mode.\n")

    while True:
        print("\n--- Main Menu ---")
        print("1. Fun Mode (Explore stores and items)")
        print("2. Manual Mode (Enter your own price)")
        print("3. Exit")

        try:
            choice = int(input("Choose an option (1-3): "))
            if choice == 1:
                fun_mode()
            elif choice == 2:
                manual_mode()
            elif choice == 3:
                print("\n✅ Thank you for using the HST Calculator. Goodbye!")
                break
            else:
                print("Please enter a valid number from 1 to 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")


# Run the program
if __name__ == "__main__":
    main()
