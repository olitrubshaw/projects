import tkinter as tk
from tkinter import ttk, messagebox
import psycopg2

def get_connection():
    return psycopg2.connect(
        host="localhost",
        port="5432",
        database="royalreads",
        user="postgres",
        password="your_password_here" 
    )

class RoyalReadsApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("RoyalReads Database System")
        self.geometry("1200x700")
        self.configure(bg="#1a1a2e")
        self.resizable(True, True)
        self.sidebar = tk.Frame(self, bg="#16213e", width=260)
        self.sidebar.pack(side=tk.LEFT, fill=tk.Y)
        self.sidebar.pack_propagate(False)

        self.content = tk.Frame(self, bg="#0f3460")
        self.content.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self._build_sidebar()
        self.current_frame = None
        self.show_frame(HomeFrame)

    def _build_sidebar(self):
        # Logo / Title
        tk.Label(self.sidebar, text="📚 RoyalReads", font=("Georgia", 16, "bold"),
                 bg="#16213e", fg="#e94560", pady=20).pack(fill=tk.X)

        tk.Label(self.sidebar, text="Database System", font=("Georgia", 9),
                 bg="#16213e", fg="#a8a8b3").pack()

        ttk.Separator(self.sidebar, orient="horizontal").pack(fill=tk.X, pady=10)

        # Navigation buttons — one per transaction + scenarios
        transactions = [
            ("🏠  Home",                    HomeFrame),
            ("1.  Insert Category",         T1Frame),
            ("2.  Delete Category",         T2Frame),
            ("3.  Book Summary Report",     T3Frame),
            ("4.  Books by Publisher",      T4Frame),
            ("5.  Order History (Book)",    T5Frame),
            ("6.  Sales Rep Performance",   T6Frame),
            ("7.  Category Discount",       T7Frame),
            ("8.  Add Order Line",          T8Frame),
            ("9.  Dispatch Order",          T9Frame),
            ("10. Insert on Dispatched",    T10Frame),
            ("11. View ShopOrders",         T11Frame),
            ("12. View Categories",         T12Frame),
        ]

        for label, frame_class in transactions:
            btn = tk.Button(
                self.sidebar, text=label, anchor="w",
                font=("Courier", 10), bg="#16213e", fg="#e0e0e0",
                activebackground="#e94560", activeforeground="white",
                relief=tk.FLAT, padx=15, pady=6, cursor="hand2",
                command=lambda fc=frame_class: self.show_frame(fc)
            )
            btn.pack(fill=tk.X)

    def show_frame(self, frame_class):
        if self.current_frame:
            self.current_frame.destroy()
        self.current_frame = frame_class(self.content)
        self.current_frame.pack(fill=tk.BOTH, expand=True)

def make_title(parent, text):
    tk.Label(parent, text=text, font=("Georgia", 16, "bold"),
             bg="#0f3460", fg="#e94560", pady=15).pack(anchor="w", padx=20)

def make_label(parent, text):
    tk.Label(parent, text=text, font=("Courier", 10),
             bg="#0f3460", fg="#e0e0e0").pack(anchor="w", padx=20, pady=2)

def make_entry(parent):
    e = tk.Entry(parent, font=("Courier", 11), bg="#16213e", fg="white",
                 insertbackground="white", relief=tk.FLAT, bd=5)
    e.pack(anchor="w", padx=20, pady=2, ipadx=5, ipady=4)
    return e

def make_button(parent, text, command):
    tk.Button(parent, text=text, command=command,
              font=("Courier", 11, "bold"), bg="#e94560", fg="white",
              activebackground="#c73652", relief=tk.FLAT,
              padx=15, pady=6, cursor="hand2").pack(anchor="w", padx=20, pady=10)

def make_result_label(parent):
    lbl = tk.Label(parent, text="", font=("Courier", 10),
                   bg="#0f3460", fg="#00ff88", wraplength=800, justify="left")
    lbl.pack(anchor="w", padx=20, pady=5)
    return lbl

def make_table(parent, columns):
    """Creates a scrollable Treeview table."""
    frame = tk.Frame(parent, bg="#0f3460")
    frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview", background="#16213e", foreground="white",
                    fieldbackground="#16213e", font=("Courier", 9), rowheight=22)
    style.configure("Treeview.Heading", background="#e94560", foreground="white",
                    font=("Courier", 10, "bold"))

    scroll_y = ttk.Scrollbar(frame, orient=tk.VERTICAL)
    scroll_x = ttk.Scrollbar(frame, orient=tk.HORIZONTAL)

    tree = ttk.Treeview(frame, columns=columns, show="headings",
                        yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)

    scroll_y.config(command=tree.yview)
    scroll_x.config(command=tree.xview)
    scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
    scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
    tree.pack(fill=tk.BOTH, expand=True)

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=130, anchor="center")

    return tree

def populate_table(tree, rows):
    """Clears and repopulates a Treeview table."""
    for item in tree.get_children():
        tree.delete(item)
    for row in rows:
        tree.insert("", tk.END, values=row)


class HomeFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#0f3460")
        tk.Label(self, text="📚 RoyalReads", font=("Georgia", 36, "bold"),
                 bg="#0f3460", fg="#e94560").pack(pady=60)
        tk.Label(self, text="Book Wholesaler Database System",
                 font=("Georgia", 14), bg="#0f3460", fg="#a8a8b3").pack()
        tk.Label(self, text="Select a transaction from the sidebar to begin.",
                 font=("Courier", 11), bg="#0f3460", fg="#e0e0e0").pack(pady=20)


class T1Frame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#0f3460")
        make_title(self, "Transaction 1 — Insert Category")

        make_label(self, "Category ID:")
        self.cat_id = make_entry(self)

        make_label(self, "Name:")
        self.name = make_entry(self)

        make_label(self, "Category Type (Fiction / Non-fiction):")
        self.cat_type = make_entry(self)

        make_button(self, "Insert Category", self.run)
        self.result = make_result_label(self)

    def run(self):
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO Category (CategoryID, Name, CategoryType) VALUES (%s, %s, %s)",
                (self.cat_id.get(), self.name.get(), self.cat_type.get())
            )
            conn.commit()
            self.result.config(text=f"Category '{self.name.get()}' inserted successfully.", fg="#00ff88")
        except Exception as e:
            self.result.config(text=f"Error: {e}", fg="#e94560")
        finally:
            conn.close()

class T2Frame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#0f3460")
        make_title(self, "Transaction 2 — Delete Category")

        make_label(self, "Category ID to delete:")
        self.cat_id = make_entry(self)

        make_button(self, "Delete Category", self.run)
        self.result = make_result_label(self)

    def run(self):
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("DELETE FROM Category WHERE CategoryID = %s", (self.cat_id.get(),))
            rows = cur.rowcount
            conn.commit()
            if rows == 0:
                self.result.config(text="No category found with that ID.", fg="#ffaa00")
            else:
                self.result.config(text=f"Category {self.cat_id.get()} deleted successfully.", fg="#00ff88")
        except Exception as e:
            self.result.config(text=f"Error: {e}", fg="#e94560")
        finally:
            conn.close()


class T3Frame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#0f3460")
        make_title(self, "Transaction 3 — Book Summary Report")
        make_button(self, "Generate Report", self.run)
        self.summary_label = make_result_label(self)

        cols = ("CategoryID", "Category", "Type", "Total Titles", "Avg Price")
        self.tree = make_table(self, cols)

    def run(self):
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("""
                SELECT c.CategoryID, c.Name, c.CategoryType,
                       COUNT(b.BookID) AS TotalTitles,
                       TO_CHAR(AVG(b.Price), 'FM£999,990.00') AS AveragePrice
                FROM Category c LEFT JOIN Book b ON b.CategoryID = c.CategoryID
                GROUP BY c.CategoryID, c.Name, c.CategoryType
                ORDER BY c.Name
            """)
            rows = cur.fetchall()
            populate_table(self.tree, rows)

            # Summary line
            cur.execute("""
                SELECT COUNT(BookID), TO_CHAR(AVG(Price), 'FM£999,990.00') FROM Book
            """)
            total = cur.fetchone()
            self.summary_label.config(
                text=f"📊 Total: {total[0]} titles | Overall Avg Price: {total[1]}", fg="#00ff88")
        except Exception as e:
            self.summary_label.config(text=f"Error: {e}", fg="#e94560")
        finally:
            conn.close()

class T4Frame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#0f3460")
        make_title(self, "Transaction 4 — Books Ordered by Publisher")

        make_label(self, "Publisher Name:")
        self.publisher = make_entry(self)

        make_button(self, "Generate Report", self.run)
        self.result = make_result_label(self)

        cols = ("Year", "Month", "BookID", "Title", "Total Orders", "Total Qty", "Selling Value", "Retail Value")
        self.tree = make_table(self, cols)

    def run(self):
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("""
                SELECT EXTRACT(YEAR FROM so.OrderDate) AS OrderYear,
                       EXTRACT(MONTH FROM so.OrderDate) AS OrderMonth,
                       b.BookID, b.Title,
                       COUNT(DISTINCT so.ShopOrderID) AS TotalOrders,
                       SUM(ol.Quantity) AS TotalQuantity,
                       TO_CHAR(SUM(ol.Quantity * ol.UnitSellingPrice), 'FM£9,999,990.00') AS TotalSellingValue,
                       TO_CHAR(SUM(ol.Quantity * b.Price), 'FM£9,999,990.00') AS TotalRetailValue
                FROM Orderline ol
                JOIN ShopOrder so ON so.ShopOrderID = ol.ShopOrderID
                JOIN Book b ON b.BookID = ol.BookID
                JOIN Publisher p ON p.PublisherID = b.PublisherID
                WHERE UPPER(p.Name) = UPPER(%s)
                GROUP BY EXTRACT(YEAR FROM so.OrderDate), EXTRACT(MONTH FROM so.OrderDate), b.BookID, b.Title
                ORDER BY OrderYear, OrderMonth, b.BookID
            """, (self.publisher.get(),))
            rows = cur.fetchall()
            populate_table(self.tree, rows)
            if not rows:
                self.result.config(text="No results found for that publisher.", fg="#ffaa00")
            else:
                self.result.config(text=f"{len(rows)} rows returned.", fg="#00ff88")
        except Exception as e:
            self.result.config(text=f"Error: {e}", fg="#e94560")
        finally:
            conn.close()

class T5Frame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#0f3460")
        make_title(self, "Transaction 5 — Order History for a Book")

        make_label(self, "Book ID:")
        self.book_id = make_entry(self)

        make_button(self, "Get Order History", self.run)
        self.summary_label = make_result_label(self)

        cols = ("Order Date", "Title", "List Price", "Unit Selling Price", "Quantity", "Order Value", "Shop")
        self.tree = make_table(self, cols)

    def run(self):
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("""
                SELECT so.OrderDate, b.Title,
                       TO_CHAR(b.Price, 'FM£9,999,990.00') AS ListPrice,
                       TO_CHAR(ol.UnitSellingPrice, 'FM£9,999,990.00') AS UnitSellingPrice,
                       ol.Quantity,
                       TO_CHAR(ol.Quantity * ol.UnitSellingPrice, 'FM£9,999,990.00') AS OrderValue,
                       sh.Name AS ShopName
                FROM Orderline ol
                JOIN ShopOrder so ON so.ShopOrderID = ol.ShopOrderID
                JOIN Book b ON b.BookID = ol.BookID
                JOIN Shop sh ON sh.ShopID = so.ShopID
                WHERE b.BookID = %s
                ORDER BY so.OrderDate
            """, (self.book_id.get(),))
            rows = cur.fetchall()
            populate_table(self.tree, rows)

            # Summary line
            cur.execute("""
                SELECT SUM(ol.Quantity),
                       TO_CHAR(SUM(ol.Quantity * ol.UnitSellingPrice), 'FM£9,999,990.00')
                FROM Orderline ol WHERE ol.BookID = %s
            """, (self.book_id.get(),))
            total = cur.fetchone()
            self.summary_label.config(
                text=f"📊 Total Copies: {total[0]} | Total Selling Value: {total[1]}", fg="#00ff88")
        except Exception as e:
            self.summary_label.config(text=f"Error: {e}", fg="#e94560")
        finally:
            conn.close()

class T6Frame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#0f3460")
        make_title(self, "Transaction 6 — Sales Rep Performance")

        make_label(self, "Start Date (YYYY-MM-DD):")
        self.start = make_entry(self)

        make_label(self, "End Date (YYYY-MM-DD):")
        self.end = make_entry(self)

        make_button(self, "Generate Report", self.run)
        self.result = make_result_label(self)

        cols = ("Rep ID", "Name", "Total Orders", "Units Sold", "Total Order Value")
        self.tree = make_table(self, cols)

    def run(self):
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("""
                SELECT sr.SalesRepID, sr.Name,
                       COUNT(DISTINCT so.ShopOrderID) AS TotalOrders,
                       COALESCE(SUM(ol.Quantity), 0) AS TotalUnitsSold,
                       TO_CHAR(COALESCE(SUM(ol.Quantity * ol.UnitSellingPrice), 0), 'FM£9,999,990.00') AS TotalOrderValue
                FROM SalesRep sr
                LEFT JOIN ShopOrder so ON so.SalesRepID = sr.SalesRepID
                    AND so.OrderDate BETWEEN %s AND %s
                LEFT JOIN Orderline ol ON ol.ShopOrderID = so.ShopOrderID
                GROUP BY sr.SalesRepID, sr.Name
                ORDER BY COALESCE(SUM(ol.Quantity * ol.UnitSellingPrice), 0) DESC
            """, (self.start.get(), self.end.get()))
            rows = cur.fetchall()
            populate_table(self.tree, rows)
            self.result.config(text=f"{len(rows)} sales reps shown.", fg="#00ff88")
        except Exception as e:
            self.result.config(text=f"Error: {e}", fg="#e94560")
        finally:
            conn.close()

class T7Frame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#0f3460")
        make_title(self, "Transaction 7 — Category Discount Preview")

        make_label(self, "Category ID:")
        self.cat_id = make_entry(self)

        make_label(self, "Discount % (e.g. 10):")
        self.discount = make_entry(self)

        make_button(self, "Apply Discount Preview", self.run)
        self.result = make_result_label(self)

        cols = ("BookID", "Title", "Category", "Publisher", "Standard Price", "Discount %", "Discounted Price")
        self.tree = make_table(self, cols)

    def run(self):
        try:
            discount = float(self.discount.get())
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("""
                SELECT b.BookID, b.Title, c.Name AS Category, p.Name AS Publisher,
                       TO_CHAR(b.Price, 'FM£9,999,990.00') AS StandardPrice,
                       %s AS Discount,
                       TO_CHAR(b.Price * (1 - %s / 100.0), 'FM£9,999,990.00') AS DiscountedPrice
                FROM Book b
                JOIN Category c ON c.CategoryID = b.CategoryID
                JOIN Publisher p ON p.PublisherID = b.PublisherID
                WHERE b.CategoryID = %s
                ORDER BY b.Title
            """, (discount, discount, self.cat_id.get()))
            rows = cur.fetchall()
            populate_table(self.tree, rows)
            if not rows:
                self.result.config(text="No books found for that category.", fg="#ffaa00")
            else:
                self.result.config(text=f"{len(rows)} books shown with {discount}% discount applied.", fg="#00ff88")
        except Exception as e:
            self.result.config(text=f"Error: {e}", fg="#e94560")
        finally:
            conn.close()

class T8Frame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#0f3460")
        make_title(self, "Transaction 8 — Add Order Line to Open Order")

        make_label(self, "Order ID:")
        self.order_id = make_entry(self)

        make_label(self, "Book ID:")
        self.book_id = make_entry(self)

        make_label(self, "Quantity:")
        self.quantity = make_entry(self)

        make_label(self, "Unit Selling Price:")
        self.price = make_entry(self)

        make_button(self, "Add Order Line", self.run)
        self.result = make_result_label(self)

    def run(self):
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO Orderline (ShopOrderID, BookID, Quantity, UnitSellingPrice)
                VALUES (%s, %s, %s, %s)
            """, (self.order_id.get(), self.book_id.get(), self.quantity.get(), self.price.get()))
            conn.commit()
            self.result.config(text="Order line added successfully.", fg="#00ff88")
        except Exception as e:
            self.result.config(text=f"Error: {e}", fg="#e94560")
        finally:
            conn.close()

class T9Frame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#0f3460")
        make_title(self, "Transaction 9 — Set Order to Dispatched")

        make_label(self, "Order ID:")
        self.order_id = make_entry(self)

        make_button(self, "Dispatch Order", self.run)
        self.result = make_result_label(self)

    def run(self):
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("""
                UPDATE ShopOrder SET Status = 'Dispatched' WHERE ShopOrderID = %s
            """, (self.order_id.get(),))
            rows = cur.rowcount
            conn.commit()
            if rows == 0:
                self.result.config(text="No order found with that ID.", fg="#ffaa00")
            else:
                self.result.config(text=f"Order {self.order_id.get()} dispatched successfully.", fg="#00ff88")
        except Exception as e:
            self.result.config(text=f"Error: {e}", fg="#e94560")
        finally:
            conn.close()

class T10Frame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#0f3460")
        make_title(self, "Transaction 10 — Attempt Insert on Dispatched Order")

        make_label(self, "Order ID:")
        self.order_id = make_entry(self)

        make_label(self, "Book ID:")
        self.book_id = make_entry(self)

        make_label(self, "Quantity:")
        self.quantity = make_entry(self)

        make_label(self, "Unit Selling Price:")
        self.price = make_entry(self)

        make_button(self, "Attempt Insert", self.run)
        self.result = make_result_label(self)

    def run(self):
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO Orderline (ShopOrderID, BookID, Quantity, UnitSellingPrice)
                VALUES (%s, %s, %s, %s)
            """, (self.order_id.get(), self.book_id.get(), self.quantity.get(), self.price.get()))
            conn.commit()
            self.result.config(text="Order line added.", fg="#00ff88")
        except Exception as e:
            self.result.config(text=f"Blocked as expected — {e}", fg="#e94560")
        finally:
            conn.close()

class T11Frame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#0f3460")
        make_title(self, "Transaction 11 — View All Shop Orders")
        make_button(self, "Load Orders", self.run)
        self.result = make_result_label(self)

        cols = ("Order ID", "Date", "Shop", "Sales Rep", "Status")
        self.tree = make_table(self, cols)

    def run(self):
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("""
                SELECT so.ShopOrderID, so.OrderDate, sh.Name AS ShopName,
                       sr.Name AS SalesRepName, so.Status
                FROM ShopOrder so
                JOIN Shop sh ON sh.ShopID = so.ShopID
                JOIN SalesRep sr ON sr.SalesRepID = so.SalesRepID
                ORDER BY so.ShopOrderID
            """)
            rows = cur.fetchall()
            populate_table(self.tree, rows)
            self.result.config(text=f" {len(rows)} orders loaded.", fg="#00ff88")
        except Exception as e:
            self.result.config(text=f"Error: {e}", fg="#e94560")
        finally:
            conn.close()

class T12Frame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#0f3460")
        make_title(self, "Transaction 12 — View All Categories")
        make_button(self, "Load Categories", self.run)
        self.result = make_result_label(self)

        cols = ("Category ID", "Name", "Type")
        self.tree = make_table(self, cols)

    def run(self):
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("SELECT CategoryID, Name, CategoryType FROM Category ORDER BY CategoryID")
            rows = cur.fetchall()
            populate_table(self.tree, rows)
            self.result.config(text=f"{len(rows)} categories loaded.", fg="#00ff88")
        except Exception as e:
            self.result.config(text=f"Error: {e}", fg="#e94560")
        finally:
            conn.close()


if __name__ == "__main__":
    app = RoyalReadsApp()
    app.mainloop()