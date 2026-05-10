import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysql"
)
mycursor = mydb.cursor()

# Create the database if it doesn't exist
mycursor.execute("CREATE DATABASE IF NOT EXISTS VanillaBeauty")

# CONNECT TO DATABASE
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="mysql",
    database="VanillaBeauty"
)
mycursor = mydb.cursor()

# CREATE TABLE 1 - USERS
mycursor.execute("""
    CREATE TABLE IF NOT EXISTS Users (
        ContactNumber BIGINT,
        EmailID VARCHAR(50),
        Username VARCHAR(30) PRIMARY KEY,
        Password VARCHAR(30)
    );
""")

# CREATE TABLE 2 - PRODUCTS
mycursor.execute("""
    CREATE TABLE IF NOT EXISTS Products (
        ProductID INT AUTO_INCREMENT PRIMARY KEY,
        Brand VARCHAR(50),
        ProductName VARCHAR(50),
        Price DECIMAL(10,2)
    );
""")

# CREATE TABLE 3 - TRANSACTIONS
mycursor.execute("""
    CREATE TABLE IF NOT EXISTS Transactions (
        TransactionID INT PRIMARY KEY AUTO_INCREMENT,
        Username VARCHAR(50),
        TransactionData TEXT,
        Quantity INT DEFAULT '1',
        Total DECIMAL(10,2),
        FOREIGN KEY (Username) REFERENCES Users(Username)
    );
""")

mycursor.execute("ALTER TABLE Products AUTO_INCREMENT = 001;")

# CREATE TABLE 4 - FEEDBACK
mycursor.execute("""
    CREATE TABLE IF NOT EXISTS feedback (
        id INT AUTO_INCREMENT PRIMARY KEY,
        user_id VARCHAR(100),
        feedback_text TEXT NOT NULL,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
""")

products = [
    ("Fenty Beauty", "Black eyeliner", 2000.00),
    ("Fenty Beauty", "Blue eyeliner", 2500.00),
    ("Fenty Beauty", "White eyeliner", 2000.00),
    ("Fenty Beauty", "Pink Chrome eyeliner", 3000.00),
    ("Fenty Beauty", "Dark Green eyeliner", 3000.00),
    ("Fenty Beauty", "Pink lipstick", 3900.00),
    ("Fenty Beauty", "Red Lipstick", 3500.00),
    ("Fenty Beauty", "Crimson Red Lipstick", 3500.00),
    ("Fenty Beauty", "Dark Red Lipstick", 4000.00),
    ("Fenty Beauty", "Nude Lipstick", 3500.00),
    ("Fenty Beauty", "Pink Blush", 2300.00),
    ("Fenty Beauty", "Red Blush", 2500.00),
    ("Fenty Beauty", "Orange Blush", 2100.00),
    ("Fenty Beauty", "Purple Blush", 2400.00),
    ("Fenty Beauty", "Burgundy Blush", 2300.00),
    ("Fenty Beauty", "Chestnut Foundation", 5000.00),
    ("Fenty Beauty", "Tan Foundation", 5000.00),
    ("Fenty Beauty", "Caramel Foundation", 5000.00),
    ("Fenty Beauty", "Hazel Foundation", 5000.00),
    ("Fenty Beauty", "Ollie Foundation", 5000.00),
    ("Fenty Beauty", "Clear Lipgloss", 1500.00),
    ("Fenty Beauty", "Pink Tinted Lipgloss", 2000.00),
    ("Fenty Beauty", "Chocolate Lipgloss", 1500.00),
    ("Fenty Beauty", "Berry Lipgloss", 2000.00),
    ("Fenty Beauty", "Choco Mint Lipgloss", 2000.00),
    ("Fenty Beauty", "Metallic Eyeshadow Palette", 6500.00),
    ("Fenty Beauty", "Pastel Eyeshadow Palette", 6900.00),
    ("Fenty Beauty", "Liquid Palette", 5500.00),
    ("Fenty Beauty", "Loose Glitter Palette", 5900.00),
    ("Fenty Beauty", "Cream Palette", 5300.00),
    ("Rare Beauty", "Black eyeliner", 1700.00),
    ("Rare Beauty", "Blue eyeliner", 1900.00),
    ("Rare Beauty", "White eyeliner", 2000.00),
    ("Rare Beauty", "Pink Chrome eyeliner", 2000.00),
    ("Rare Beauty", "Dark Green eyeliner", 2100.00),
    ("Rare Beauty", "Pink lipstick", 1500.00),
    ("Rare Beauty", "Red Lipstick", 1700.00),
    ("Rare Beauty", "Crimson Red Lipstick", 2500.00),
    ("Rare Beauty", "Dark Red Lipstick", 1900.00),
    ("Rare Beauty", "Nude Lipstick", 1900.00),
    ("Rare Beauty", "Pink Blush", 3000.00),
    ("Rare Beauty", "Red Blush", 3500.00),
    ("Rare Beauty", "Orange Blush", 3100.00),
    ("Rare Beauty", "Purple Blush", 3400.00),
    ("Rare Beauty", "Burgundy Blush", 3300.00),
    ("Rare Beauty", "Chestnut Foundation", 5000.00),
    ("Rare Beauty", "Tan Foundation", 5000.00),
    ("Rare Beauty", "Caramel Foundation", 5000.00),
    ("Rare Beauty", "Hazel Foundation", 5000.00),
    ("Rare Beauty", "Ollie Foundation", 5000.00),
    ("Rare Beauty", "Clear Lipgloss", 1000.00),
    ("Rare Beauty", "Pink Tinted Lipgloss", 1500.00),
    ("Rare Beauty", "Metallic Eyeshadow Palette", 4500.00),
    ("Rare Beauty", "Pastel Eyeshadow Palette", 5000.00),
    ("Rare Beauty", "Liquid Palette", 5500.00),
    ("Rare Beauty", "Loose Glitter Palette", 5800.00),
    ("Rare Beauty", "Cream Palette", 5200.00),
    ("Haus Labs", "Black eyeliner", 1900.00),
    ("Haus Labs", "Blue eyeliner", 1800.00),
    ("Haus Labs", "White eyeliner", 2000.00),
    ("Haus Labs", "Pink Chrome eyeliner", 2100.00),
    ("Haus Labs", "Dark Green eyeliner", 2200.00),
    ("Haus Labs", "Pink lipstick", 1400.00),
    ("Haus Labs", "Red Lipstick", 1800.00),
    ("Haus Labs", "Crimson Red Lipstick", 1500.00),
    ("Haus Labs", "Dark Red Lipstick", 1750.00),
    ("Haus Labs", "Nude Lipstick", 1500.00),
    ("Haus Labs", "Pink Blush", 4000.00),
    ("Haus Labs", "Red Blush", 4500.00),
    ("Haus Labs", "Orange Blush", 3800.00),
    ("Haus Labs", "Purple Blush", 4100.00),
    ("Haus Labs", "Burgundy Blush", 4000.00),
    ("Haus Labs", "Chestnut Foundation", 5000.00),
    ("Haus Labs", "Tan Foundation", 5000.00),
    ("Haus Labs", "Caramel Foundation", 5000.00),
    ("Haus Labs", "Hazel Foundation", 5000.00),
    ("Haus Labs", "Ollie Foundation", 5000.00),
    ("Haus Labs", "Clear Lipgloss", 1500.00),
    ("Haus Labs", "Pink Tinted Lipgloss", 1700.00),
    ("Haus Labs", "Chocolate Lipgloss", 1500.00),
    ("Haus Labs", "Berry Lipgloss", 2000.00),
    ("Haus Labs", "Choco Mint Lipgloss", 2000.00),
    ("Haus Labs", "Metallic Eyeshadow Palette", 5500.00),
    ("Haus Labs", "Pastel Eyeshadow Palette", 5500.00),
    ("Haus Labs", "Liquid Palette", 5500.00),
    ("Haus Labs", "Loose Glitter Palette", 6000.00),
    ("Haus Labs", "Cream Palette", 5300.00),
    ("r.e.m Beauty", "Black eyeliner", 1800.00),
    ("r.e.m Beauty", "Blue eyeliner", 1900.00),
    ("r.e.m Beauty", "White eyeliner", 2000.00),
    ("r.e.m Beauty", "Pink Chrome eyeliner", 2000.00),
    ("r.e.m Beauty", "Dark Green eyeliner", 1700.00),
    ("r.e.m Beauty", "Pink lipstick", 2000.00),
    ("r.e.m Beauty", "Red Lipstick", 1900.00),
    ("r.e.m Beauty", "Crimson Red Lipstick", 2500.00),
    ("r.e.m Beauty", "Dark Red Lipstick", 2000.00),
    ("r.e.m Beauty", "Nude Lipstick", 2500.00),
    ("r.e.m Beauty", "Pink Blush", 2500.00),
    ("r.e.m Beauty", "Red Blush", 3000.00),
    ("r.e.m Beauty", "Orange Blush", 2100.00),
    ("r.e.m Beauty", "Purple Blush", 2400.00),
    ("r.e.m Beauty", "Burgundy Blush", 2300.00),
    ("r.e.m Beauty", "Chestnut Foundation", 5000.00),
    ("r.e.m Beauty", "Tan Foundation", 5000.00),
    ("r.e.m Beauty", "Caramel Foundation", 5000.00),
    ("r.e.m Beauty", "Hazel Foundation", 5000.00),
    ("r.e.m Beauty", "Ollie Foundation", 5000.00),
    ("r.e.m Beauty", "Clear Lipgloss", 1500.00),
    ("r.e.m Beauty", "Pink Tinted Lipgloss", 1300.00),
    ("r.e.m Beauty", "Chocolate Lipgloss", 1500.00),
    ("r.e.m Beauty", "Berry Lipgloss", 2000.00),
    ("r.e.m Beauty", "Choco Mint Lipgloss", 2000.00),
    ("r.e.m Beauty", "Metallic Eyeshadow Palette", 4500.00),
    ("r.e.m Beauty", "Pastel Eyeshadow Palette", 5000.00),
    ("r.e.m Beauty", "Liquid Palette", 5500.00),
    ("r.e.m Beauty", "Loose Glitter Palette", 5700.00),
    ("r.e.m Beauty", "Cream Palette", 5300.00),
    ("rhode", "Black eyeliner", 1700.00),
    ("rhode", "Blue eyeliner", 1900.00),
    ("rhode", "White eyeliner", 2000.00),
    ("rhode", "Pink Chrome eyeliner", 2300.00),
    ("rhode", "Dark Green eyeliner", 2000.00),
    ("rhode", "Pink lipstick", 1500.00),
    ("rhode", "Red Lipstick", 1700.00),
    ("rhode", "Crimson Red Lipstick", 1500.00),
    ("rhode", "Nude Lipstick", 1000.00),
    ("rhode", "Dark Red Lipstick", 1900.00),
    ("rhode", "Pink Blush", 3000.00),
    ("rhode", "Red Blush", 3500.00),
    ("rhode", "Orange Blush", 3100.00),
    ("rhode", "Purple Blush", 3400.00),
    ("rhode", "Burgundy Blush", 3300.00),
    ("rhode", "Chestnut Foundation", 5000.00),
    ("rhode", "Tan Foundation", 5000.00),
    ("rhode", "Caramel Foundation", 5000.00),
    ("rhode", "Hazel Foundation", 5000.00),
    ("rhode", "Ollie Foundation", 5000.00),
    ("rhode", "Clear Lipgloss", 1000.00),
    ("rhode", "Pink Tinted Lipgloss", 1500.00),
    ("rhode", "Chocolate Lipgloss", 1500.00),
    ("rhode", "Berry Lipgloss", 2000.00),
    ("rhode", "Choco Mint Lipgloss", 2000.00),
    ("rhode", "Metallic Eyeshadow Palette", 5500.00),
    ("rhode", "Pastel Eyeshadow Palette", 5000.00),
    ("rhode", "Liquid Palette", 5500.00),
    ("rhode", "Loose Glitter Palette", 5600.00),
    ("rhode", "Cream Palette", 5300.00),
]

for brand, pname, price in products:
    mycursor.execute("""
        INSERT INTO Products (Brand, ProductName, Price)
        VALUES (%s, %s, %s)
    """, (brand, pname, price))

mydb.commit()


# TAKE CONTACT INFO AND INSERT INTO USERS
def signup(contact, email, username, password):
    mycursor.execute("SELECT * FROM Users WHERE ContactNumber = %s", (contact,))
    if mycursor.fetchone():
        messagebox.showerror("Error: Contact number already registered.")
    else:
        mycursor.execute("""
            INSERT INTO Users (ContactNumber, EmailID, Username, Password)
            VALUES (%s, %s, %s, %s)
        """, (contact, email, username, password))
        mydb.commit()


# SEARCH FOR USERNAME
def login(username, password):
    mycursor.execute(
        "SELECT * FROM Users WHERE Username = %s AND Password = %s",
        (username, password)
    )
    user = mycursor.fetchone()
    if user:
        return user[0]  # return UserID
    else:
        return None


def getprice(brand, product):
    try:
        cursor = mydb.cursor(buffered=True)
        query = "SELECT Price FROM Products WHERE Brand = %s AND ProductName = %s"
        cursor.execute(query, (brand, product))
        result = cursor.fetchone()
        cursor.close()
        if result:
            return float(result[0])
        else:
            return None
    except Exception as e:
        return None


# ADD SELECTED PRODUCTS TO TRANSACTIONS
def add(username, transaction_data, quantity, total):
    global mydb, mycursor
    query = "INSERT INTO Transactions (Username, TransactionData, Quantity, Total) VALUES (%s, %s, %s, %s)"
    values = (username, transaction_data, quantity, total)
    mycursor.execute(query, values)
    transaction_id = mycursor.lastrowid
    mydb.commit()
    return transaction_id


def update_qty(qty, total, tid):
    sql = "UPDATE Transactions SET Quantity = %s, Total = %s WHERE TransactionID = %s"
    values = (qty, total, tid)
    try:
        mycursor.execute(sql, values)
        mydb.commit()
    except Exception as e:
        mydb.rollback()


def get_transaction_id():
    try:
        query = "SELECT TransactionID FROM Transactions ORDER BY TransactionID DESC LIMIT 1"
        mycursor.execute(query)
        result = mycursor.fetchone()
        if result:
            tid = result[0]
            return tid
        else:
            return None
    except Exception as e:
        return None


def feedback(uid, feedback_text):
    insert_query = "INSERT INTO feedback (user_id, feedback_text) VALUES (%s, %s)"
    mycursor.execute(insert_query, (uid, feedback_text))
    mydb.commit()
