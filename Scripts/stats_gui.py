# =============Libraries=============
import tkinter as tk
from tkinter import ttk
from tkcalendar import *
import Scripts.functions as fun

# =============GUI Section=============

# ----Statistics Section----


def stats(frame, check_username):

    '''stats_win = tk.Toplevel()
    stats_win.title("Statistics")
    stats_win.config(bg="#333333")
    #stats_win.geometry("250x200")
    frame = tk.Frame(stats_win, bg="#333333")'''

    # Clear the frame first
    fun.clear_frame(frame)

    # ---- Widgets ----
    header_lbl = tk.Label(
        frame, text="Statistics", bg="#333333", fg="#ffffff", font=("Arial", 18)
    )

    txt_bx = tk.Text(frame, width=48, height=25, wrap="word", font=("Arial", 10))

    vert_scroll = ttk.Scrollbar(frame, orient="vertical", command=txt_bx.yview)
    horizon_scroll = ttk.Scrollbar(frame, orient="horizontal", command=txt_bx.xview)

    gen_report_btn = tk.Button(
        frame,
        text="Generate report",
        width=15,
        font=("Arial", 12),
        bg="#46a094",
        fg="#ffffff",
        command= lambda: fun.generate_report(check_username, txt_bx)
    )

    # ----- Populate Textbox ----
    
    fun.display_stats(txt_bx)
    txt_bx.config(state=tk.DISABLED)

    # ---- Grid ----
    header_lbl.grid(row=0, column=0, columnspan=4, pady=10, sticky="ew")

    txt_bx.grid(row=1, column=2, rowspan=8, columnspan=2, sticky="ew")
    vert_scroll.grid(row=1, column=4, rowspan=8, sticky="ns")
    horizon_scroll.grid(row=9, column=2, columnspan=2, sticky="ew")

    # ---- Scrollbar ----
    txt_bx["yscrollcommand"] = vert_scroll.set
    txt_bx["xscrollcommand"] = horizon_scroll.set
