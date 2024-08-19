import os
import tkinter
from tkinter import filedialog

tkinter.Tk().withdraw()

# Ask for the source location
source_location = filedialog.askdirectory(title="Select the source folder you want to copy (root folder is not copied, only contents)")

# Ask for the destination location
destination_location = filedialog.askdirectory(title="Select the destination folder").replace("/", "\\")

print(f"running: robocopy {source_location} {destination_location} /MIR /XJ /NDL /E /Z /R:5 /W:5 /TEE")
os.system(f"robocopy {source_location} {destination_location} /MIR /XJ /NDL /E /Z /R:5 /W:5 /TEE")


print("Done!")
input("Press Enter to exit...")