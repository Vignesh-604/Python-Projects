# YouTube Videos Downloader GUI

Clone the repository to get the exe file [Pytube_GUI-V2.exe](https://github.com/Vignesh-604/Python-Projects/blob/main/Yt%20Videos%20Downloader/Pytube_GUI-V2.exe) (Entire project in single executable file or app)   

This subfolder contains the python script to create a GUI to download videos in 720p,360p or only audio (MP3) version of the video. The script uses the tkinter and [customtkinter](https://github.com/TomSchimansky/CustomTkinter) to create the GUI window and it's widgets and the [Pytube](https://github.com/pytube/pytube) library to download videos. Also uses 'os' for file path requirements and threading for multithreading task.

Issues I had in version 1 which got fixed in version 2:  
-- **Added MP3** (By downloading only_audio file and changing extension to .mp3)  
-- **Fixed icon for root window** (Icon should be placed in the same directory)   
-- **GUI crashing while downloading**: While downloading the video, the mainloop for tkinter window was being interrupted causing it to crash so I placed the download function in thread so that it doesn't interrupt with the GUI loop and downloads simultaneously.   
