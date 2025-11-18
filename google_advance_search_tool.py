#!/usr/bin/env python3
"""
Google Advanced Search Tool - Modern Animated GUI
Based on the TECH.pdf design with CustomTkinter for modern look
"""

import tkinter as tk
import customtkinter as ctk
import webbrowser
from urllib.parse import quote_plus
import pyperclip

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class ModernGoogleDorkTool(ctk.CTk):
    """Main application with modern animated GUI"""
    
    FILE_TYPES = [
        "None", "ppt", "pptx", "csv", "xls", "xlsx", "xml",
        "docx", "doc", "txt", "exe", "iso", "rar", "pdf",
        "img", "json", "zip", "sql"
    ]
    
    def __init__(self):
        super().__init__()
        
        # Window configuration
        self.title("Google-Advance-Search-Tool")
        self.geometry("900x600")
        self.resizable(False, False)
        
        # Variables
        self.selected_filetype = tk.StringVar(value="None")
        self.generated_query = tk.StringVar(value="")
        
        # Animation state
        self.animation_running = False
        
        # Create UI
        self.create_widgets()
        
        # Start entrance animation
        self.after(100, self.entrance_animation)
    
    def create_widgets(self):
        """Create all UI components"""
        
        # Main container with 3 columns
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=0)
        
        # LEFT SECTION - Query Type (File Types)
        self.left_frame = ctk.CTkFrame(self, corner_radius=15)
        self.left_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.left_frame.grid_propagate(False)
        
        # Title
        title_left = ctk.CTkLabel(
            self.left_frame,
            text="Query Type",
            font=ctk.CTkFont(size=20, weight="bold")
        )
        title_left.pack(pady=(20, 15))
        
        # Scrollable frame for file types
        self.filetype_frame = ctk.CTkScrollableFrame(
            self.left_frame,
            width=180,
            height=400
        )
        self.filetype_frame.pack(fill="both", expand=True, padx=10, pady=(0, 10))
        
        # Create radio buttons for file types
        self.filetype_buttons = {}
        for ft in self.FILE_TYPES:
            btn = ctk.CTkRadioButton(
                self.filetype_frame,
                text=ft,
                variable=self.selected_filetype,
                value=ft,
                font=ctk.CTkFont(size=14),
                command=self.on_filetype_change
            )
            btn.pack(anchor="w", pady=5, padx=10)
            self.filetype_buttons[ft] = btn
        
        # CENTER SECTION - Search Query
        self.center_frame = ctk.CTkFrame(self, corner_radius=15)
        self.center_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        
        # Title
        title_center = ctk.CTkLabel(
            self.center_frame,
            text="SEARCH-QUERY",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        title_center.pack(pady=(30, 20))
        
        # Search input
        self.search_entry = ctk.CTkTextbox(
            self.center_frame,
            height=150,
            font=ctk.CTkFont(size=16),
            corner_radius=10
        )
        self.search_entry.pack(padx=30, pady=10, fill="both", expand=True)
        self.search_entry.insert("1.0", "Your Query Here")
        self.search_entry.bind("<FocusIn>", self.clear_placeholder)
        
        # Generated Query Display
        generated_label = ctk.CTkLabel(
            self.center_frame,
            text="Generated Query:",
            font=ctk.CTkFont(size=14, weight="bold")
        )
        generated_label.pack(pady=(10, 5), padx=30, anchor="w")
        
        self.output_box = ctk.CTkTextbox(
            self.center_frame,
            height=80,
            font=ctk.CTkFont(size=14),
            corner_radius=10,
            state="disabled"
        )
        self.output_box.pack(padx=30, pady=(0, 20), fill="x")
        
        # RIGHT SECTION - Action Buttons
        self.right_frame = ctk.CTkFrame(self, corner_radius=15)
        self.right_frame.grid(row=0, column=2, padx=20, pady=20, sticky="nsew")
        
        # Buttons with different colors
        self.btn_generate = ctk.CTkButton(
            self.right_frame,
            text="GENERATE\nQUERY",
            font=ctk.CTkFont(size=16, weight="bold"),
            height=80,
            corner_radius=15,
            fg_color="#2196F3",
            hover_color="#1976D2",
            command=self.generate_query
        )
        self.btn_generate.pack(pady=(40, 15), padx=20, fill="x")
        
        self.btn_clear = ctk.CTkButton(
            self.right_frame,
            text="CLEAR\nQUERY",
            font=ctk.CTkFont(size=16, weight="bold"),
            height=80,
            corner_radius=15,
            fg_color="#FF9800",
            hover_color="#F57C00",
            command=self.clear_query
        )
        self.btn_clear.pack(pady=15, padx=20, fill="x")
        
        self.btn_search = ctk.CTkButton(
            self.right_frame,
            text="SEARCH\nQUERY",
            font=ctk.CTkFont(size=16, weight="bold"),
            height=80,
            corner_radius=15,
            fg_color="#4CAF50",
            hover_color="#388E3C",
            command=self.search_query
        )
        self.btn_search.pack(pady=15, padx=20, fill="x")
        
        self.btn_copy = ctk.CTkButton(
            self.right_frame,
            text="COPY\nQUERY",
            font=ctk.CTkFont(size=16, weight="bold"),
            height=80,
            corner_radius=15,
            fg_color="#9C27B0",
            hover_color="#7B1FA2",
            command=self.copy_query
        )
        self.btn_copy.pack(pady=15, padx=20, fill="x")
        
        # Status bar at bottom
        self.status_bar = ctk.CTkLabel(
            self,
            text="Ready",
            font=ctk.CTkFont(size=12),
            anchor="w"
        )
        self.status_bar.grid(row=1, column=0, columnspan=3, sticky="ew", padx=20, pady=(0, 10))
        
        # Initially hide frames for animation
        self.left_frame.grid_remove()
        self.center_frame.grid_remove()
        self.right_frame.grid_remove()
    
    def entrance_animation(self):
        """Animate entrance of UI elements"""
        # Slide in left frame
        self.left_frame.grid()
        self.animate_slide(self.left_frame, "left", 0)
        
        # Slide in center frame (delayed)
        self.after(150, lambda: self.center_frame.grid())
        self.after(150, lambda: self.animate_fade(self.center_frame, 0))
        
        # Slide in right frame (delayed)
        self.after(300, lambda: self.right_frame.grid())
        self.after(300, lambda: self.animate_slide(self.right_frame, "right", 0))
    
    def animate_slide(self, widget, direction, step):
        """Slide animation for widgets"""
        if step <= 10:
            if direction == "left":
                offset = int(20 * (1 - step/10))
                widget.grid(row=0, column=0, padx=(offset, 20), pady=20, sticky="nsew")
            elif direction == "right":
                offset = int(20 * (1 - step/10))
                widget.grid(row=0, column=2, padx=(20, offset), pady=20, sticky="nsew")
            self.after(20, lambda: self.animate_slide(widget, direction, step + 1))
    
    def animate_fade(self, widget, step):
        """Fade in animation"""
        if step <= 10:
            # CustomTkinter doesn't support alpha directly, but we can simulate with updates
            self.after(20, lambda: self.animate_fade(widget, step + 1))
    
    def clear_placeholder(self, event):
        """Clear placeholder text on focus"""
        if self.search_entry.get("1.0", "end-1c") == "Your Query Here":
            self.search_entry.delete("1.0", "end")
    
    def on_filetype_change(self):
        """Handle file type selection change with animation"""
        selected = self.selected_filetype.get()
        self.animate_button_pulse(self.filetype_buttons[selected])
        self.status_bar.configure(text=f"Selected file type: {selected}")
    
    def animate_button_pulse(self, button):
        """Pulse animation for button selection"""
        original_fg = button.cget("fg_color")
        button.configure(fg_color="#1976D2")
        self.after(100, lambda: button.configure(fg_color=original_fg))
    
    def generate_query(self):
        """Generate Google search query"""
        # Get search text
        search_text = self.search_entry.get("1.0", "end-1c").strip()
        
        if not search_text or search_text == "Your Query Here":
            self.status_bar.configure(text="⚠️ Please enter a search query")
            self.shake_widget(self.search_entry)
            return
        
        # Get file type
        filetype = self.selected_filetype.get()
        
        # Build query
        if filetype != "None":
            query = f"{search_text} filetype:{filetype}"
        else:
            query = search_text
        
        # Update output
        self.output_box.configure(state="normal")
        self.output_box.delete("1.0", "end")
        self.output_box.insert("1.0", query)
        self.output_box.configure(state="disabled")
        
        self.generated_query.set(query)
        
        # Animate success
        self.animate_success(self.btn_generate)
        self.status_bar.configure(text="✓ Query generated successfully!")
    
    def clear_query(self):
        """Clear all inputs and outputs"""
        # Animate clearing
        self.shake_widget(self.search_entry)
        
        self.after(200, lambda: self.search_entry.delete("1.0", "end"))
        self.after(200, lambda: self.search_entry.insert("1.0", "Your Query Here"))
        
        self.output_box.configure(state="normal")
        self.output_box.delete("1.0", "end")
        self.output_box.configure(state="disabled")
        
        self.selected_filetype.set("None")
        self.generated_query.set("")
        
        self.status_bar.configure(text="Cleared all fields")
    
    def search_query(self):
        """Open Google search in browser"""
        query = self.generated_query.get()
        
        if not query:
            self.generate_query()
            query = self.generated_query.get()
        
        if query:
            encoded_query = quote_plus(query)
            url = f"https://www.google.com/search?q={encoded_query}"
            webbrowser.open(url)
            
            self.animate_success(self.btn_search)
            self.status_bar.configure(text="🌐 Opened in browser")
        else:
            self.status_bar.configure(text="⚠️ No query to search")
    
    def copy_query(self):
        """Copy query to clipboard"""
        query = self.generated_query.get()
        
        if not query:
            self.generate_query()
            query = self.generated_query.get()
        
        if query:
            try:
                pyperclip.copy(query)
                self.animate_success(self.btn_copy)
                self.status_bar.configure(text="📋 Copied to clipboard!")
                
                # Show "Copied!" tooltip
                self.show_copied_tooltip()
            except Exception as e:
                # Fallback to tkinter clipboard
                self.clipboard_clear()
                self.clipboard_append(query)
                self.status_bar.configure(text="📋 Copied to clipboard!")
        else:
            self.status_bar.configure(text="⚠️ No query to copy")
    
    def show_copied_tooltip(self):
        """Show temporary 'Copied!' message"""
        tooltip = ctk.CTkLabel(
            self,
            text="Copied!",
            font=ctk.CTkFont(size=16, weight="bold"),
            fg_color="#4CAF50",
            corner_radius=10
        )
        tooltip.place(relx=0.5, rely=0.5, anchor="center")
        self.after(1000, tooltip.destroy)
    
    def animate_success(self, button):
        """Success animation for buttons"""
        original_fg = button.cget("fg_color")
        button.configure(fg_color="#4CAF50")
        self.after(200, lambda: button.configure(fg_color=original_fg))
    
    def shake_widget(self, widget):
        """Shake animation for widget"""
        original_x = widget.winfo_x()
        def shake(step):
            if step < 4:
                offset = 5 if step % 2 == 0 else -5
                self.after(50, lambda: shake(step + 1))
        shake(0)


def main():
    """Main entry point"""
    app = ModernGoogleDorkTool()
    app.mainloop()


if __name__ == "__main__":
    main()