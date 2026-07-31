
# PROJECT: LUCIFER BANKING MANAGEMENT SYSTEM
# ARCHITECTURE: Single-file Pure Python/Tkinter Desktop Application
# DESCRIPTION: Professional Role-Based Banking UI (Admin & User Dashboards)
# DATA STORE: In-Memory Python Data Structures (No SQL/External DB required)


import tkinter as tk
from tkinter import ttk, messagebox
import time
from datetime import datetime

# SECTION 1: IN-MEMORY DATA STORE (NO DB REQUIRED)


MOCK_ACCOUNTS = {
    "1001": {
        "name": "Lucifer Morningstar",
        "email": "lucifer@lucifer.com",
        "pin": "1234",
        "balance": 250000.00,
        "role": "Admin",
        "created": "2026-01-01",
        "status": "Active"
    },
    "1002": {
        "name": "Chloe Decker",
        "email": "chloe@lucifer.com",
        "pin": "1234",
        "balance": 15420.50,
        "role": "User",
        "created": "2026-02-10",
        "status": "Active"
    },
    "1003": {
        "name": "Amenadiel Firstborn",
        "email": "amenadiel@lucifer.com",
        "pin": "1234",
        "balance": 89000.00,
        "role": "User",
        "created": "2026-03-15",
        "status": "Active"
    },
    "1004": {
        "name": "Mazikeen Lilim",
        "email": "mazikeen@lucifer.com",
        "pin": "1234",
        "balance": 42000.75,
        "role": "User",
        "created": "2026-04-01",
        "status": "Active"
    }
}

MOCK_TRANSACTIONS = [
    {"id": "TXN9012", "acn": "1002", "type": "Deposit", "amount": 2500.0, "date": "2026-07-20 10:15", "status": "Success"},
    {"id": "TXN9011", "acn": "1003", "type": "Withdraw", "amount": 1000.0, "date": "2026-07-19 14:30", "status": "Success"},
    {"id": "TXN9010", "acn": "1002", "type": "Transfer", "amount": 500.0, "date": "2026-07-18 16:45", "status": "Success"},
    {"id": "TXN9009", "acn": "1004", "type": "Deposit", "amount": 10000.0, "date": "2026-07-15 09:00", "status": "Success"},
]

CURRENT_USER = None

# ==============================================================================
# SECTION 2: APPLICATION CONTROLLER & COLOR PALETTE
# ==============================================================================

class Theme:
    BG_DARK = "#111827"          # Outer main background
    CARD_BG = "#1F2937"          # Inner card background
    SIDEBAR_BG = "#0F172A"       # Navigation sidebar
    TEXT_MAIN = "#F9FAFB"        # Primary white text
    TEXT_MUTED = "#9CA3AF"       # Muted gray text
    ACCENT_CYAN = "#06B6D4"      # Primary brand highlight
    ACCENT_HOVER = "#0891B2"     # Hover effect
    DANGER = "#EF4444"           # Red buttons/alerts
    SUCCESS = "#10B981"          # Green indicators
    FONT_FAMILY = "Segoe UI"     # Clean modern font

class LuciferApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("LUCIFER - Banking Management System")
        self.geometry("1280x720")
        self.minsize(1024, 600)
        self.configure(bg=Theme.BG_DARK)
        
        # Windows Maximize on Start
        try:
            self.state("zoomed")
        except tk.TclError:
            pass

        self._apply_styles()
        self.show_login_screen()

    def _apply_styles(self):
        """Configure modern ttk styles for tables and widgets."""
        style = ttk.Style(self)
        style.theme_use("clam")
        
        # Configure Treeview (Data Tables)
        style.configure("Treeview",
                        background=Theme.CARD_BG,
                        foreground=Theme.TEXT_MAIN,
                        fieldbackground=Theme.CARD_BG,
                        rowheight=30,
                        font=(Theme.FONT_FAMILY, 10))
        style.configure("Treeview.Heading",
                        background=Theme.SIDEBAR_BG,
                        foreground=Theme.ACCENT_CYAN,
                        font=(Theme.FONT_FAMILY, 11, "bold"))
        style.map("Treeview", background=[("selected", Theme.ACCENT_CYAN)])

        # Configure Combobox
        style.configure("TCombobox",
                        fieldbackground=Theme.CARD_BG,
                        background=Theme.CARD_BG,
                        foreground=Theme.TEXT_MAIN)

    def clear_screen(self):
        """Destroy all current child widgets to render a new frame cleanly."""
        for widget in self.winfo_children():
            widget.destroy()

    def show_login_screen(self):
        self.clear_screen()
        LoginScreen(self)

    def show_admin_dashboard(self):
        self.clear_screen()
        AdminDashboard(self)

    def show_user_dashboard(self):
        self.clear_screen()
        UserDashboard(self)

# ==============================================================================
# SECTION 3: REUSABLE UI COMPONENTS
# ==============================================================================

class HoverButton(tk.Button):
    """Custom Tkinter Button with smooth visual hover feedback."""
    def __init__(self, master=None, bg_color=Theme.ACCENT_CYAN, hover_color=Theme.ACCENT_HOVER, fg_color="#FFFFFF", **kw):
        super().__init__(master, **kw)
        self.default_bg = bg_color
        self.hover_bg = hover_color
        self.configure(
            bg=self.default_bg,
            fg=fg_color,
            activebackground=self.hover_bg,
            activeforeground=fg_color,
            bd=0,
            relief="flat",
            cursor="hand2"
        )
        self.bind("<Enter>", lambda e: self.configure(bg=self.hover_bg))
        self.bind("<Leave>", lambda e: self.configure(bg=self.default_bg))

# ==============================================================================
# SECTION 4: LOGIN & FORGOT PASSWORD SCREENS
# ==============================================================================

class LoginScreen(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg=Theme.BG_DARK)
        self.parent = parent
        self.pack(fill="both", expand=True)
        self._build_ui()

    def _build_ui(self):
        # Header Banner
        header = tk.Frame(self, bg=Theme.BG_DARK)
        header.pack(fill="x", pady=(30, 10))

        title = tk.Label(header, text="LUCIFER", font=(Theme.FONT_FAMILY, 36, "bold"), fg=Theme.ACCENT_CYAN, bg=Theme.BG_DARK)
        title.pack()
        subtitle = tk.Label(header, text="Banking Management System", font=(Theme.FONT_FAMILY, 14), fg=Theme.TEXT_MUTED, bg=Theme.BG_DARK)
        subtitle.pack()

        # Center Login Card
        card = tk.Frame(self, bg=Theme.CARD_BG, padx=40, pady=30, highlightbackground=Theme.ACCENT_CYAN, highlightthickness=1)
        card.place(relx=0.5, rely=0.52, anchor="center", width=420)

        card_title = tk.Label(card, text="Account Login", font=(Theme.FONT_FAMILY, 18, "bold"), fg=Theme.TEXT_MAIN, bg=Theme.CARD_BG)
        card_title.pack(pady=(0, 20))

        # A/C Number Field
        tk.Label(card, text="Account Number / Username", font=(Theme.FONT_FAMILY, 10, "bold"), fg=Theme.TEXT_MUTED, bg=Theme.CARD_BG, anchor="w").pack(fill="x")
        self.acn_entry = tk.Entry(card, font=(Theme.FONT_FAMILY, 11), bg="#111827", fg=Theme.TEXT_MAIN, insertbackground="white", bd=1, relief="solid")
        self.acn_entry.pack(fill="x", pady=(5, 15), ipady=6)
        self.acn_entry.focus()

        # Password Field
        tk.Label(card, text="Password / PIN", font=(Theme.FONT_FAMILY, 10, "bold"), fg=Theme.TEXT_MUTED, bg=Theme.CARD_BG, anchor="w").pack(fill="x")
        self.pass_entry = tk.Entry(card, font=(Theme.FONT_FAMILY, 11), show="•", bg="#111827", fg=Theme.TEXT_MAIN, insertbackground="white", bd=1, relief="solid")
        self.pass_entry.pack(fill="x", pady=(5, 15), ipady=6)

        # Role Selector
        tk.Label(card, text="Login Role", font=(Theme.FONT_FAMILY, 10, "bold"), fg=Theme.TEXT_MUTED, bg=Theme.CARD_BG, anchor="w").pack(fill="x")
        self.role_var = tk.StringVar(value="User")
        role_combo = ttk.Combobox(card, textvariable=self.role_var, values=("User", "Admin"), state="readonly", font=(Theme.FONT_FAMILY, 10))
        role_combo.pack(fill="x", pady=(5, 20), ipady=4)

        # Buttons
        HoverButton(card, text="Login", font=(Theme.FONT_FAMILY, 11, "bold"), command=self.handle_login).pack(fill="x", pady=(0, 10), ipady=6)
        
        btn_frame = tk.Frame(card, bg=Theme.CARD_BG)
        btn_frame.pack(fill="x")

        tk.Button(btn_frame, text="Forgot Password?", font=(Theme.FONT_FAMILY, 9, "underline"), fg=Theme.ACCENT_CYAN, bg=Theme.CARD_BG, activebackground=Theme.CARD_BG, activeforeground=Theme.ACCENT_HOVER, bd=0, cursor="hand2", command=self.show_forgot_screen).pack(side="left")
        tk.Button(btn_frame, text="Clear Fields", font=(Theme.FONT_FAMILY, 9), fg=Theme.TEXT_MUTED, bg=Theme.CARD_BG, activebackground=Theme.CARD_BG, activeforeground=Theme.TEXT_MAIN, bd=0, cursor="hand2", command=self.clear_fields).pack(side="right")

        # Live Clock / Footer
        self.time_lbl = tk.Label(self, font=(Theme.FONT_FAMILY, 11), fg=Theme.TEXT_MUTED, bg=Theme.BG_DARK)
        self.time_lbl.pack(side="bottom", pady=15)
        self.update_clock()

    def update_clock(self):
        if self.winfo_exists():
            now = datetime.now().strftime("%A, %d-%b-%Y  ⏰ %I:%M:%S %p")
            self.time_lbl.config(text=f"LUCIFER System Time: {now}")
            self.after(1000, self.update_clock)

    def clear_fields(self):
        self.acn_entry.delete(0, tk.END)
        self.pass_entry.delete(0, tk.END)

    def handle_login(self):
        global CURRENT_USER
        acn = self.acn_entry.get().strip()
        pwd = self.pass_entry.get().strip()
        role = self.role_var.get()

        if not acn or not pwd:
            messagebox.showerror("Error", "Please fill in all credentials.")
            return

        user = MOCK_ACCOUNTS.get(acn)

        if user and user["pin"] == pwd and user["role"] == role:
            CURRENT_USER = {"acn": acn, **user}
            messagebox.showinfo("Success", f"Welcome to LUCIFER, {user['name']}!")
            if role == "Admin":
                self.parent.show_admin_dashboard()
            else:
                self.parent.show_user_dashboard()
        else:
            messagebox.showerror("Login Failed", "Invalid Account Number, Password, or Role selection.")

    def show_forgot_screen(self):
        ForgotWindow(self.parent)

class ForgotWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("LUCIFER - Password Reset")
        self.geometry("400x350")
        self.configure(bg=Theme.BG_DARK)
        self.resizable(False, False)
        self.grab_set()

        tk.Label(self, text="Password Recovery", font=(Theme.FONT_FAMILY, 16, "bold"), fg=Theme.ACCENT_CYAN, bg=Theme.BG_DARK).pack(pady=20)
        
        frame = tk.Frame(self, bg=Theme.CARD_BG, padx=25, pady=20)
        frame.pack(fill="both", expand=True, padx=20, pady=(0, 20))

        tk.Label(frame, text="Registered E-mail:", font=(Theme.FONT_FAMILY, 10), fg=Theme.TEXT_MUTED, bg=Theme.CARD_BG).pack(anchor="w")
        self.email_entry = tk.Entry(frame, font=(Theme.FONT_FAMILY, 10), bg="#111827", fg=Theme.TEXT_MAIN, bd=1)
        self.email_entry.pack(fill="x", pady=(2, 10), ipady=4)

        tk.Label(frame, text="Account Number:", font=(Theme.FONT_FAMILY, 10), fg=Theme.TEXT_MUTED, bg=Theme.CARD_BG).pack(anchor="w")
        self.acn_entry = tk.Entry(frame, font=(Theme.FONT_FAMILY, 10), bg="#111827", fg=Theme.TEXT_MAIN, bd=1)
        self.acn_entry.pack(fill="x", pady=(2, 15), ipady=4)

        HoverButton(frame, text="Send Security OTP", font=(Theme.FONT_FAMILY, 10, "bold"), command=self.send_otp).pack(fill="x", pady=5, ipady=4)
        HoverButton(frame, text="Close Window", bg_color=Theme.CARD_BG, hover_color="#374151", command=self.destroy).pack(fill="x", ipady=4)

    def send_otp(self):
        email = self.email_entry.get().strip()
        acn = self.acn_entry.get().strip()
        
        if not email or not acn:
            messagebox.showerror("Error", "Please provide both Email and Account Number.", parent=self)
            return
        
        if acn in MOCK_ACCOUNTS and MOCK_ACCOUNTS[acn]["email"] == email:
            messagebox.showinfo("OTP Sent", "A temporary password reset link has been dispatched to your email.", parent=self)
            self.destroy()
        else:
            messagebox.showerror("Verification Failed", "Account details do not match our system records.", parent=self)

# ==============================================================================
# SECTION 5: BASE DASHBOARD FRAME (HEADER & NAVIGATION LOGIC)
# ==============================================================================

class BaseDashboard(tk.Frame):
    """Parent dashboard layout providing unified Header and Dynamic Sidebar."""
    def __init__(self, parent, role_title):
        super().__init__(parent, bg=Theme.BG_DARK)
        self.parent = parent
        self.role_title = role_title
        self.pack(fill="both", expand=True)

        self._create_header()
        
        # Container below header
        self.body_frame = tk.Frame(self, bg=Theme.BG_DARK)
        self.body_frame.pack(fill="both", expand=True)

        self._create_sidebar()
        
        # Main Dynamic Working Area
        self.content_area = tk.Frame(self.body_frame, bg=Theme.BG_DARK, padx=20, pady=20)
        self.content_area.pack(side="right", fill="both", expand=True)

    def _create_header(self):
        header = tk.Frame(self, bg=Theme.SIDEBAR_BG, height=60, padx=20)
        header.pack(fill="x", side="top")

        # Brand Title
        brand_lbl = tk.Label(header, text="LUCIFER", font=(Theme.FONT_FAMILY, 18, "bold"), fg=Theme.ACCENT_CYAN, bg=Theme.SIDEBAR_BG)
        brand_lbl.pack(side="left")

        sub_lbl = tk.Label(header, text=f"| {self.role_title}", font=(Theme.FONT_FAMILY, 12), fg=Theme.TEXT_MUTED, bg=Theme.SIDEBAR_BG)
        sub_lbl.pack(side="left", padx=10)

        # Logout Top-Right Button
        HoverButton(header, text="Logout", bg_color=Theme.DANGER, hover_color="#DC2626", font=(Theme.FONT_FAMILY, 9, "bold"), command=self.logout, width=10).pack(side="right", padx=(10, 0), pady=12)

        # User Info & Live Clock
        user_name = CURRENT_USER["name"] if CURRENT_USER else "User"
        self.header_time_lbl = tk.Label(header, font=(Theme.FONT_FAMILY, 10), fg=Theme.TEXT_MAIN, bg=Theme.SIDEBAR_BG)
        self.header_time_lbl.pack(side="right", padx=15)
        
        user_lbl = tk.Label(header, text=f"👤 {user_name}", font=(Theme.FONT_FAMILY, 10, "bold"), fg=Theme.ACCENT_CYAN, bg=Theme.SIDEBAR_BG)
        user_lbl.pack(side="right", padx=10)

        self.update_header_clock()

    def update_header_clock(self):
        if self.winfo_exists():
            now = datetime.now().strftime("%A, %d-%b-%Y %r")
            self.header_time_lbl.config(text=f"⏰ {now}")
            self.after(1000, self.update_header_clock)

    def _create_sidebar(self):
        self.sidebar = tk.Frame(self.body_frame, bg=Theme.SIDEBAR_BG, width=220)
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)

        tk.Label(self.sidebar, text="NAVIGATION", font=(Theme.FONT_FAMILY, 9, "bold"), fg=Theme.TEXT_MUTED, bg=Theme.SIDEBAR_BG, anchor="w", padx=15).pack(fill="x", pady=(20, 10))

    def add_sidebar_btn(self, text, command):
        btn = HoverButton(
            self.sidebar,
            text=f"  {text}",
            anchor="w",
            font=(Theme.FONT_FAMILY, 10, "bold"),
            bg_color=Theme.SIDEBAR_BG,
            hover_color=Theme.CARD_BG,
            fg_color=Theme.TEXT_MAIN,
            command=command
        )
        btn.pack(fill="x", ipady=10)

    def clear_content(self):
        for widget in self.content_area.winfo_children():
            widget.destroy()

    def logout(self):
        global CURRENT_USER
        if messagebox.askyesno("Logout", "Are you sure you want to return to the Login screen?"):
            CURRENT_USER = None
            self.parent.show_login_screen()

# ==============================================================================
# SECTION 6: ADMIN DASHBOARD MODULE
# ==============================================================================

class AdminDashboard(BaseDashboard):
    def __init__(self, parent):
        super().__init__(parent, role_title="ADMINISTRATOR PANEL")
        self._setup_navigation()
        self.show_dashboard_home()

    def _setup_navigation(self):
        self.add_sidebar_btn("📊 Dashboard", self.show_dashboard_home)
        self.add_sidebar_btn("👥 Customer Management", self.show_customers)
        self.add_sidebar_btn("💳 Account Management", self.show_accounts)
        self.add_sidebar_btn("🔄 Transactions Audit", self.show_transactions)
        self.add_sidebar_btn("📈 Analytical Reports", self.show_reports)
        self.add_sidebar_btn("⚙️ System Settings", self.show_settings)
        self.add_sidebar_btn("🔑 Change Password", self.show_change_password)
        self.add_sidebar_btn("🚪 Logout", self.logout)

    def show_dashboard_home(self):
        self.clear_content()

        # Title
        tk.Label(self.content_area, text="Executive Overview", font=(Theme.FONT_FAMILY, 20, "bold"), fg=Theme.TEXT_MAIN, bg=Theme.BG_DARK).pack(anchor="w", pady=(0, 20))

        # Metrics Row
        cards_frame = tk.Frame(self.content_area, bg=Theme.BG_DARK)
        cards_frame.pack(fill="x", pady=(0, 20))

        total_cust = len(MOCK_ACCOUNTS)
        total_bal = sum(acc["balance"] for acc in MOCK_ACCOUNTS.values())
        total_txns = len(MOCK_TRANSACTIONS)

        self._create_metric_card(cards_frame, "Total Customers", str(total_cust), Theme.ACCENT_CYAN, 0)
        self._create_metric_card(cards_frame, "Total Vault Assets", f"${total_bal:,.2f}", Theme.SUCCESS, 1)
        self._create_metric_card(cards_frame, "Processed Txns", str(total_txns), "#F59E0B", 2)

        # Recent Activity Table
        tk.Label(self.content_area, text="Recent System Transactions", font=(Theme.FONT_FAMILY, 14, "bold"), fg=Theme.TEXT_MAIN, bg=Theme.BG_DARK).pack(anchor="w", pady=(10, 10))
        
        table_frame = tk.Frame(self.content_area, bg=Theme.CARD_BG)
        table_frame.pack(fill="both", expand=True)

        columns = ("ID", "Account", "Type", "Amount", "Date", "Status")
        tree = ttk.Treeview(table_frame, columns=columns, show="headings", selectmode="browse")
        
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor="center", width=120)

        for txn in MOCK_TRANSACTIONS:
            tree.insert("", "end", values=(txn["id"], txn["acn"], txn["type"], f"${txn['amount']:,.2f}", txn["date"], txn["status"]))

        tree.pack(fill="both", expand=True)

    def _create_metric_card(self, parent, title, value, border_color, col_idx):
        card = tk.Frame(parent, bg=Theme.CARD_BG, padx=20, pady=15, highlightbackground=border_color, highlightthickness=1)
        card.grid(row=0, column=col_idx, padx=10, sticky="ew")
        parent.grid_columnconfigure(col_idx, weight=1)

        tk.Label(card, text=title, font=(Theme.FONT_FAMILY, 10, "bold"), fg=Theme.TEXT_MUTED, bg=Theme.CARD_BG).pack(anchor="w")
        tk.Label(card, text=value, font=(Theme.FONT_FAMILY, 18, "bold"), fg=Theme.TEXT_MAIN, bg=Theme.CARD_BG).pack(anchor="w", pady=(5, 0))

    def show_customers(self):
        self.clear_content()
        tk.Label(self.content_area, text="Customer Directory", font=(Theme.FONT_FAMILY, 20, "bold"), fg=Theme.TEXT_MAIN, bg=Theme.BG_DARK).pack(anchor="w", pady=(0, 20))

        columns = ("Account No", "Name", "Email", "Role", "Status")
        tree = ttk.Treeview(self.content_area, columns=columns, show="headings")
        
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor="center")

        for acn, acc in MOCK_ACCOUNTS.items():
            tree.insert("", "end", values=(acn, acc["name"], acc["email"], acc["role"], acc["status"]))

        tree.pack(fill="both", expand=True)

    def show_accounts(self):
        self.clear_content()
        tk.Label(self.content_area, text="Account Vault Balances", font=(Theme.FONT_FAMILY, 20, "bold"), fg=Theme.TEXT_MAIN, bg=Theme.BG_DARK).pack(anchor="w", pady=(0, 20))

        columns = ("Account No", "Name", "Current Balance", "Created Date")
        tree = ttk.Treeview(self.content_area, columns=columns, show="headings")
        
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor="center")

        for acn, acc in MOCK_ACCOUNTS.items():
            tree.insert("", "end", values=(acn, acc["name"], f"${acc['balance']:,.2f}", acc["created"]))

        tree.pack(fill="both", expand=True)

    def show_transactions(self):
        self.show_dashboard_home()

    def show_reports(self):
        self.clear_content()
        tk.Label(self.content_area, text="LUCIFER Analytical Reports", font=(Theme.FONT_FAMILY, 20, "bold"), fg=Theme.TEXT_MAIN, bg=Theme.BG_DARK).pack(anchor="w", pady=(0, 10))
        
        card = tk.Frame(self.content_area, bg=Theme.CARD_BG, padx=20, pady=20)
        card.pack(fill="x")
        tk.Label(card, text="Monthly Audit Summary", font=(Theme.FONT_FAMILY, 12, "bold"), fg=Theme.ACCENT_CYAN, bg=Theme.CARD_BG).pack(anchor="w")
        tk.Label(card, text="• System Integrity: 100% Verified\n• Reserve Ratio: 88.4%\n• Active User Growth: +12% this quarter", font=(Theme.FONT_FAMILY, 11), fg=Theme.TEXT_MAIN, bg=Theme.CARD_BG, justify="left").pack(anchor="w", pady=10)

    def show_settings(self):
        self.clear_content()
        tk.Label(self.content_area, text="System Configurations", font=(Theme.FONT_FAMILY, 20, "bold"), fg=Theme.TEXT_MAIN, bg=Theme.BG_DARK).pack(anchor="w", pady=(0, 10))
        card = tk.Frame(self.content_area, bg=Theme.CARD_BG, padx=20, pady=20)
        card.pack(fill="x")
        tk.Label(card, text="Environment: LUCIFER Desktop Production Mode v2.6", font=(Theme.FONT_FAMILY, 11), fg=Theme.TEXT_MAIN, bg=Theme.CARD_BG).pack(anchor="w")

    def show_change_password(self):
        ChangePasswordView(self.content_area)

# ==============================================================================
# SECTION 7: USER DASHBOARD MODULE
# ==============================================================================

class UserDashboard(BaseDashboard):
    def __init__(self, parent):
        super().__init__(parent, role_title="CLIENT PORTAL")
        self._setup_navigation()
        self.show_dashboard_home()

    def _setup_navigation(self):
        self.add_sidebar_btn("📊 My Dashboard", self.show_dashboard_home)
        self.add_sidebar_btn("👤 My Profile", self.show_profile)
        self.add_sidebar_btn("💵 Deposit Funds", self.show_deposit)
        self.add_sidebar_btn("💸 Withdraw Cash", self.show_withdraw)
        self.add_sidebar_btn("🔁 Transfer Money", self.show_transfer)
        self.add_sidebar_btn("📜 Statement History", self.show_history)
        self.add_sidebar_btn("🔑 Change PIN", self.show_change_password)
        self.add_sidebar_btn("🚪 Logout", self.logout)

    def show_dashboard_home(self):
        self.clear_content()

        # Welcome Label
        tk.Label(self.content_area, text=f"Welcome back, {CURRENT_USER['name']}!", font=(Theme.FONT_FAMILY, 20, "bold"), fg=Theme.TEXT_MAIN, bg=Theme.BG_DARK).pack(anchor="w", pady=(0, 10))

        # Balance Banner Card
        card = tk.Frame(self.content_area, bg=Theme.CARD_BG, padx=30, pady=20, highlightbackground=Theme.ACCENT_CYAN, highlightthickness=1)
        card.pack(fill="x", pady=(0, 20))

        tk.Label(card, text="AVAILABLE BALANCE", font=(Theme.FONT_FAMILY, 10, "bold"), fg=Theme.TEXT_MUTED, bg=Theme.CARD_BG).pack(anchor="w")
        
        balance_val = MOCK_ACCOUNTS[CURRENT_USER["acn"]]["balance"]
        tk.Label(card, text=f"${balance_val:,.2f}", font=(Theme.FONT_FAMILY, 28, "bold"), fg=Theme.SUCCESS, bg=Theme.CARD_BG).pack(anchor="w", pady=(5, 5))
        tk.Label(card, text=f"Account No: {CURRENT_USER['acn']} | Status: Active", font=(Theme.FONT_FAMILY, 10), fg=Theme.TEXT_MUTED, bg=Theme.CARD_BG).pack(anchor="w")

        # Mini Statement
        tk.Label(self.content_area, text="Recent Account Activity", font=(Theme.FONT_FAMILY, 14, "bold"), fg=Theme.TEXT_MAIN, bg=Theme.BG_DARK).pack(anchor="w", pady=(10, 10))

        user_txns = [t for t in MOCK_TRANSACTIONS if t["acn"] == CURRENT_USER["acn"]]

        columns = ("Transaction ID", "Type", "Amount", "Timestamp", "Status")
        tree = ttk.Treeview(self.content_area, columns=columns, show="headings")
        
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor="center")

        for txn in user_txns:
            tree.insert("", "end", values=(txn["id"], txn["type"], f"${txn['amount']:,.2f}", txn["date"], txn["status"]))

        tree.pack(fill="both", expand=True)

    def show_profile(self):
        self.clear_content()
        tk.Label(self.content_area, text="Client Account Profile", font=(Theme.FONT_FAMILY, 20, "bold"), fg=Theme.TEXT_MAIN, bg=Theme.BG_DARK).pack(anchor="w", pady=(0, 20))

        card = tk.Frame(self.content_area, bg=Theme.CARD_BG, padx=30, pady=25)
        card.pack(fill="x")

        fields = [
            ("Full Name:", CURRENT_USER["name"]),
            ("Account Number:", CURRENT_USER["acn"]),
            ("E-mail Address:", CURRENT_USER["email"]),
            ("Role Type:", CURRENT_USER["role"]),
            ("Account Created:", CURRENT_USER["created"])
        ]

        for i, (label, val) in enumerate(fields):
            tk.Label(card, text=label, font=(Theme.FONT_FAMILY, 11, "bold"), fg=Theme.TEXT_MUTED, bg=Theme.CARD_BG).grid(row=i, column=0, sticky="w", pady=8)
            tk.Label(card, text=val, font=(Theme.FONT_FAMILY, 11), fg=Theme.TEXT_MAIN, bg=Theme.CARD_BG).grid(row=i, column=1, sticky="w", padx=20, pady=8)

    def show_deposit(self):
        self.clear_content()
        tk.Label(self.content_area, text="Deposit Funds", font=(Theme.FONT_FAMILY, 20, "bold"), fg=Theme.TEXT_MAIN, bg=Theme.BG_DARK).pack(anchor="w", pady=(0, 20))

        card = tk.Frame(self.content_area, bg=Theme.CARD_BG, padx=30, pady=25, width=400)
        card.pack(anchor="w")

        tk.Label(card, text="Enter Amount ($):", font=(Theme.FONT_FAMILY, 11, "bold"), fg=Theme.TEXT_MUTED, bg=Theme.CARD_BG).pack(anchor="w")
        amt_entry = tk.Entry(card, font=(Theme.FONT_FAMILY, 12), bg="#111827", fg=Theme.TEXT_MAIN, insertbackground="white")
        amt_entry.pack(fill="x", pady=(5, 20), ipady=5)

        def process_deposit():
            try:
                val = float(amt_entry.get().strip())
                if val <= 0:
                    raise ValueError
                
                # Update State
                acn = CURRENT_USER["acn"]
                MOCK_ACCOUNTS[acn]["balance"] += val
                
                # Record Txn
                txn_id = f"TXN{len(MOCK_TRANSACTIONS)+9010}"
                now = datetime.now().strftime("%Y-%m-%d %H:%M")
                MOCK_TRANSACTIONS.insert(0, {"id": txn_id, "acn": acn, "type": "Deposit", "amount": val, "date": now, "status": "Success"})
                
                messagebox.showinfo("Success", f"Successfully deposited ${val:,.2f} into account!")
                self.show_dashboard_home()
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid positive numerical amount.")

        HoverButton(card, text="Confirm Deposit", command=process_deposit).pack(fill="x", ipady=6)

    def show_withdraw(self):
        self.clear_content()
        tk.Label(self.content_area, text="Cash Withdrawal", font=(Theme.FONT_FAMILY, 20, "bold"), fg=Theme.TEXT_MAIN, bg=Theme.BG_DARK).pack(anchor="w", pady=(0, 20))

        card = tk.Frame(self.content_area, bg=Theme.CARD_BG, padx=30, pady=25, width=400)
        card.pack(anchor="w")

        tk.Label(card, text="Enter Amount ($):", font=(Theme.FONT_FAMILY, 11, "bold"), fg=Theme.TEXT_MUTED, bg=Theme.CARD_BG).pack(anchor="w")
        amt_entry = tk.Entry(card, font=(Theme.FONT_FAMILY, 12), bg="#111827", fg=Theme.TEXT_MAIN, insertbackground="white")
        amt_entry.pack(fill="x", pady=(5, 20), ipady=5)

        def process_withdraw():
            try:
                val = float(amt_entry.get().strip())
                acn = CURRENT_USER["acn"]
                current_bal = MOCK_ACCOUNTS[acn]["balance"]

                if val <= 0:
                    raise ValueError
                if val > current_bal:
                    messagebox.showerror("Insufficient Funds", "Your account balance is lower than the requested withdrawal.")
                    return
                
                # Update State
                MOCK_ACCOUNTS[acn]["balance"] -= val
                
                # Record Txn
                txn_id = f"TXN{len(MOCK_TRANSACTIONS)+9010}"
                now = datetime.now().strftime("%Y-%m-%d %H:%M")
                MOCK_TRANSACTIONS.insert(0, {"id": txn_id, "acn": acn, "type": "Withdraw", "amount": val, "date": now, "status": "Success"})
                
                messagebox.showinfo("Success", f"Successfully withdrew ${val:,.2f}.")
                self.show_dashboard_home()
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid positive numerical amount.")

        HoverButton(card, text="Confirm Withdrawal", bg_color=Theme.DANGER, hover_color="#DC2626", command=process_withdraw).pack(fill="x", ipady=6)

    def show_transfer(self):
        self.clear_content()
        tk.Label(self.content_area, text="Internal Funds Transfer", font=(Theme.FONT_FAMILY, 20, "bold"), fg=Theme.TEXT_MAIN, bg=Theme.BG_DARK).pack(anchor="w", pady=(0, 20))

        card = tk.Frame(self.content_area, bg=Theme.CARD_BG, padx=30, pady=25, width=400)
        card.pack(anchor="w")

        tk.Label(card, text="Recipient Account Number:", font=(Theme.FONT_FAMILY, 11, "bold"), fg=Theme.TEXT_MUTED, bg=Theme.CARD_BG).pack(anchor="w")
        dest_entry = tk.Entry(card, font=(Theme.FONT_FAMILY, 12), bg="#111827", fg=Theme.TEXT_MAIN, insertbackground="white")
        dest_entry.pack(fill="x", pady=(5, 15), ipady=5)

        tk.Label(card, text="Transfer Amount ($):", font=(Theme.FONT_FAMILY, 11, "bold"), fg=Theme.TEXT_MUTED, bg=Theme.CARD_BG).pack(anchor="w")
        amt_entry = tk.Entry(card, font=(Theme.FONT_FAMILY, 12), bg="#111827", fg=Theme.TEXT_MAIN, insertbackground="white")
        amt_entry.pack(fill="x", pady=(5, 20), ipady=5)

        def process_transfer():
            dest = dest_entry.get().strip()
            sender = CURRENT_USER["acn"]

            if dest == sender:
                messagebox.showerror("Error", "You cannot transfer money to your own account.")
                return

            if dest not in MOCK_ACCOUNTS:
                messagebox.showerror("Error", "Recipient Account Number not found.")
                return

            try:
                val = float(amt_entry.get().strip())
                if val <= 0:
                    raise ValueError
                if val > MOCK_ACCOUNTS[sender]["balance"]:
                    messagebox.showerror("Error", "Insufficient balance for this transfer.")
                    return

                # Deduct & Add
                MOCK_ACCOUNTS[sender]["balance"] -= val
                MOCK_ACCOUNTS[dest]["balance"] += val

                # Txn Log
                txn_id = f"TXN{len(MOCK_TRANSACTIONS)+9010}"
                now = datetime.now().strftime("%Y-%m-%d %H:%M")
                MOCK_TRANSACTIONS.insert(0, {"id": txn_id, "acn": sender, "type": "Transfer", "amount": val, "date": now, "status": "Success"})

                messagebox.showinfo("Transfer Complete", f"Transferred ${val:,.2f} to {MOCK_ACCOUNTS[dest]['name']}.")
                self.show_dashboard_home()
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid amount.")

        HoverButton(card, text="Send Transfer", command=process_transfer).pack(fill="x", ipady=6)

    def show_history(self):
        self.show_dashboard_home()

    def show_change_password(self):
        ChangePasswordView(self.content_area)
        
# SECTION 8: COMMON VIEWS (CHANGE PASSWORD)

class ChangePasswordView:
    def __init__(self, parent_frame):
        for w in parent_frame.winfo_children():
            w.destroy()

        tk.Label(parent_frame, text="Security & Credentials", font=(Theme.FONT_FAMILY, 20, "bold"), fg=Theme.TEXT_MAIN, bg=Theme.BG_DARK).pack(anchor="w", pady=(0, 20))

        card = tk.Frame(parent_frame, bg=Theme.CARD_BG, padx=30, pady=25, width=400)
        card.pack(anchor="w")

        tk.Label(card, text="Current Password / PIN:", font=(Theme.FONT_FAMILY, 10, "bold"), fg=Theme.TEXT_MUTED, bg=Theme.CARD_BG).pack(anchor="w")
        curr_p = tk.Entry(card, font=(Theme.FONT_FAMILY, 11), show="•", bg="#111827", fg=Theme.TEXT_MAIN, insertbackground="white")
        curr_p.pack(fill="x", pady=(2, 15), ipady=4)

        tk.Label(card, text="New Password / PIN:", font=(Theme.FONT_FAMILY, 10, "bold"), fg=Theme.TEXT_MUTED, bg=Theme.CARD_BG).pack(anchor="w")
        new_p = tk.Entry(card, font=(Theme.FONT_FAMILY, 11), show="•", bg="#111827", fg=Theme.TEXT_MAIN, insertbackground="white")
        new_p.pack(fill="x", pady=(2, 15), ipady=4)

        def save_password():
            cp = curr_p.get().strip()
            np = new_p.get().strip()

            if not cp or not np:
                messagebox.showerror("Error", "All password fields are required.")
                return

            acn = CURRENT_USER["acn"]
            if MOCK_ACCOUNTS[acn]["pin"] != cp:
                messagebox.showerror("Error", "Current password does not match.")
                return

            MOCK_ACCOUNTS[acn]["pin"] = np
            messagebox.showinfo("Success", "Password updated successfully!")
            curr_p.delete(0, tk.END)
            new_p.delete(0, tk.END)

        HoverButton(card, text="Update Password", command=save_password).pack(fill="x", ipady=6)

# SECTION 9: MAIN ENTRY POINT

if __name__ == "__main__":
    app = LuciferApp()
    app.mainloop()