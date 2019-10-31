
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: n10214453
#    Student name: Zachary Nicoll
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  Submitted files will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Assignment Description-----------------------------------------#
#
#  What's On?: Online Entertainment Planning Application
#
#  In this assignment you will combine your knowledge of HTMl/XML
#  mark-up languages with your skills in Python scripting, pattern
#  matching, and Graphical User Interface design to produce a useful
#  application for planning an entertainment schedule.  See
#  the instruction sheet accompanying this file for full details.
#
#--------------------------------------------------------------------#



#-----Imported Functions---------------------------------------------#
#
# Below are various import statements for helpful functions.  You
# should be able to complete this assignment using these
# functions only.  Note that not all of these functions are
# needed to successfully complete this assignment.

# The function for opening a web document given its URL.
# (You WILL need to use this function in your solution,
# either directly or via our "download" function.)
from urllib.request import urlopen

# Import the standard Tkinter functions. (You WILL need to use
# these functions in your solution.  You may import other widgets
# from the Tkinter module provided they are ones that come bundled
# with a standard Python 3 implementation and don't have to
# be downloaded and installed separately.)
from tkinter import *
from tkinter import messagebox

# Functions for finding all occurrences of a pattern
# defined via a regular expression, as well as
# the "multiline" and "dotall" flags.  (You do NOT need to
# use these functions in your solution, because the problem
# can be solved with the string "find" function, but it will
# be difficult to produce a concise and robust solution
# without using regular expressions.)
from re import findall, finditer, MULTILINE, DOTALL

# Import the standard SQLite functions (just in case they're
# needed one day).
from sqlite3 import *

#
#--------------------------------------------------------------------#



#-----Downloader Function--------------------------------------------#
#
# This is our function for downloading a web page's content and both
# saving it as a local file and returning its source code
# as a Unicode string. The function tries to produce
# a meaningful error message if the attempt fails.  WARNING: This
# function will silently overwrite the target file if it
# already exists!  NB: You should change the filename extension to
# "xhtml" when downloading an XML document.  (You do NOT need to use
# this function in your solution if you choose to call "urlopen"
# directly, but it is provided for your convenience.)
#
def download(url = 'http://www.wikipedia.org/',
             target_filename = 'download',
             filename_extension = 'html'):

    # Import an exception raised when a web server denies access
    # to a document
    from urllib.error import HTTPError

    # Open the web document for reading
    try:
        web_page = urlopen(url)
    except ValueError:
        raise Exception("Download error - Cannot find document at URL '" + url + "'")
    except HTTPError:
        raise Exception("Download error - Access denied to document at URL '" + url + "'")
    except:
        raise Exception("Download error - Something went wrong when trying to download " + \
                        "the document at URL '" + url + "'")

    # Read its contents as a Unicode string
    try:
        web_page_contents = web_page.read().decode('UTF-8')
    except UnicodeDecodeError:
        raise Exception("Download error - Unable to decode document at URL '" + \
                        url + "' as Unicode text")

    # Write the contents to a local text file as Unicode
    # characters (overwriting the file if it
    # already exists!)
    try:
        text_file = open(target_filename + '.' + filename_extension,
                         'w', encoding = 'UTF-8')
        text_file.write(web_page_contents)
        text_file.close()
    except:
        raise Exception("Download error - Unable to write to file '" + \
                        target_file + "'")

    # Return the downloaded document to the caller
    return web_page_contents

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#

###### Websites Used ######
# 1. https://www.songkick.com/metro_areas/26778-australia-brisbane#date-filter-form -> Upcoming concerts
# 2. https://www.fandango.com/moviescomingsoon-> Upcoming movies
# 3. https://www.mightyape.com.au/books/coming-soon -> Upcoming book releases
##########################

concerts_url = "https://www.songkick.com/metro_areas/26778-australia-brisbane#date-filter-form"
movies_url = "https://www.fandango.com/moviescomingsoon"
books_url  = "https://www.mightyape.com.au/books/coming-soon"

HTML_PLANNER_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>HUB Planner - Upcomming Music, Movies, and Books.</title>
    <link href="https://fonts.googleapis.com/css?family=Open+Sans" rel="stylesheet">

    <style type="text/css">
        html, body {
        font-family: "Open Sans";
        padding: 0px;
        border: none;
        margin: 0px;
        background-color: mintcream;
        }

        hr {
            width: 85%;
            height: 2px;
            background-color: black;
            border: none;
        }

        table {
            width: 100%;
            text-align: center;
        }

        td {
            height: 300px;
            width: 50%;
            background: no-repeat;
            background-position: center;
            max-width: 100px; 
            word-wrap: break-word;
            vertical-align: bottom;
            background-size: cover;
        }

        #title div{
            display: block;
            width: 100%;

        }

        #title img{
            padding-top: 30px;
            padding-bottom: 30px;
            margin-left: auto;
            margin-right: auto;
            display: block;
        }

        .container {
            display: block;
            width: 50%;
            padding: 2px;
            background-color: none;
            margin-left: auto;
            margin-right: auto;
        }

        .container th{
            color: black;
            font-size: 36px;
            font-weight: lighter;
            background-color: seagreen;
        }

        .container td{
            color: black;
        }

        .container td div{
            background-color: white;
        }
        
        .container img{
            z-index: 1; 
            position: absolute; 
        }
    </style>


</head>

<body>
    <div id="title">
        <img src="https://i.ibb.co/98FP2wK/HUBWeb-Logo.png" alt="HUBWeb-Logo" border="0">
    </div>

    <hr>

    <!--Upcoming Concerts-->
    <div class="container">
        <div style="background-color: white;">
            <table>
                <thead>
                    <tr>
                        <th colspan="2">Upcoming Concerts</th>
                    </tr>
                </thead>
                <tbody>
                    <!--INSERTCONCERTS-->
                </tbody>
            </table>
        </div>
    </div>

    <hr>

    <!--Upcoming Movies-->
    <div class="container">
        <div style="background-color: white;">
            <table>
                <thead>
                    <tr>
                        <th colspan="2">Upcoming Movies</th>
                    </tr>
                </thead>
                <tbody>
                    <!--INSERTMOVIES-->
                </tbody>
            </table>
        </div>  
    </div>

    <hr>

    <!--Upcoming Books-->
    <div class="container">
        <div style="background-color: white;">
            <table>
                <thead>
                    <tr>
                        <th colspan="2">Upcoming Books</th>
                    </tr>
                </thead>
                <tbody>
                    <!--INSERTBOOKS-->
                </tbody>
            </table>
        </div>  
    </div>
    



    <hr>
    <div>
        <p style="text-align: center;">This information was sourced from the following wesbites:
            <br>
            <a href="https://www.songkick.com/metro_areas/26778-australia-brisbane#date-filter-form">https://www.songkick.com/metro_areas/26778-australia-brisbane#date-filter-form</a>
            <br>
            <a href="https://www.fandango.com/moviescomingsoon">https://www.fandango.com/moviescomingsoon</a>
            <br>
            <a href="https://www.mightyape.com.au/books/coming-soon">https://www.mightyape.com.au/books/coming-soon</a>
        </p>    
    </div>
    

</body>
</html>
"""

# Make a copy of the original HTML to preserve the template.
HTML_PLANNER = HTML_PLANNER_TEMPLATE


###########################################
#-------------------GUI-------------------#
###########################################

# Create a class of Tkinter Button that changes colour when the mouse hovers over it.
class HoverButton(Button):
    def __init__(self, master, **kw):
        Button.__init__(self,master=master,**kw)
        self.defaultBackground = self["background"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self['background'] = self['activebackground']

    def on_leave(self, e):
        self['background'] = self.defaultBackground

# Main Tkinter window.
class MainGUI(Tk):
    def __init__(self):
        # Setup window.
        super().__init__()
        self.title("HUB - Upcoming concerts, movies, and books.")
        self.geometry("1400x900")

        # Create empty list that will store all of the selected (exported) events.
        self.EXPORT_LIST = []

        # Utilise three frames (main, top, and bottom) for organising the GUI.
        main_frame = Frame(self, width=1400, height=900)
        main_frame.grid(row=0, column=0)

        top_frame = Frame(main_frame, width=1400, height=300)
        top_frame.grid(row=0,column=0)

        bottom_frame = Frame(main_frame, width=1400, height=600, bg="black")
        bottom_frame.grid(row=1,column=0)

        # Create a canvas widget to display the title logo.
        logo_canvas = Canvas(top_frame, width=1400, height=300, highlightthickness=0, bg="#F6F6F6")
        logo_canvas.pack()
        self.logo = PhotoImage(file=".\\images\\HUBLogo.png")
        logo_canvas.create_image(700,160, image=self.logo)
        
        # Create labels for each of the event buttons and place them in GUI using grid().
        concert_l = Label(bottom_frame, text="CONCERTS", font=('Calibri Bold', '24'), bg="#F6F6F6")
        movie_l = Label(bottom_frame, text="MOVIES", font=('Calibri Bold', '24'), bg="#F6F6F6")
        book_l = Label(bottom_frame, text="BOOKS", font=('Calibri Bold', '24'), bg="#F6F6F6")

        concert_l.grid(row=0, column=0, columnspan=2, sticky='ew', pady=5)
        movie_l.grid(row=0, column=2, columnspan=2, sticky='ew', pady=5)
        book_l.grid(row=0, column=5, columnspan=2, sticky='ew', pady=5)

        # Store the button images in variables
        self.concert_logo = PhotoImage(file=".\\images\\ticket.png")
        self.movie_logo = PhotoImage(file=".\\images\\movies.png")
        self.book_logo = PhotoImage(file=".\\images\\books.png")

        # Create 3 HoverButtons (custom button class) and apply corresponding images.
        concert_button = HoverButton(bottom_frame, image=self.concert_logo, width=464, height=450, bd=0, bg="#F6F6F6", activebackground="#6dcff6", command=lambda:self.music_window())
        movie_button = HoverButton(bottom_frame, image=self.movie_logo, width=464, height=450, bd=0, bg="#F6F6F6", activebackground="#6dcff6", command=lambda:self.movie_window())
        book_button = HoverButton(bottom_frame, image=self.book_logo, width=464, height=450, bd=0, bg="#F6F6F6", activebackground="#6dcff6", command=lambda:self.book_window())

        concert_button.grid(row=1,column=0, columnspan=2)
        movie_button.grid(row=1,column=2, columnspan=2)
        book_button.grid(row=1,column=5, columnspan=2)

        # Create variable for storing state of the 'offline mode' button.
        self.offline_state = StringVar()
        self.offline_state.set("Offline Mode On")
        # Assign variable to 'offline mode' button.
        self.offline_btn = Button(bottom_frame, textvariable=self.offline_state, font=('Calibri Light', '20'), bd=0, bg="lime", height=2, command=lambda:self.offline_online())
        self.offline_btn.grid(row=2, column=0, sticky='nesw')
        
        # Create variable for storing state of the 'export database' button.
        self.db_state = StringVar()
        self.db_state.set("Database Export On")
        # Assign variable to 'export database' button.
        self.db_btn = Button(bottom_frame, textvariable=self.db_state, font=('Calibri Light', '20'), bd=0, bg="lime", height=2, command=lambda:self.db_on_off())
        self.db_btn.grid(row=2, column=1, sticky='nesw')

        # Create button for resetting/emptying the planner file and event list.
        resetplanner_btn = Button(bottom_frame, text="Reset Planner", font=('Calibri Light', '24'), bd=0, bg="#6dcff6", height=2, command=lambda: self.reset_planner())
        resetplanner_btn.grid(row=2, column=2, columnspan=2, sticky='nesw')

        # Create button for exporting planner to HTML file.
        planner_btn = Button(bottom_frame, text="Export Planner", font=('Calibri Light', '24'), bd=0, bg="#82ca9c", height=2, command=lambda: generate_planner(self.EXPORT_LIST, HTML_PLANNER, self.db_state.get()))
        planner_btn.grid(row=2, column=5, columnspan=2, sticky='nesw')

    # Function for changing the state of the 'offline mode' button.
    # Color and text are changed.
    def offline_online(self):
        if(self.offline_state.get()=="Offline Mode Off"):
            self.offline_state.set("Offline Mode On")
            self.offline_btn['bg'] = 'lime'
        else:
            self.offline_state.set("Offline Mode Off")
            self.offline_btn['bg'] = 'red'

    # Function for changing the state of the 'export database' button.
    # Color and text are changed.
    def db_on_off(self):
        if(self.db_state.get()=="Database Export Off"):
            self.db_state.set("Database Export On")
            self.db_btn['bg'] = 'lime'
        else:
            self.db_state.set("Database Export Off")
            self.db_btn['bg'] = 'red'

    # Function for opening the 'Upcoming Concerts' window.
    def music_window(self):
        # If 'offline mode' is off, download the HTML page and get events.
        if(self.offline_state.get()=="Offline Mode Off"):
            self.event_list = get_upcoming_concerts(download(url = concerts_url, target_filename = 'download', filename_extension = 'html'))
        
        # Otherwise, use the archive file.
        else:
            web_page = open(".\\archive\\OFFLINE_CONCERTS.html", "r")
            web_page_contents = web_page.read()
            self.event_list = get_upcoming_concerts(web_page_contents)

        # Open 'Upcoming Concerts' window and hide the current window.
        ConcertGUI(self)
        self.withdraw()
    
    # Function for opening the 'Upcoming Movies' window.
    def movie_window(self):
        # If 'offline mode' is off, download the HTML page and get events.
        if(self.offline_state.get()=="Offline Mode Off"):
            self.event_list = get_upcoming_movies(download(url = movies_url, target_filename = 'download', filename_extension = 'html'))
        
        # Otherwise, use the archive file.
        else:
            web_page = open(".\\archive\\OFFLINE_MOVIES.html", "r")
            web_page_contents = web_page.read()
            self.event_list = get_upcoming_movies(web_page_contents)

        # Open 'Upcoming Movies' window and hide the current window.
        MovieGUI(self)
        self.withdraw()

    # Function for opening the 'Upcoming Books' window.
    def book_window(self):
        # If 'offline mode' is off, download the HTML page and get events.
        if(self.offline_state.get()=="Offline Mode Off"):
            self.event_list = get_upcoming_books(download(url = books_url, target_filename = 'download', filename_extension = 'html'))
        
        # Otherwise, use the archive file.
        else:
            web_page = open(".\\archive\\OFFLINE_BOOKS.html", "r")
            web_page_contents = web_page.read()
            self.event_list = get_upcoming_books(web_page_contents)
        
        # Open 'Upcoming Books' window and hide the current window.
        BookGUI(self)
        self.withdraw()

    # Function for resetting the planner and database. 
    def reset_planner(self):
        # Set export event list back to an empty list.
        self.EXPORT_LIST = []

        # Set the HTML planner back to the original template.
        HTML_PLANNER = HTML_PLANNER_TEMPLATE

        # Generate the planner/database with no events.
        generate_planner(self.EXPORT_LIST, HTML_PLANNER, self.db_state.get())

       
# 'Upcoming Concerts' window.
class ConcertGUI(Toplevel):
    def __init__(self, master):
        # Setup window.
        super().__init__()
        self.title("HUB - Upcoming concerts, movies, and books.")
        self.geometry("1400x900")
        main_frame = Frame(self, width=1400, bg="black")
        main_frame.pack(fill=BOTH, expand=1)
        
        title_l = Label(main_frame, text="UPCOMING CONCERTS", font=('Calibri Light', '36'), bg="#F6F6F6", height=3)
        title_l.grid(row=0, column=0, columnspan=3, sticky="ew")

        # Create two empty lists that store all the checkbuttons and their
        # corresponding values.
        self.chkbtn_list = [None]*10
        self.chkbtnvars_list = [None]*10

        # Generate 10 rows of checkbuttons with corresponding titles and dates.
        for row_num in range(10):
            # Set button variable at index row_num to a Tkinter boolean variable.
            self.chkbtnvars_list[row_num] = BooleanVar()

            # Set index row_num of the button list to a Checkbutton with corresponding variable
            # from the button variables list. 
            self.chkbtn_list[row_num]=Checkbutton(main_frame, bg="#F6F6F6", variable=self.chkbtnvars_list[row_num])
            self.chkbtn_list[row_num].grid(row=2+row_num, column=0, sticky="news", padx=1, pady=1)

            # Create two labels for the title and date of the event at index row_num of the current event list.
            Label(main_frame, text=self.master.event_list[row_num][1], bg="#F6F6F6", height=2, font=('Calibri Light', '16')).grid(row=2+row_num, column=1, sticky="news", padx=1, pady=1)
            Label(main_frame, text=self.master.event_list[row_num][2], bg="#F6F6F6", height=2, font=('Calibri Light', '16')).grid(row=2+row_num, column=2, sticky="news", padx=1, pady=1)

        # Add additional title labels for each column.
        selected_l = Label(main_frame, text="Select", font=('Calibri Bold', '20'), width=5, bg="#F6F6F6")
        selected_l.grid(row=1, column=0, padx=1, pady=1)
        concerts_l = Label(main_frame, text="Concert", font=('Calibri Bold', '20'), width=51, bg="#F6F6F6")
        concerts_l.grid(row=1, column=1, padx=1, pady=1)
        dates_l = Label(main_frame, text="Date", font=('Calibri Bold', '20'),width=43, bg="#F6F6F6")
        dates_l.grid(row=1, column=2, padx=1, pady=1)

        # Add button at the bottom of the screen to confirm selection and
        # return to home screen (via main_window()).
        confirm_btn = Button(main_frame, text="CONFIRM", font=('Calibri Bold', '28'), height=1, bg="lime", command=lambda: self.main_window())
        confirm_btn.grid(row = 13, column = 0, columnspan=3, sticky="EW")

    # Function for destroying current window and re-displaying the main window.
    # All selected events are also added to the 'export list'.
    def main_window(self):
        index = 0
        for chkbtn in self.chkbtn_list:
            # Check each checkbutton's variable; if it is checked (or True), then
            # add the corresponding event to the 'export list'.
            if(self.chkbtnvars_list[index].get()==True):
                self.master.EXPORT_LIST.append(self.master.event_list[index])
            index += 1
        
        # Destory current window and re-display main GUI.
        self.master.deiconify()
        self.destroy()

class MovieGUI(Toplevel):
    def __init__(self, master):
        # Setup window.
        super().__init__()
        self.title("HUB - Upcoming concerts, movies, and books.")
        self.geometry("1400x900")
        main_frame = Frame(self, width=1400, bg="black")
        main_frame.pack(fill=BOTH, expand=1)
        
        title_l = Label(main_frame, text="UPCOMING MOVIES", font=('Calibri Light', '36'), bg="#F6F6F6", height=3)
        title_l.grid(row=0, column=0, columnspan=3, sticky="ew")
       
        # Create two empty lists that store all the checkbuttons and their
        # corresponding values.
        self.chkbtn_list = [None]*10
        self.chkbtnvars_list = [None]*10

        # Generate 10 rows of checkbuttons with corresponding titles and dates.
        for row_num in range(10):
            # Set button variable at index row_num to a Tkinter boolean variable.
            self.chkbtnvars_list[row_num] = BooleanVar()

            # Set index row_num of the button list to a Checkbutton with corresponding variable
            # from the button variables list.  
            self.chkbtn_list[row_num] = Checkbutton(main_frame, bg="#F6F6F6", variable=self.chkbtnvars_list[row_num])
            self.chkbtn_list[row_num].grid(row=2+row_num, column=0, sticky="news", padx=1, pady=1)

            # Create two labels for the title and date of the event at index row_num of the current event list.
            Label(main_frame, text=self.master.event_list[row_num][1], bg="#F6F6F6", height=2, font=('Calibri Light', '16')).grid(row=2+row_num, column=1, sticky="news", padx=1, pady=1)
            Label(main_frame, text=self.master.event_list[row_num][2], bg="#F6F6F6", height=2, font=('Calibri Light', '16')).grid(row=2+row_num, column=2, sticky="news", padx=1, pady=1)

        # Add additional title labels for each column.
        selected_l = Label(main_frame, text="Select", font=('Calibri Bold', '20'), width=5, bg="#F6F6F6")
        selected_l.grid(row=1, column=0, padx=1, pady=1)
        concerts_l = Label(main_frame, text="Movie", font=('Calibri Bold', '20'), width=51, bg="#F6F6F6")
        concerts_l.grid(row=1, column=1, padx=1, pady=1)
        dates_l = Label(main_frame, text="Date", font=('Calibri Bold', '20'),width=43, bg="#F6F6F6")
        dates_l.grid(row=1, column=2, padx=1, pady=1)

        # Add button at the bottom of the screen to confirm selection and
        # return to home screen (via main_window()).
        confirm_btn = Button(main_frame, text="CONFIRM", font=('Calibri Bold', '28'), height=1, bg="lime", command=lambda: self.main_window())
        confirm_btn.grid(row = 13, column = 0, columnspan=3, sticky="EW")

    # Function for destroying current window and re-displaying the main window.
    # All selected events are also added to the 'export list'.
    def main_window(self):
        index = 0
        for chkbtn in self.chkbtn_list:
            # Check each checkbutton's variable; if it is checked (or True), then
            # add the corresponding event to the 'export list'.
            if(self.chkbtnvars_list[index].get()==True):
                self.master.EXPORT_LIST.append(self.master.event_list[index])
            index += 1
        
        # Destory current window and re-display main GUI.
        self.master.deiconify()
        self.destroy()

class BookGUI(Toplevel):
    def __init__(self, master):
        # Setup window.
        super().__init__()
        self.title("HUB - Upcoming concerts, movies, and books.")
        self.geometry("1400x900")
        main_frame = Frame(self, width=1400, bg="black")
        main_frame.pack(fill=BOTH, expand=1)
        
        title_l = Label(main_frame, text="UPCOMING BOOKS", font=('Calibri Light', '36'), bg="#F6F6F6", height=3)
        title_l.grid(row=0, column=0, columnspan=3, sticky="ew")

        # Create two empty lists that store all the checkbuttons and their
        # corresponding values.
        self.chkbtn_list = [None]*10
        self.chkbtnvars_list = [None]*10

        # Generate 10 rows of checkbuttons with corresponding titles and dates.
        for row_num in range(10):
            # Set button variable at index row_num to a Tkinter boolean variable.
            self.chkbtnvars_list[row_num] = BooleanVar()

            # Set index row_num of the button list to a Checkbutton with corresponding variable
            # from the button variables list.
            self.chkbtn_list[row_num] = Checkbutton(main_frame, bg="#F6F6F6", variable=self.chkbtnvars_list[row_num])
            self.chkbtn_list[row_num].grid(row=2+row_num, column=0, sticky="news", padx=1, pady=1)

            # Create two labels for the title and date of the event at index row_num of the current event list.
            Label(main_frame, text=self.master.event_list[row_num][1], bg="#F6F6F6", height=2, font=('Calibri Light', '16')).grid(row=2+row_num, column=1, sticky="news", padx=1, pady=1)
            Label(main_frame, text=self.master.event_list[row_num][2], bg="#F6F6F6", height=2, font=('Calibri Light', '16')).grid(row=2+row_num, column=2, sticky="news", padx=1, pady=1)
        
        # Add additional title labels for each column.
        selected_l = Label(main_frame, text="Select", font=('Calibri Bold', '20'), width=5, bg="#F6F6F6")
        selected_l.grid(row=1, column=0, padx=1, pady=1)
        concerts_l = Label(main_frame, text="Book", font=('Calibri Bold', '20'), width=51, bg="#F6F6F6")
        concerts_l.grid(row=1, column=1, padx=1, pady=1)
        dates_l = Label(main_frame, text="Date", font=('Calibri Bold', '20'),width=43, bg="#F6F6F6")
        dates_l.grid(row=1, column=2, padx=1, pady=1)

        # Add button at the bottom of the screen to confirm selection and
        # return to home screen (via main_window()).
        confirm_btn = Button(main_frame, text="CONFIRM", font=('Calibri Bold', '28'), height=1, bg="lime", command=lambda: self.main_window())
        confirm_btn.grid(row = 13, column = 0, columnspan=3, sticky="EW")

    # Function for destroying current window and re-displaying the main window.
    # All selected events are also added to the 'export list'.
    def main_window(self):
        index = 0
        for chkbtn in self.chkbtn_list:
            # Check each checkbutton's variable; if it is checked (or True), then
            # add the corresponding event to the 'export list'.
            if(self.chkbtnvars_list[index].get()==True):
                self.master.EXPORT_LIST.append(self.master.event_list[index])
            index += 1
        
        # Destory current window and re-display main GUI.
        self.master.deiconify()
        self.destroy()

###########################################
#-----------------------------------------#
###########################################


###########################################
#--------------GET HTML INFO--------------#
###########################################

# Function for gathering all the event info about upcoming concerts.
# A list is returned containing other lists with the structure:
# ["Concert", title, date, location_name, full_location, imgurl]
def get_upcoming_concerts(html_file):
    # Create empty list to store individual listings.
    concerts_list = [None]*10
    index = 0

    # Get each listing, or section of HTML that contains all the information needed
    # about the listing.
    concerts = findall('<li title="[\s\S]+?</script>\n      </div>\n    </li>', html_file)

    # Reduce the list down to only 10 events.
    concerts = concerts[:10]

    # For each section of HTML:
    # find the date, title, venue name, location, and image url of the event.
    # Return this info as a list to be used in button/label generation of the 'Upcoming Concerts' GUI,
    # and for exporting the HTML document.
    for concert in concerts:
        # Replace '-' character not properly interpretted by the HTML downloader function.
        concert = concert.replace('â€“', '-')

        # Find corresponding information in section of HTML code using REGEX.
        date = findall('<li title="(.*)">', concert)[0]
        title = findall('<strong>(.*)</strong>', concert)[0]
        venue_name = findall('<span class="venue-name"><a href="[a-zA-Z0-9 _/-]+">([a-zA-Z ]+)</a>', concert)
        location_name = findall('<span>\n[ \t]+<span>\n[ \t]+(.*)\n[ \t]+</span>', concert)[0]
        street_address = findall('<span class="street-address">(.*)</span>', concert)
        imgurl = findall('<img src="([a-zA-Z0-9 _/.-]+)"', concert)[0]

        # This particular website doesn't always display the locaitons consistently.
        # Hence, if 1 or more parts of the location is missing, the final location string
        # must be handled differently.
        if venue_name != [] and street_address != []:
            venue_name = venue_name[0]
            street_address = street_address[0]
            full_location = venue_name + ', ' + street_address + ' - ' + location_name
        elif venue_name != []:
            venue_name = venue_name[0]
            full_location = venue_name + ' - ' + location_name
        elif street_address != []:
            street_address = street_address[0]
            full_location = street_address + ' - ' + location_name
        else:
            full_location = location_name

        # Compile all info into one 'listing', with an identifier at the first index so the program
        # knows where the list came from.
        concert_listing = ["Concert", title, date, location_name, full_location, imgurl]

        # Add this listing to a list of listings, which will be returned upon calling this function.
        concerts_list[index] = concert_listing
        index += 1

    # Return the list containing 10 individual events and their information.
    return(concerts_list)

# Function for gathering all the event info about upcoming movies.
# A list is returned containing other lists with the structure:
# ["Movie", title, date, imgurl]
def get_upcoming_movies(html_file):
    # Create empty list to store individual listings.
    movies_list = [None]*10
    index = 0

    # Get each listing, or section of HTML that contains all the information needed
    # about the listing.
    movies = findall('<li class="visual-item">(.*?)</li>', html_file, re.DOTALL)
    movies = movies[:10]

    # For each section of HTML:
    # find the date, title, and image url of this event.
    # Return this info as a list to be used in button/label generation of the 'Upcoming Movies' GUI,
    # and for exporting the HTML document.
    for movie in movies:
        # Find corresponding information in section of HTML code using REGEX.
        title = findall('<a class="visual-title dark".*>(.*)</a>', movie, re.DOTALL)[0]
        title  = title.strip()
        date = findall('<span class="visual-sub-title">(.*)</span>', movie, re.DOTALL)[0]
        imgurl = findall('<img data-src="(.*?)"', movie, re.DOTALL)[0]

        # Compile all info into one 'listing', with an identifier at the first index so the program
        # knows where the list came from.
        movie_listing = ["Movie", title, date, imgurl]

        # Add this listing to a list of listings, which will be returned upon calling this function.
        movies_list[index] = movie_listing
        index+=1

    # Return the list containing 10 individual events and their information.
    return(movies_list)

# Function for gathering all the release info of upcoming Books.
# A list is returned containing other lists with the structure:
# ["Book", title, date, author, imgurl]
def get_upcoming_books(html_file):
    # Create empty list to store individual listings.
    books_list = [None]*10
    index = 0

    # Get each listing, or section of HTML that contains all the information needed
    # about the listing.
    books = findall('<div class="product" data-listing="[0-9]+">(.*?)</span>[\n\t ]*</span>[\n\t ]*</div>[\n\t ]*</div>', html_file, re.DOTALL)
    books = books[:10]

    # For each section of HTML:
    # find the release date, title, author and image url of the book.
    # Return this info as a list to be used in button/label generation of the 'Upcoming Books' GUI,
    # and for exporting the HTML document.
    for book in books:
        # Find corresponding information in section of HTML code using REGEX.
        title = findall('<a href="/product/.*" title="(.*)"', book)[0]
        author = findall('<a class="creator" href=".*">(.*)</a>', book)[0]

        # The dates appear jumbled when displayed, however this is due to the websites layout/sorting
        # of its content.
        date = findall('<span class="date">- out (.*)', book)[0]
        imgurl = findall('<img title=".*" src="(.*?)"', book)[0]

        # Compile all info into one 'listing', with an identifier at the first index so the program
        # knows where the list came from.
        book_listing = ["Book", title, date, author, imgurl]

        # Add this listing to a list of listings, which will be returned upon calling this function.
        books_list[index] = book_listing
        index+=1
    
    # Return the list containing 10 individual upcoming books and their information.
    return(books_list)
###########################################
#-----------------------------------------#
###########################################



###########################################
#------------REMOVE DUPLICATES------------#
###########################################

# Function for removing duplicate events.
# As events can be selected more than once due to the GUI creation/destruction
# process. Therefore, if events are selected mulitple times, they'll be filtered
# out and a list consisting of ONLY 1 of each event will be returned.
def remove_duplicates(EXPORTEDLIST):
    final_list = [] 
    for item in EXPORTEDLIST:
        if item not in final_list: 
            final_list.append(item) 
    return final_list

###########################################
#-----------------------------------------#
###########################################



###########################################
#-----------PLANNER GENERATION------------#
###########################################

# Function for generating the HTML planner file, and the database.
def generate_planner(EXPORTEDLIST, HTML_PLANNER, DBSTATE):
    # Name of the planner file.
    planner_file = 'planner.html'

    # Set variables to count the number of events in each category.
    concert_count = 1
    movie_count = 1
    book_count = 1

    # Remove all duplicate events in the list.
    EXPORTEDLIST = remove_duplicates(EXPORTEDLIST)

    # If the exported list is empty, then display the appropriate empty HTML
    # document.
    if(not EXPORTEDLIST):
        insert_index = HTML_PLANNER.find('<div style="background-color: white;">')
        insert_string = """
                        <p style="color:red; font-size:24px; text-align: center;">
                            <b> THERE ARE NO SELECTED EVENTS TO DISPLAY</b>
                        </p>
                        """
        HTML_PLANNER = HTML_PLANNER[:insert_index] + insert_string + HTML_PLANNER[insert_index:]

    # Otherwise, loop through each event and test whether it is a conecrt, movie, or book release.
    # Then, insert the corresponding string to display the data and image in HTML code.
    else:
        for event in EXPORTEDLIST:
            # The identifier of the event is stored at index 0 of each event.
            if event[0]=="Concert":
                insert_index = HTML_PLANNER.find("<!--INSERTCONCERTS-->")

                # If the current event count in this category is odd or even, generate
                # the appropriate HTML code for the start or end of a table row.
                if concert_count%2==0:
                    insert_string = """
                                        <td style="background-image: url('https:%s');">
                                            <div>
                                                <b>%s <!--Title--></b>
                                                <br>
                                                %s <!--Location-->
                                                <br>
                                                %s <!--Date-->
                                                <br>
                                            </div>
                                        </td>
                                    </tr>
                                    """%(event[5], event[1], event[4], event[2])
                else:
                    insert_string= """
                                    <tr>
                                        <td style="background-image: url('https:%s');">
                                            <div>
                                                <b>%s <!--Title--></b>
                                                <br>
                                                %s <!--Location-->
                                                <br>
                                                %s <!--Date-->
                                                <br>
                                            </div>
                                        </td>
                                    """%(event[5], event[1], event[4], event[2])

                # Insert this block of HTML code at the right index by slicing all the 
                # characters before and after that index and creating a new string.
                HTML_PLANNER = HTML_PLANNER[:insert_index] + insert_string + HTML_PLANNER[insert_index:]

                # Add 1 to this category's counter to keep track of how many of this event type 
                # have been added.
                concert_count += 1

            elif event[0]=="Movie":
                insert_index = HTML_PLANNER.find("<!--INSERTMOVIES-->")

                if movie_count%2==0:
                    insert_string = """
                                        <td style="background-image: url('%s');">
                                            <div>
                                                <b>%s <!--Title--></b>
                                                <br>
                                                %s <!--Date-->
                                                <br>
                                            </div>
                                        </td>
                                    </tr>
                                    """%(event[3], event[1], event[2])
                else:
                    insert_string= """
                                    <tr>
                                        <td style="background-image: url('%s');">
                                            <div>
                                                <b>%s <!--Title--></b>
                                                <br>
                                                %s <!--Date-->
                                                <br>
                                            </div>
                                        </td>
                                    """%(event[3], event[1], event[2])
                HTML_PLANNER = HTML_PLANNER[:insert_index] + insert_string + HTML_PLANNER[insert_index:]
                movie_count += 1

            elif event[0]=="Book":
                insert_index = HTML_PLANNER.find("<!--INSERTBOOKS-->")

                if book_count%2==0:
                    insert_string = """
                                        <td style="background-image: url('%s');">
                                            <div>
                                                <b>%s <!--Title--></b>
                                                <br>
                                                <i>%s</i> <!--Author-->
                                                <br>
                                                %s <!--Date-->
                                                <br>
                                            </div>
                                        </td>
                                    </tr>
                                    """%(event[4], event[1], event[3], event[2])
                else:
                    insert_string= """
                                    <tr>
                                        <td style="background-image: url('%s');">
                                            <div>
                                                <b>%s <!--Title--></b>
                                                <br>
                                                <i>%s</i> <!--Author-->
                                                <br>
                                                %s <!--Date-->
                                                <br>
                                            </div>
                                        </td>
                                    """%(event[4], event[1], event[3], event[2])
                HTML_PLANNER = HTML_PLANNER[:insert_index] + insert_string + HTML_PLANNER[insert_index:]
                book_count += 1

    # Write full HTML string to a HTML file.
    HTML_FILE = open(planner_file, 'w')
    HTML_FILE.write(HTML_PLANNER)
    HTML_FILE.close()

    # Display a message to show how many events were exported.
    messagebox.showinfo('PLANNER EXPORTED!', 'Your planner has a total of %i events!'%(len(EXPORTEDLIST)))

    # If the 'database mode' button is on, also export the list in the database.
    if(DBSTATE == "Database Export On"):
        export_db(EXPORTEDLIST)
    
###########################################
#-----------------------------------------#
###########################################



###########################################
#----------------DATABASE-----------------#
###########################################

# Function for exporting the events list as an SQL database.
def export_db(EXPORTEDLIST):
    # Connect to the database and create a cursor object. 
    connection = connect('.\\database\\entertainment_planner.db')
    cursor = connection.cursor()

    # Delete ("DROP") the current table to clear it of all old data.
    cursor.execute('DROP TABLE IF EXISTS events')

    # Re-create the table with the same fields
    cursor.execute('''CREATE TABLE events (
                    event_name    TEXT NOT NULL, 
                    event_date    TEXT NOT NULL 
                    )''')

    # For each event, insert the corresponding title and date into the database.
    for event in EXPORTEDLIST:
        cursor.execute('INSERT INTO events VALUES ("%s", "%s")'%(event[1], event[2]))
    
    connection.commit()
    connection.close()

    # Display message notifying the user that the database has been updated.
    messagebox.showinfo('DATABASE EXPORTED!', 'Your database has been updated with the latest events!')

###########################################
#-----------------------------------------#
###########################################

# Open the main Tkinter window and run the mainloop()
MainGUI().mainloop()