import tkinter
import customtkinter as ct
from pytube import YouTube
#import time                                                            # Used for testing only

# To Check if video exists
def check():
    try:
        # time_start = time.perf_counter()
        ytLink = link.get()
        vid = YouTube(ytLink)
        status.configure(text=f"{vid.title}\n\n{vid.author}", text_color="white")   # Gives title and creator of video
        res(vid)
    except:
        framebox.grid(row=3, columnspan = 2, ipadx=18, ipady=5)
        status.configure(text="Invalid URL")
    else:
        framebox.grid(row=3, columnspan = 2, ipadx=18, ipady=5)         # If video exists, the frame containing download btn and
        down.grid(row=1, column=0, padx=12, pady=12, ipady=5)           # Resultion drop down menu btn appears
        optmenu.grid(row=1,column=1, padx=12, pady=12, ipady=5)
        # time_stop = time.perf_counter()
        # print(str(time_stop - time_start)[0:3])

# Resets everything
def reset():                                                            # Removes the link and video details
    link.delete(0, len(link.get()))
    status.configure(text="")
    framebox.grid_forget()                                              # Removes the frame with download and Resolution btns
    down.grid_forget()
    optmenu.grid_forget()

# To get the required resolution
video_resolutions = ["360p", "720p"]                        # Downloading any other resolution doesn't provide any audio
def res(vid):
    # video_resolutions = []                                              # Empties the resolution list
    # for stream in vid.streams.order_by('resolution'):                   # Loops through video resolutions in ascending order
    #     if stream.resolution in video_resolutions:                      # To avoid repetition of resolution options
    #         continue
    #     else:
    #         video_resolutions.append(stream.resolution)
    opt_var.set(video_resolutions[0])                                   # Dropdown menu shows first available resolution as default
    optmenu.configure(values=video_resolutions)                         # Gives the resolution list to the dropdown menu

# To download the video
def download():
    try:
        ytLink = link.get()
        vid = YouTube(ytLink)
        video = vid.streams.filter(res=optmenu.get()).first()           # Filters by the resolution selected in dropdown
        video.download()                                                # and selects the first available option.
    except:
        print("YouTube link is invalid!")
        status.configure(text="Download Error", text_color="red")
        down.grid_forget()                                              # Hides the download and dropdown menu if download error
        optmenu.grid_forget()

    else:
        status.configure(text="Downloaded", text_color="lime")
        print("Download Complete!!")
        down.grid_forget()                                              # Hides the download and dropdown menu after download
        optmenu.grid_forget()


# System
ct.set_appearance_mode("Dark")                                      # GUI box theme
ct.set_default_color_theme("green")                                 # Theme color for buttons

# App frame
app = ct.CTk()
app.geometry("450x380")
app.title("YouTube Downloader")
app.resizable(False, False)                                         # Window resize

# Window icon (Enter path of the given YTlogo.ico image)
# pic = ""
# app.iconbitmap(default=pic)                               # The picture has to be .ico file to change the window icon (topleft)

# UI Elements
title = ct.CTkLabel(app, text="Insert a YouTube Link", font=("Arial", 22, "bold"))
title.grid(row=0, columnspan=2, pady=10)

# Entry box
url_var =tkinter.StringVar()
link = ct.CTkEntry(app, width=370, height=40, textvariable=url_var, font=("Arial", 15))
link.grid(row=1, columnspan=2)

# Check for video button
checkLink = ct.CTkButton(app,text="Check for Video", command=check, font=("Arial", 15, "bold"))
checkLink.grid(row=2, column=0,padx=10, pady=15, ipady=5)

# Clears the entry box
resetLink = ct.CTkButton(app,text="Reset", command=reset, font=("Arial", 15, "bold"))
resetLink.grid(row=2, column=1,padx=10, pady=15, ipady=5)

# Frame for video details
framebox = ct.CTkFrame(app)

# Status label (Video title & creator, download status)
status = ct.CTkLabel(framebox, text="", font=("Arial", 15), wraplength=300)         # Word wrap after given width
status.grid(row=0, columnspan=2,padx=10, pady=10)

# Download button
down = ct.CTkButton(framebox,text="Download", command=download, font=("Arial", 15, "bold"))

# Resolution select box
opt_var = tkinter.StringVar()
optmenu = ct.CTkOptionMenu(framebox, variable=opt_var, values=video_resolutions,
                            anchor="center", font=("Arial", 15, "bold"))            # Anchor=center : centers the text

# Testing
# def testurl():
#     example_url = "https://youtu.be/weTotAPorpY?si=PE2GC1kZI7saNreI"
#     link.insert(0, example_url)
# test = ct.CTkButton(app, text="Test", command=testurl, font=("Arial", 15, "bold"))
# test.grid(row=4, columnspan=2)

# Dynamic spacing between columns  *(Centers the widgets)*
app.grid_columnconfigure((0,1), weight=1)                       # Columns expand proportionally to window resize
framebox.grid_columnconfigure((0,1), weight=1)
app.mainloop()
