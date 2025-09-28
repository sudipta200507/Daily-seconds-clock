import tkinter as tk
import random
from datetime import datetime, timedelta
import winsound  # For tick sound (Windows only)

# Motivational quotes
quotes = [
    "🚀 Time is your most valuable asset.",
    "📚 Learn today, lead tomorrow.",
    "💻 Code now, success later.",
    "🔥 Don’t waste time, create it!",
    "🎯 Focus on progress, not perfection.",
    "⌛ Every second counts. Make it matter."
]


def update_clock():
    now = datetime.now()
    tomorrow = (now + timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0)
    remaining_seconds = int((tomorrow - now).total_seconds())

    # Update text
    label.config(text=f"{remaining_seconds:,}\nsec left today")

    # Progress %
    percent_used = (86400 - remaining_seconds) / 86400 * 100
    percent_label.config(text=f"Day {percent_used:.2f}% done")

    # Change colors based on urgency
    if percent_used < 50:
        color = "#00ffcc"  # calm green
    elif percent_used < 70:
        color = "#ffaa00"  # warning yellow
    else:
        color = "#ff4444"  # urgent red

    label.config(fg=color)

    # Draw circular progress
    canvas.delete("arc")
    angle = int((remaining_seconds / 86400) * 360)
    canvas.create_arc(20, 20, 280, 280, start=90, extent=-angle, outline=color,
                      width=20, style="arc", tags="arc")

    # Tick sound
    winsound.Beep(1000, 80)  # 1000 Hz, 80 ms

    # Update every second
    root.after(1000, update_clock)


# GUI Setup
root = tk.Tk()
root.title("⚡ Daily Seconds Clock ⚡")
root.geometry("400x450")
root.configure(bg="#0d1117")

# Title
title = tk.Label(root, text="⏳ Use Your Time Wisely ⏳", font=("Arial", 16, "bold"), fg="#ffcc00", bg="#0d1117")
title.pack(pady=10)

# Canvas for circular progress
canvas = tk.Canvas(root, width=300, height=300, bg="#0d1117", highlightthickness=0)
canvas.pack()

# Countdown Label (center of circle)
label = tk.Label(root, font=("Consolas", 20, "bold"), fg="#00ffcc", bg="#0d1117", justify="center")
label.place(x=110, y=160)

# Percent Label
percent_label = tk.Label(root, font=("Arial", 14), fg="#ffaa00", bg="#0d1117")
percent_label.pack(pady=10)

# Random motivational quote
quote_label = tk.Label(root, text=random.choice(quotes), font=("Arial", 12, "italic"), fg="#cccccc", bg="#0d1117")
quote_label.pack(pady=10)

update_clock()
root.mainloop()
