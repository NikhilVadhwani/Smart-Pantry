# ----------------------------------------------------------
# Smart Pantry - Recipe Recommender & Grocery Planner
# Team: CodeCooks

# Recipe database
recipes = {

    # ---------- VEG ----------
    "pasta": {
        "ingredients": ["pasta", "tomato, salt", "oil"],
        "type": "veg"
    },

    "sandwich": {
        "ingredients": ["bread", "butter", "tomato"],
        "type": "veg"
    },

    "maggi": {
        "ingredients": ["maggi", "salt", "water"],
        "type": "veg"
    },

    "paneer butter masala": {
        "ingredients": ["paneer", "tomato", "butter", "cream", "salt"],
        "type": "veg"
    },

    "aloo paratha": {
        "ingredients": ["potato", "wheat flour", "salt", "oil"],
        "type": "veg"
    },

    "poha": {
        "ingredients": ["poha", "onion", "turmeric", "salt", "oil"],
        "type": "veg"
    },

    "upma": {
        "ingredients": ["sooji", "onion", "salt", "oil"],
        "type": "veg"
    },

    "chole": {
        "ingredients": ["chickpeas", "onion", "tomato", "salt", "spices"],
        "type": "veg"
    },

    # ---------- NON-VEG ----------
    "omelette": {
        "ingredients": ["egg", "salt", "onion", "oil"],
        "type": "non-veg"
    },

    "grilled chicken": {
        "ingredients": ["chicken", "salt", "pepper", "oil"],
        "type": "non-veg"
    },

    "chicken curry": {
        "ingredients": ["chicken", "onion", "tomato", "salt", "oil"],
        "type": "non-veg"
    },

    "fish fry": {
        "ingredients": ["fish", "salt", "turmeric", "oil"],
        "type": "non-veg"
    },

    "egg fried rice": {
        "ingredients": ["rice", "egg", "soy sauce", "salt"],
        "type": "non-veg"
    },

    # ---------- DIET ----------
    "salad": {
        "ingredients": ["lettuce", "tomato", "cucumber", "salt"],
        "type": "diet"
    },

    "oats": {
        "ingredients": ["oats", "milk", "honey"],
        "type": "diet"
    },

    "smoothie": {
        "ingredients": ["banana", "milk", "honey"],
        "type": "diet"
    },

    "sprouts bowl": {
        "ingredients": ["sprouts", "tomato", "onion", "lemon"],
        "type": "diet"
    },

    "fruit bowl": {
        "ingredients": ["apple", "banana", "orange"],
        "type": "diet"
    }
}

# ----------------------------------------------------------
# Pantry list
# ----------------------------------------------------------
pantry = []

print("=====================================")
print("      Welcome to Smart Pantry!       ")
print("=====================================")

while True:
    print("\nChoose an option:")
    print("1. Add item to pantry")
    print("2. View pantry items")
    print("3. Show recipes you can make (with missing ingredients)")
    
    print("4. Filter recipes by category (veg / non-veg / diet)")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # OPTION 1: Add pantry item
    if choice == "1":
        item = input("Enter item name: ").lower()
        if item not in pantry:
            pantry.append(item)
            print(f"'{item}' added to pantry.")
        else:
            print("Item already exists!")

    # OPTION 2: View pantry items
    elif choice == "2":
        if len(pantry) == 0:
            print("Pantry is empty.")
        else:
            print("\nYour pantry contains:")
            for i in pantry:
                print("-", i)

    # OPTION 3: Suggest recipes
    elif choice == "3":
        print("\nChecking available recipes...\n")
        at_least_one = False

        for recipe, data in recipes.items():
            required = data["ingredients"]
            missing = []

            # Check each ingredient
            for ing in required:
                if ing not in pantry:
                    missing.append(ing)

            if len(missing) == 0:
                print(f"✅ You can make: {recipe}")
                at_least_one = True
            else:
                print(f"⚠ {recipe} - Missing {len(missing)} ingredients:")
                print("  Missing:", ", ".join(missing))
                at_least_one = True

        if at_least_one == False:
            print("❌ No recipes match your pantry. Add more items!")

    # OPTION 4: Exit
    elif choice == "5":
        print("Thank you for using Smart Pantry! Goodbye!")
        break

    # OPTION 5: Filter by category
    elif choice == "4":
        c = input("Enter category (veg / non-veg / diet): ").lower()
        found = False

        print(f"\nRecipes in category '{c}':")
        for recipe, data in recipes.items():
            if data["type"] == c:
                print("-", recipe)
                found = True

        if not found:
            print("No recipes found in this category!")

    else:
        print("Invalid choice. Try again!")