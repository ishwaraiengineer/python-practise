

import tkinter as tk
from tkinter import ttk, messagebox

# ---------------------------------------------------------------------------
# Color / Font constants - single source of truth for the whole theme.
# ---------------------------------------------------------------------------
COLOR_SIDEBAR = "#1E293B"       # Dark blue sidebar
COLOR_SIDEBAR_HOVER = "#334155"
COLOR_SIDEBAR_ACTIVE = "#2563EB"
COLOR_TOPBAR = "#FFFFFF"
COLOR_CONTENT_BG = "#F8FAFC"
COLOR_CARD_BG = "#FFFFFF"
COLOR_TEXT_DARK = "#1E293B"
COLOR_TEXT_MUTED = "#64748B"
COLOR_ACCENT = "#2563EB"
COLOR_ACCENT_HOVER = "#1D4ED8"
COLOR_DANGER = "#DC2626"
COLOR_DANGER_HOVER = "#B91C1C"
COLOR_SUCCESS = "#16A34A"

FONT_TITLE = ("Segoe UI", 18, "bold")
FONT_SUBTITLE = ("Segoe UI", 11)
FONT_LABEL = ("Segoe UI", 10, "bold")
FONT_NORMAL = ("Segoe UI", 10)
FONT_SIDEBAR_BTN = ("Segoe UI", 11)

SIDEBAR_WIDTH = 220
TOPBAR_HEIGHT = 60


class Dashboard:
    """Main application window shown after a successful login."""

    def __init__(self, root):
        self.root = root
        self.root.title("Restaurant Management System - Dashboard")
        self.root.geometry("1200x700")
        self.root.minsize(1000, 600)
        self.root.configure(bg=COLOR_CONTENT_BG)

        # -----------------------------------------------------------------
        # In-memory "database" of menu items.
        # TODO (future DB integration): replace this list with real queries
        #   to SQLite/MySQL, e.g. a MenuRepository class with
        #   get_all(), add(), update(), delete() methods backed by SQL.
        # -----------------------------------------------------------------
        self.menu_items = [
            {"id": 1, "name": "Margherita Pizza", "category": "Main Course", "price": 8.99, "availability": "Available"},
            {"id": 2, "name": "Caesar Salad", "category": "Starters", "price": 5.49, "availability": "Available"},
            {"id": 3, "name": "Chocolate Lava Cake", "category": "Desserts", "price": 4.99, "availability": "Out of Stock"},
            {"id": 4, "name": "Iced Lemon Tea", "category": "Beverages", "price": 2.99, "availability": "Available"},
        ]
        self.next_item_id = 5  # simple auto-increment for the in-memory list

        # In-memory profile data.
        # TODO (future DB integration): load/save from a `restaurant_profile` table.
        self.profile_data = {
            "restaurant_name": "The Golden Spoon",
            "owner_name": "John Carter",
            "phone": "+1 555-123-4567",
            "email": "contact@goldenspoon.com",
            "address": "123 Flavor Street, Food City, FC 45678",
        }

        # Keeps track of which row (item id) is currently selected in the table
        self.selected_item_id = None

        # Configure ttk styles
        self._configure_styles()

        # Build the overall layout (sidebar + topbar + content)
        self._build_layout()

        # Load the default page
        self.show_menu_page()

    # ---------------------------------------------------------------- #
    # Styles
    # ---------------------------------------------------------------- #
    def _configure_styles(self):
        style = ttk.Style()
        style.theme_use("clam")

        # Treeview (table) styling
        style.configure(
            "Custom.Treeview",
            background="#FFFFFF",
            foreground=COLOR_TEXT_DARK,
            rowheight=32,
            fieldbackground="#FFFFFF",
            font=FONT_NORMAL,
            borderwidth=0,
        )
        style.configure(
            "Custom.Treeview.Heading",
            font=("Segoe UI", 10, "bold"),
            background="#E2E8F0",
            foreground=COLOR_TEXT_DARK,
            relief="flat",
        )
        style.map("Custom.Treeview", background=[("selected", "#DBEAFE")],
                  foreground=[("selected", COLOR_TEXT_DARK)])

        # General action button (blue)
        style.configure(
            "Accent.TButton",
            font=("Segoe UI", 10, "bold"),
            padding=8,
            background=COLOR_ACCENT,
            foreground="#FFFFFF",
            borderwidth=0,
        )
        style.map("Accent.TButton", background=[("active", COLOR_ACCENT_HOVER)])

        # Danger button (red) - for delete actions
        style.configure(
            "Danger.TButton",
            font=("Segoe UI", 10, "bold"),
            padding=8,
            background=COLOR_DANGER,
            foreground="#FFFFFF",
            borderwidth=0,
        )
        style.map("Danger.TButton", background=[("active", COLOR_DANGER_HOVER)])

        # Neutral button (grey) - for clear/cancel actions
        style.configure(
            "Neutral.TButton",
            font=("Segoe UI", 10, "bold"),
            padding=8,
            background="#64748B",
            foreground="#FFFFFF",
            borderwidth=0,
        )
        style.map("Neutral.TButton", background=[("active", "#475569")])

        # Entry style
        style.configure(
            "Custom.TEntry",
            padding=6,
            relief="flat",
            fieldbackground="#F1F5F9",
        )

    # ---------------------------------------------------------------- #
    # Overall layout: sidebar / topbar / content
    # ---------------------------------------------------------------- #
    def _build_layout(self):
        # --- Sidebar (left, fixed width) ---
        self.sidebar = tk.Frame(self.root, bg=COLOR_SIDEBAR, width=SIDEBAR_WIDTH)
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)  # keep fixed width regardless of contents
        self._build_sidebar()

        # --- Right side container (topbar + content stacked vertically) ---
        right_container = tk.Frame(self.root, bg=COLOR_CONTENT_BG)
        right_container.pack(side="right", fill="both", expand=True)

        # Top bar
        self.topbar = tk.Frame(right_container, bg=COLOR_TOPBAR, height=TOPBAR_HEIGHT)
        self.topbar.pack(side="top", fill="x")
        self.topbar.pack_propagate(False)
        self._build_topbar()

        # Main content area (pages get swapped in here)
        self.content = tk.Frame(right_container, bg=COLOR_CONTENT_BG)
        self.content.pack(side="top", fill="both", expand=True)

    # ---------------------------------------------------------------- #
    # Sidebar
    # ---------------------------------------------------------------- #
    def _build_sidebar(self):
        """Builds the fixed left sidebar with Profile / Menu / Logout."""

        # --- Top: Logo / App name ---
        top_frame = tk.Frame(self.sidebar, bg=COLOR_SIDEBAR)
        top_frame.pack(side="top", fill="x", pady=(25, 10))

        tk.Label(
            top_frame,
            text="🍴 RMS",
            font=("Segoe UI", 16, "bold"),
            bg=COLOR_SIDEBAR,
            fg="#FFFFFF",
        ).pack(pady=(0, 20))

        # Profile button (top section)
        self.profile_btn = self._create_sidebar_button(
            top_frame, "👤  Profile", self.show_profile_page
        )
        self.profile_btn.pack(fill="x", padx=15, pady=5)

        # --- Middle: Menu button ---
        middle_frame = tk.Frame(self.sidebar, bg=COLOR_SIDEBAR)
        middle_frame.pack(side="top", fill="x", pady=10)

        self.menu_btn = self._create_sidebar_button(
            middle_frame, "🍽  Menu", self.show_menu_page
        )
        self.menu_btn.pack(fill="x", padx=15, pady=5)

        # --- Bottom: Logout button ---
        bottom_frame = tk.Frame(self.sidebar, bg=COLOR_SIDEBAR)
        bottom_frame.pack(side="bottom", fill="x", pady=20)

        self.logout_btn = self._create_sidebar_button(
            bottom_frame, "🚪  Logout", self._handle_logout, danger=True
        )
        self.logout_btn.pack(fill="x", padx=15, pady=5)

    def _create_sidebar_button(self, parent, text, command, danger=False):
        """Creates a flat, modern-looking sidebar navigation button."""
        btn = tk.Button(
            parent,
            text=text,
            font=FONT_SIDEBAR_BTN,
            bg=COLOR_SIDEBAR,
            fg="#FFFFFF",
            activebackground=COLOR_DANGER_HOVER if danger else COLOR_SIDEBAR_ACTIVE,
            activeforeground="#FFFFFF",
            bd=0,
            relief="flat",
            anchor="w",
            padx=15,
            pady=12,
            cursor="hand2",
            command=command,
        )

        hover_color = COLOR_DANGER if danger else COLOR_SIDEBAR_HOVER

        def on_enter(event):
            btn.configure(bg=hover_color)

        def on_leave(event):
            btn.configure(bg=COLOR_SIDEBAR)

        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)
        return btn

    # ---------------------------------------------------------------- #
    # Top bar
    # ---------------------------------------------------------------- #
    def _build_topbar(self):
        """Builds the top bar with restaurant title and search box."""

        tk.Label(
            self.topbar,
            text=self.profile_data["restaurant_name"],
            font=FONT_TITLE,
            bg=COLOR_TOPBAR,
            fg=COLOR_TEXT_DARK,
        ).pack(side="left", padx=25)

        search_frame = tk.Frame(self.topbar, bg=COLOR_TOPBAR)
        search_frame.pack(side="right", padx=25)

        self.global_search_entry = ttk.Entry(
            search_frame, style="Custom.TEntry", font=FONT_NORMAL, width=28
        )
        self.global_search_entry.pack(side="left", ipady=4, padx=(0, 8))
        self.global_search_entry.bind("<Return>", lambda e: self._handle_global_search())

        ttk.Button(
            search_frame,
            text="Search",
            style="Accent.TButton",
            command=self._handle_global_search,
        ).pack(side="left")

    def _handle_global_search(self):
        """Handles searches triggered from the top bar's global search box."""
        query = self.global_search_entry.get().strip()
        if not query:
            return
        # A global search simply routes to the Menu page and filters it.
        self.show_menu_page()
        self.menu_search_entry.delete(0, tk.END)
        self.menu_search_entry.insert(0, query)
        self._filter_menu_items()

    # ---------------------------------------------------------------- #
    # Page switching helper
    # ---------------------------------------------------------------- #
    def _clear_content(self):
        """Removes all widgets currently in the main content frame."""
        for widget in self.content.winfo_children():
            widget.destroy()

    def _highlight_active_nav(self, active_btn):
        """Visually marks which sidebar button is currently active."""
        for btn in (self.profile_btn, self.menu_btn):
            btn.configure(bg=COLOR_SIDEBAR)
        active_btn.configure(bg=COLOR_SIDEBAR_ACTIVE)

    # ================================================================== #
    # MENU MANAGEMENT PAGE
    # ================================================================== #
    def show_menu_page(self):
        """Loads the Menu Management page into the content frame."""
        self._clear_content()
        self._highlight_active_nav(self.menu_btn)
        self.selected_item_id = None

        page = tk.Frame(self.content, bg=COLOR_CONTENT_BG)
        page.pack(fill="both", expand=True, padx=25, pady=20)

        # --- Page title ---
        tk.Label(
            page,
            text="Menu Management",
            font=FONT_TITLE,
            bg=COLOR_CONTENT_BG,
            fg=COLOR_TEXT_DARK,
        ).pack(anchor="w", pady=(0, 15))

        # --- Toolbar: action buttons + search ---
        toolbar = tk.Frame(page, bg=COLOR_CONTENT_BG)
        toolbar.pack(fill="x", pady=(0, 15))

        actions_frame = tk.Frame(toolbar, bg=COLOR_CONTENT_BG)
        actions_frame.pack(side="left")

        ttk.Button(actions_frame, text="Add Item", style="Accent.TButton",
                   command=self._add_item).pack(side="left", padx=(0, 8))
        ttk.Button(actions_frame, text="Update Item", style="Accent.TButton",
                   command=self._update_item).pack(side="left", padx=8)
        ttk.Button(actions_frame, text="Delete Item", style="Danger.TButton",
                   command=self._delete_item).pack(side="left", padx=8)
        ttk.Button(actions_frame, text="Clear", style="Neutral.TButton",
                   command=self._clear_form).pack(side="left", padx=8)

        search_frame = tk.Frame(toolbar, bg=COLOR_CONTENT_BG)
        search_frame.pack(side="right")

        self.menu_search_entry = ttk.Entry(
            search_frame, style="Custom.TEntry", font=FONT_NORMAL, width=22
        )
        self.menu_search_entry.pack(side="left", ipady=4, padx=(0, 8))
        self.menu_search_entry.bind("<Return>", lambda e: self._filter_menu_items())

        ttk.Button(search_frame, text="Search", style="Accent.TButton",
                   command=self._filter_menu_items).pack(side="left")

        # --- Body: table (left) + form (right) ---
        body = tk.Frame(page, bg=COLOR_CONTENT_BG)
        body.pack(fill="both", expand=True)

        table_card = tk.Frame(body, bg=COLOR_CARD_BG)
        table_card.pack(side="left", fill="both", expand=True, padx=(0, 15))

        form_card = tk.Frame(body, bg=COLOR_CARD_BG, width=300)
        form_card.pack(side="right", fill="y")
        form_card.pack_propagate(False)

        self._build_menu_table(table_card)
        self._build_menu_form(form_card)

        # Populate table with current data
        self._refresh_menu_table()

    def _build_menu_table(self, parent):
        """Creates the Treeview table listing menu items."""
        container = tk.Frame(parent, bg=COLOR_CARD_BG)
        container.pack(fill="both", expand=True, padx=15, pady=15)

        columns = ("id", "name", "category", "price", "availability")
        self.menu_tree = ttk.Treeview(
            container,
            columns=columns,
            show="headings",
            style="Custom.Treeview",
        )

        headings = {
            "id": "Item ID",
            "name": "Item Name",
            "category": "Category",
            "price": "Price",
            "availability": "Availability",
        }
        widths = {"id": 70, "name": 180, "category": 120, "price": 80, "availability": 110}

        for col in columns:
            self.menu_tree.heading(col, text=headings[col])
            self.menu_tree.column(col, width=widths[col], anchor="center")

        # Scrollbar
        scrollbar = ttk.Scrollbar(container, orient="vertical", command=self.menu_tree.yview)
        self.menu_tree.configure(yscrollcommand=scrollbar.set)

        self.menu_tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        self.menu_tree.bind("<<TreeviewSelect>>", self._on_row_select)

    def _build_menu_form(self, parent):
        """Creates the Add/Update form for a menu item."""
        tk.Label(
            parent, text="Item Details", font=("Segoe UI", 13, "bold"),
            bg=COLOR_CARD_BG, fg=COLOR_TEXT_DARK,
        ).pack(anchor="w", padx=20, pady=(20, 15))

        form_inner = tk.Frame(parent, bg=COLOR_CARD_BG)
        form_inner.pack(fill="x", padx=20)

        # Item Name
        tk.Label(form_inner, text="Item Name", font=FONT_LABEL, bg=COLOR_CARD_BG,
                 fg=COLOR_TEXT_DARK, anchor="w").pack(fill="x")
        self.name_entry = ttk.Entry(form_inner, style="Custom.TEntry", font=FONT_NORMAL)
        self.name_entry.pack(fill="x", pady=(5, 15), ipady=4)

        # Category
        tk.Label(form_inner, text="Category", font=FONT_LABEL, bg=COLOR_CARD_BG,
                 fg=COLOR_TEXT_DARK, anchor="w").pack(fill="x")
        self.category_combo = ttk.Combobox(
            form_inner, font=FONT_NORMAL, state="readonly",
            values=["Starters", "Main Course", "Desserts", "Beverages"],
        )
        self.category_combo.pack(fill="x", pady=(5, 15), ipady=4)

        # Price
        tk.Label(form_inner, text="Price ($)", font=FONT_LABEL, bg=COLOR_CARD_BG,
                 fg=COLOR_TEXT_DARK, anchor="w").pack(fill="x")
        self.price_entry = ttk.Entry(form_inner, style="Custom.TEntry", font=FONT_NORMAL)
        self.price_entry.pack(fill="x", pady=(5, 15), ipady=4)

        # Availability
        tk.Label(form_inner, text="Availability", font=FONT_LABEL, bg=COLOR_CARD_BG,
                 fg=COLOR_TEXT_DARK, anchor="w").pack(fill="x")
        self.availability_combo = ttk.Combobox(
            form_inner, font=FONT_NORMAL, state="readonly",
            values=["Available", "Out of Stock"],
        )
        self.availability_combo.pack(fill="x", pady=(5, 20), ipady=4)

        # Form buttons
        btn_frame = tk.Frame(parent, bg=COLOR_CARD_BG)
        btn_frame.pack(fill="x", padx=20, pady=(0, 20))

        ttk.Button(btn_frame, text="Save", style="Accent.TButton",
                   command=self._add_item).pack(fill="x", pady=4)
        ttk.Button(btn_frame, text="Update", style="Accent.TButton",
                   command=self._update_item).pack(fill="x", pady=4)
        ttk.Button(btn_frame, text="Delete", style="Danger.TButton",
                   command=self._delete_item).pack(fill="x", pady=4)
        ttk.Button(btn_frame, text="Clear", style="Neutral.TButton",
                   command=self._clear_form).pack(fill="x", pady=4)

    # ---------------------------------------------------------------- #
    # Menu Management: data operations
    # ---------------------------------------------------------------- #
    def _refresh_menu_table(self, items=None):
        """Reloads the Treeview with the given items (or all items)."""
        self.menu_tree.delete(*self.menu_tree.get_children())
        data = items if items is not None else self.menu_items
        for item in data:
            self.menu_tree.insert(
                "", "end", iid=item["id"],
                values=(item["id"], item["name"], item["category"],
                        f"{item['price']:.2f}", item["availability"]),
            )

    def _on_row_select(self, event):
        """Fills the form with the selected row's data."""
        selection = self.menu_tree.selection()
        if not selection:
            return

        item_id = int(selection[0])
        item = next((i for i in self.menu_items if i["id"] == item_id), None)
        if not item:
            return

        self.selected_item_id = item_id
        self.name_entry.delete(0, tk.END)
        self.name_entry.insert(0, item["name"])
        self.category_combo.set(item["category"])
        self.price_entry.delete(0, tk.END)
        self.price_entry.insert(0, str(item["price"]))
        self.availability_combo.set(item["availability"])

    def _get_form_values(self):
        """Reads and validates form field values. Returns dict or None."""
        name = self.name_entry.get().strip()
        category = self.category_combo.get().strip()
        price_text = self.price_entry.get().strip()
        availability = self.availability_combo.get().strip()

        if not name or not category or not price_text or not availability:
            messagebox.showwarning("Missing Fields", "Please fill in all fields.")
            return None

        try:
            price = float(price_text)
            if price < 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Invalid Price", "Price must be a positive number.")
            return None

        return {"name": name, "category": category, "price": price, "availability": availability}

    def _add_item(self):
        """Adds a new menu item to the in-memory list and table."""
        values = self._get_form_values()
        if values is None:
            return

        # TODO (future DB integration): INSERT INTO menu_items (...) VALUES (...)
        new_item = {"id": self.next_item_id, **values}
        self.menu_items.append(new_item)
        self.next_item_id += 1

        self._refresh_menu_table()
        self._clear_form()
        messagebox.showinfo("Success", "Item added successfully.")

    def _update_item(self):
        """Updates the currently selected menu item."""
        if self.selected_item_id is None:
            messagebox.showwarning("No Selection", "Please select an item to update.")
            return

        values = self._get_form_values()
        if values is None:
            return

        # TODO (future DB integration): UPDATE menu_items SET ... WHERE id=?
        for item in self.menu_items:
            if item["id"] == self.selected_item_id:
                item.update(values)
                break

        self._refresh_menu_table()
        self._clear_form()
        messagebox.showinfo("Success", "Item updated successfully.")

    def _delete_item(self):
        """Deletes the currently selected menu item."""
        if self.selected_item_id is None:
            messagebox.showwarning("No Selection", "Please select an item to delete.")
            return

        confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this item?")
        if not confirm:
            return

        # TODO (future DB integration): DELETE FROM menu_items WHERE id=?
        self.menu_items = [i for i in self.menu_items if i["id"] != self.selected_item_id]

        self._refresh_menu_table()
        self._clear_form()
        messagebox.showinfo("Deleted", "Item deleted successfully.")

    def _clear_form(self):
        """Clears the form fields and deselects any table row."""
        self.selected_item_id = None
        self.name_entry.delete(0, tk.END)
        self.category_combo.set("")
        self.price_entry.delete(0, tk.END)
        self.availability_combo.set("")
        if self.menu_tree.selection():
            self.menu_tree.selection_remove(self.menu_tree.selection())

    def _filter_menu_items(self):
        """Filters the table based on the search entry's text."""
        query = self.menu_search_entry.get().strip().lower()
        if not query:
            self._refresh_menu_table()
            return

        filtered = [
            item for item in self.menu_items
            if query in item["name"].lower() or query in item["category"].lower()
        ]
        self._refresh_menu_table(filtered)

    # ================================================================== #
    # PROFILE PAGE
    # ================================================================== #
    def show_profile_page(self):
        """Loads the Restaurant Profile page into the content frame."""
        self._clear_content()
        self._highlight_active_nav(self.profile_btn)

        page = tk.Frame(self.content, bg=COLOR_CONTENT_BG)
        page.pack(fill="both", expand=True, padx=25, pady=20)

        tk.Label(
            page, text="Restaurant Profile", font=FONT_TITLE,
            bg=COLOR_CONTENT_BG, fg=COLOR_TEXT_DARK,
        ).pack(anchor="w", pady=(0, 15))

        card = tk.Frame(page, bg=COLOR_CARD_BG)
        card.pack(fill="both", expand=True)

        form_inner = tk.Frame(card, bg=COLOR_CARD_BG)
        form_inner.pack(fill="x", padx=40, pady=40)

        self.profile_entries = {}
        fields = [
            ("restaurant_name", "Restaurant Name"),
            ("owner_name", "Owner Name"),
            ("phone", "Phone"),
            ("email", "Email"),
            ("address", "Address"),
        ]

        for key, label_text in fields:
            tk.Label(
                form_inner, text=label_text, font=FONT_LABEL,
                bg=COLOR_CARD_BG, fg=COLOR_TEXT_DARK, anchor="w",
            ).pack(fill="x", pady=(10, 0))

            entry = ttk.Entry(form_inner, style="Custom.TEntry", font=FONT_NORMAL, state="disabled")
            entry.pack(fill="x", pady=(5, 0), ipady=5)
            entry.configure(state="normal")
            entry.insert(0, self.profile_data[key])
            entry.configure(state="disabled")
            self.profile_entries[key] = entry

        # Buttons
        btn_frame = tk.Frame(card, bg=COLOR_CARD_BG)
        btn_frame.pack(fill="x", padx=40, pady=(0, 30))

        self.profile_edit_btn = ttk.Button(
            btn_frame, text="Edit", style="Accent.TButton",
            command=self._toggle_profile_edit,
        )
        self.profile_edit_btn.pack(side="left", padx=(0, 10))

        self.profile_save_btn = ttk.Button(
            btn_frame, text="Save", style="Accent.TButton",
            command=self._save_profile, state="disabled",
        )
        self.profile_save_btn.pack(side="left")

    def _toggle_profile_edit(self):
        """Enables editing of all profile fields."""
        for entry in self.profile_entries.values():
            entry.configure(state="normal")
        self.profile_save_btn.configure(state="normal")

    def _save_profile(self):
        """Persists the edited profile fields back into profile_data."""
        # TODO (future DB integration): UPDATE restaurant_profile SET ... WHERE id=?
        for key, entry in self.profile_entries.items():
            self.profile_data[key] = entry.get().strip()
            entry.configure(state="disabled")

        self.profile_save_btn.configure(state="disabled")

        # Reflect the (possibly) updated restaurant name in the top bar title
        self._refresh_topbar_title()

        messagebox.showinfo("Saved", "Profile updated successfully.")

    def _refresh_topbar_title(self):
        """Updates the restaurant name label shown in the top bar."""
        for widget in self.topbar.winfo_children():
            if isinstance(widget, tk.Label):
                widget.configure(text=self.profile_data["restaurant_name"])
                break

    # ================================================================== #
    # LOGOUT
    # ================================================================== #
    def _handle_logout(self):
        """Confirms and logs the user out, returning to the Login window."""
        confirm = messagebox.askyesno("Logout", "Are you sure you want to logout?")
        if not confirm:
            return

        # Import here to avoid a circular import with login.py
        from login import LoginWindow

        self.root.destroy()

        login_root = tk.Tk()
        LoginWindow(login_root)
        login_root.mainloop()


def main():
    """Allows running the dashboard directly for quick UI testing."""
    root = tk.Tk()
    Dashboard(root)
    root.mainloop()


if __name__ == "__main__":
    main()