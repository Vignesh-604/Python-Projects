import tkinter
import customtkinter as ct
from pytube import YouTube, helpers
import os
import threading
# import time                                                            # Used for testing only

# To use the values across multiple functions
ytLink = ""
vid = ""
video = ""

# To Check if video exists
def check():
    global ytLink, vid
    try:
        # time_start = time.perf_counter()
        ytLink = link.get()
        vid = YouTube(ytLink)
        status.configure(text=f"{vid.title}\n\n{vid.author}", text_color="white")   # Gives title and creator of video

        if vid.age_restricted:
            status.configure(text="Video is age restricted. Can not download.")     # Cannot download age-restricted videos
        else:
            framebox.grid(row=3, columnspan = 2, ipadx=18, ipady=5)         # If video exists, the frame containing download btn and
            down.grid(row=1, column=0, padx=12, pady=12, ipady=5)           # Resultion drop down menu btn appears
            optmenu.grid(row=1,column=1, padx=12, pady=12, ipady=5)
            bottom.grid(row=2,columnspan=2,padx=5, sticky="s")

            # time_stop = time.perf_counter()
            # print(str(time_stop - time_start)[0:3])
    except:
        framebox.grid(row=3, columnspan = 2, ipadx=18, ipady=5)         # Frame with Invalid URL msg
        status.configure(text="Invalid URL")

# Resets everything
def reset():                                                            # Removes the link and video details
    link.delete(0, len(link.get()))
    status.configure(text="")
    framebox.grid_forget()                                              # Removes the frame with download and Resolution btns


path = os.path.expanduser("~") +"\\Downloads\\"        # Gives the path of the Downloads folder (.expanduser("~") gives user's home directory)

# To download the video
def startDownload():
    status.configure(text="Downloading...")
    down.grid_forget()                                          # Hides the download and dropdown menu while downloading 
    optmenu.grid_forget()
    bottom.grid_forget()

    def download():
        try:
            global video, vid
            option = optmenu.get()                                      # Gets selected option from Option menu
            if option == "Audio (MP3)":
                video = vid.streams.filter(only_audio=True).first()     # Gets the first stream with audio only feature
                title = helpers.safe_filename(vid.title)+".mp3"         # This function converts the title into a safe filename format
                                                                        # Using regex to remove ?,",<,>,',etc
                video.download(path, title)                 # Title + ".mp3" format converts the file into an mp3 file from any other format
            else:
                if option == "High":
                    video = vid.streams.get_highest_resolution()        # Highest re (720p)
                else:
                    video = vid.streams.get_lowest_resolution()         # Lowest res (360p)
                video.download(path)                                                # File will be in mp4 format
    
        except Exception as e:
            # print(e)
            status.configure(text=f"Download Error\n\n{vid.title}. ID:{e}", text_color="#FF3131")

        else:
            status.configure(text="Downloaded!!", text_color="lime")

    download_thread = threading.Thread(target=download)     # The download function works on a different thread so that the
    download_thread.start()                                 # GUI loop doesn't get interrupted (GUI crashes if not)

# System
ct.set_appearance_mode("Dark")                                      # GUI box theme
ct.set_default_color_theme("green")                                 # Theme color for widgets

# App frame
app = ct.CTk()
app.geometry("450x380")
app.title("YouTube Downloader")
app.resizable(False, False)                                         # Window resize False

# Window icon
try:
    iconpath = os.path.dirname(__file__)                 # Gives the path of directory of the current file
    pic = iconpath + "\\YTlogo.ico"                      # The picture has to be .ico file to change the window icon (topleft)
    print(pic)
    app.iconbitmap(pic)
except:
    pass                                                    # If error in finding img file, it'll show tkinter icon

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
down = ct.CTkButton(framebox,text="Download", command=startDownload, font=("Arial", 15, "bold"))

# Resolution select box
video_resolutions = ["High", "Low", "Audio (MP3)"]
opt_var = tkinter.StringVar()
opt_var.set(video_resolutions[0])                                   # Dropdown menu shows first available resolution as default
optmenu = ct.CTkOptionMenu(framebox, variable=opt_var, values=video_resolutions,
                            anchor="center", font=("Arial", 15, "bold"))            # Anchor=center : centers the text

# Bottom Label
bottom = ct.CTkLabel(framebox, text="-- Please select the desired video quality --\n-- or Audio only (MP3) version --",
                      font=("Arial", 15), wraplength=300)

# # Testing
# def testurl():
#     example_url = "https://youtu.be/weTotAPorpY?si=PE2GC1kZI7saNreI"
#     link.insert(0, example_url)
# test = ct.CTkButton(app, text="Test", command=testurl, font=("Arial", 15, "bold"))
# test.grid(row=4, columnspan=2)

# Dynamic spacing between columns  *(Centers the widgets)*
app.grid_columnconfigure((0,1), weight=1)                       # Columns expand proportionally to window resize
framebox.grid_columnconfigure((0,1), weight=1)
app.mainloop()
