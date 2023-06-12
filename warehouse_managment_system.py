import sqlite3
from product import Product


# algorytm podobieństwa LCS
def longest_common_subsequence(text1, text2):
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]


class WarehouseManagementSystem:
    def __init__(self):
        self.cursor = None
        self.connection = None
        self.products = []

    def connect_to_database(self, path="db/database.db"):
        self.connection = sqlite3.connect(path)
        self.cursor = self.connection.cursor()

        # Fetch products
        rows = self.cursor.execute("SELECT * FROM Warehouse")
        for row in rows:
            item = Product(row[0], row[1], row[2], row[3], row[4])
            self.products.append(item)

    def disconnect_from_database(self):
        self.connection.close()

    def add_product(self, name, description, price, quantity):
        if name in self.products:
            raise ValueError("Product with the same name already exists.")

        self.cursor.execute("INSERT INTO Warehouse (name, description, price, quantity) VALUES (?,?,?,?)",
                            (name, description, price, quantity))
        self.connection.commit()

        print("Product added successfully.")

    def remove_product(self, product_id):
        self.cursor.execute("DELETE FROM Warehouse WHERE ProductId = ?", (product_id,))
        self.connection.commit()

        print("Product removed successfully.")

    def search_product(self, keyword):
        results = []
        for product in self.products:
            if keyword.lower() in product.name.lower() or keyword.lower() == product.product_id:
                results.append(product)
            else:
                lcs_length = longest_common_subsequence(product.name, keyword)
                similarity = lcs_length / max(len(product.name), len(keyword))
                if similarity >= 0.5:  # próg podobieństwa
                    results.append(product)
        return results

    def update_product_quantity(self, product_id, name, description, price, quantity):

        if int(product_id) not in [product.product_id for product in self.products]:
            raise ValueError("Product not found.")

        update_values = {}

        if name != '':
            update_values['name'] = name
        if description != '':
            update_values['description'] = description
        if price != '':
            update_values['price'] = price
        if quantity != '':
            update_values['quantity'] = quantity

        if not update_values:
            print("No fields to update.")
            return

        # Tworzy zapytanie SET używając keys z update_values
        # w postaci "nazwa_kolumny = ?".
        set_clause = ', '.join([f"{column} = ?" for column in update_values.keys()])

        # Tworzy krotke wartosci
        values = tuple(update_values.values())

        # Tworzy query
        query = f"UPDATE Warehouse SET {set_clause} WHERE ProductId = ?"

        # Dodawanie jednoelementowej krotki product_id
        values += (product_id,)

        self.cursor.execute(query, values)
        self.connection.commit()
        print("Warehouse updated successfully.")

    def generate_report(self):
        # # Fetch products
        # self.products = []
        # rows = self.cursor.execute("SELECT * FROM Warehouse")
        # for row in rows:
        #     item = Product(row[0], row[1], row[2], row[3], row[4])
        #     self.products.append(item)

        print("Warehouse Report:")
        for product in self.products:
            print("Product ID:", product.product_id)
            print("Name:", product.name)
            print("Description:", product.description)
            print("Price:", product.price)
            print("Quantity:", product.quantity)
            print("---------------------")

    def run(self):
        while True:
            # Fetch products
            self.products = []
            rows = self.cursor.execute("SELECT * FROM Warehouse")
            for row in rows:
                item = Product(row[0], row[1], row[2], row[3], row[4])
                self.products.append(item)

            print("\nWarehouse Management System Menu:")
            print("1. Add Product")
            print("2. Search Product")
            print("3. Update Product")
            print("4. Generate Report")
            print("5. Remove Product")
            print("5. Exit")

            choice = input("Enter your choice: ")
            print("---------------------\n")
            if choice == '1':
                name = input("Enter product name: ")
                description = input("Enter product description: ")
                price = input("Enter product price: ")
                if not price.isdigit():
                    print("To nie jest liczba!")
                    continue
                quantity = input("Enter product quantity: ")
                if not quantity.isdigit():
                    print("To nie jest liczba!")
                    continue
                try:
                    self.add_product(name, description, price, quantity)
                except ValueError as e:
                    print("Error:", str(e))
            elif choice == '2':
                keyword = input("Enter search keyword: ")
                results = self.search_product(keyword)
                if results:
                    print("\nSearch results:")
                    for product in results:
                        print("Product ID:", product.product_id)
                        print("Name:", product.name)
                        print("Quantity:", product.quantity)
                        print("Price:", product.price)
                        print("---------------------")
                else:
                    print("No matching products found.")
            elif choice == '3':
                product_id = input("Enter product ID: ")
                if not product_id.isdigit():
                    print('This is not an digit!')
                    continue
                name = input("Enter new name (Enter if none): ")
                description = input("Enter new description (Enter if none): ")
                price = input("Enter new price (Enter if none): ")
                if not price.isdigit() and len(price) != 0:
                    print('This is not an digit!')
                    continue
                quantity = input("Enter new quantity (Enter if none): ")
                if not quantity.isdigit() and len(quantity) != 0:
                    print('This is not an digit!')
                    continue

                self.update_product_quantity(product_id, name, description, price, quantity)
            elif choice == '4':
                self.generate_report()
            elif choice == '5':
                product_id = input("Enter product ID: ")
                if not product_id.isdigit():
                    print('This is not an digit!')
                    continue
                self.remove_product(product_id)
            elif choice == '6':
                break
            else:
                print("Invalid choice. Please try again.")
