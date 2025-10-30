import tkinter as tk
from tkinter import font as tkfont

class MotivationalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To: Amber ✨")
        self.root.geometry("600x500")
        self.root.config(bg="#FFF0F5")
        
        # Motivational quotes
        self.quotes = [
            "I know you're not feeling well, but you can do it!",
            "This too shall pass. Stay strong!",
            "Believe in yourself. You're capable of more than you think.",
            "Hard times don't last, but tough people do.",
            "Keep going, even when it feels tough. You are stronger than you know.",
            "Remember, you're amazing, and you can handle anything that comes your way.",
            "So take care, and remember you're not alone.",
            "And if you ever feel lonely, just know I'm always here for you."
        ]
        
        self.current_index = 0
        self.showing_final = False
        
        # Create custom fonts
        self.title_font = tkfont.Font(family="Arial", size=22, weight="bold")
        self.quote_font = tkfont.Font(family="Georgia", size=16)
        self.button_font = tkfont.Font(family="Arial", size=12, weight="bold")
        
        self.setup_ui()
        
    def setup_ui(self):
        # Title label
        self.title_label = tk.Label(
            self.root,
            text="💖 To: Amber 💖",
            font=self.title_font,
            bg="#FFF0F5",
            fg="#FF1493"
        )
        self.title_label.pack(pady=(0, 20))
        
        # Quote card frame
        self.card_frame = tk.Frame(
            self.root,
            bg="#FFE4E1",
            relief="raised",
            bd=3
        )
        self.card_frame.pack(pady=20, padx=20, fill="both", expand=True)
        
        # Quote label
        self.quote_label = tk.Label(
            self.card_frame,
            text=self.quotes[0],
            font=self.quote_font,
            bg="#FFE4E1",
            fg="#8B008B",
            wraplength=500,
            justify="center",
            pady=40,
            padx=30
        )
        self.quote_label.pack(expand=True)
        
        # Button frame
        self.button_frame = tk.Frame(self.root, bg="#FFF0F5")
        self.button_frame.pack(pady=10)
        
        # Next/OK button
        self.next_button = tk.Button(
            self.button_frame,
            text="Next →",
            font=self.button_font,
            command=self.show_next,
            bg="#FF69B4",
            fg="white",
            relief="flat",
            padx=30,
            pady=10,
            cursor="hand2"
        )
        self.next_button.pack()
        
        # Add hover effects
        self.add_button_hover(self.next_button, "#FF1493", "#FF69B4")
        
        # Footer label
        self.footer_label = tk.Label(
            self.root,
            text="You are loved and supported! 💕",
            font=("Arial", 9, "italic"),
            bg="#FFF0F5",
            fg="#DB7093"
        )
        self.footer_label.pack(pady=(10, 0))
        
    def add_button_hover(self, button, hover_color, normal_color):
        """Add hover effect to buttons"""
        button.bind("<Enter>", lambda e: button.config(bg=hover_color))
        button.bind("<Leave>", lambda e: button.config(bg=normal_color))
        
    def show_next(self):
        """Show the next quote or final message"""
        if self.showing_final:
            self.root.quit()
            return
            
        if self.current_index < len(self.quotes) - 1:
            self.current_index += 1
            self.quote_label.config(text=self.quotes[self.current_index])
        else:
            self.show_final_message()
            
    def show_final_message(self):
        """Show the final completion message"""
        self.showing_final = True
        
        # Update the quote to show final message
        self.quote_label.config(
            text="🌟 You've made it through the journey! 🌟\n\n"
                 "Stay strong, you're amazing!\n\n"
                 "Remember these words whenever you need them.",
            font=("Georgia", 16, "bold")
        )
        
        # Change button to exit
        self.next_button.config(text="OK", command=self.show_next)

# Create and run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = MotivationalApp(root)
    root.mainloop()
