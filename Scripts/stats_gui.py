# =============Libraries=============
import tkinter as tk
from tkinter import ttk
from tkcalendar import *
import Scripts.functions as fun

# =============GUI Section=============

# ----Statistics Section----


def stats(frame, check_username):
    """stats_win = tk.Toplevel()
    stats_win.title("Statistics")
    stats_win.config(bg="#333333")
    #stats_win.geometry("250x200")
    frame = tk.Frame(stats_win, bg="#333333")"""

    # Clear the frame first
    fun.clear_frame(frame)

    """canvas = tk.Canvas(frame, bg="#333333", height=550, width=500)
    widget_frame = tk.Frame(canvas, bg="#333333")

    # ----Scrollbar----
    vert_scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=canvas.yview)
    hori_scrollbar = ttk.Scrollbar(frame, orient=tk.HORIZONTAL, command=canvas.xview)

    # +++Bindings/Configure canvas+++
    canvas.bind("<Configure>", lambda event: canvas.configure(scrollregion=canvas.bbox('all')))

    canvas.configure(yscrollcommand=vert_scrollbar.set)
    canvas.configure(xscrollcommand=hori_scrollbar.set)

    # +++Create canvas+++
    canvas.create_window((0, 0), window=widget_frame, anchor="nw")"""

    # ---- Widgets ----
    header_lbl = tk.Label(
        frame, text="Statistics", bg="#333333", fg="#ffffff", font=("Arial", 18)
    )

    txt_bx = tk.Text(frame, width=48, height=25, wrap="word", font=("Arial", 11))

    vert_scroll = ttk.Scrollbar(frame, orient="vertical", command=txt_bx.yview)
    horizon_scroll = ttk.Scrollbar(frame, orient="horizontal", command=txt_bx.xview)

    graph_btn = tk.Button(
        frame,
        text="Plot graph",
        width=15,
        font=("Arial, 12"),
        bg="#46a094",
        fg="#ffffff",
        command=lambda: fun.plot_graph(check_username),
    )
    """gen_report_btn = tk.Button(
        frame,
        text="Generate report",
        width=15,
        font=("Arial", 12),
        bg="#46a094",
        fg="#ffffff",
        command= lambda: fun.generate_report(check_username, txt_bx)
    )"""

    # ----- Populate Textbox ----

    fun.display_stats(txt_bx)
    txt_bx.config(state=tk.DISABLED)

    # ---- Grid ----
    header_lbl.grid(row=0, column=0, columnspan=4, pady=30, sticky="news")

    txt_bx.grid(row=1, column=2, rowspan=8, columnspan=2, sticky="nw")
    vert_scroll.grid(row=1, column=4, rowspan=8, sticky="ns")
    # horizon_scroll.grid(row=9, column=2, columnspan=2, sticky="ew")

    graph_btn.grid(row=9, column=2, pady=5, sticky="ew")

    # ---- Scrollbar ----
    txt_bx["yscrollcommand"] = vert_scroll.set
    txt_bx["xscrollcommand"] = horizon_scroll.set

    # ---- Pack Layout ----
    # canvas.pack(side='left', fill='both', expand=True)
    # canvas.configure(height=450, width=400)
    # vert_scrollbar.pack(side='left', fill='y')
    # hori_scrollbar.pack(side='bottom', fill='x')

    # ---- Canvas Layout ----
    """canvas.grid(row=0, column=0, sticky="ew")
    vert_scrollbar.grid(row=0, column=1, sticky='ns')
    hori_scrollbar.grid(row=1, column=0, sticky='ew')"""
