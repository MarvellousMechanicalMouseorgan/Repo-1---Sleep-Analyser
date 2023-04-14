# Repo-1---Sleep-Analyser
This Python script is a Sleep Analysis Utility, which uses the Tkinter library and a custom Tkinter package (customtkinter) to create a graphical user interface (GUI) for analyzing sleep data. The utility reads data from CSV files and performs various data cleaning and analysis tasks.

An overview of the script's functionality is below:
• Import necessary libraries, including customtkinter, pandas, and Tkinter components.
• Create the main GUI window, set its dimensions and title, and configure its appearance.
• Create frames for displaying buttons and an image. Load the image and display it in the image_frame.
• Define a function ‘clean_dataframe’ to clean the input DataFrame by removing rows containing missing values.
• Define a function ‘merge_csv_files’ to merge multiple CSV files into a single DataFrame. This function also calls ‘clean_dataframe’ to clean the data.
• Define a function ‘count_contiguous_ones’ to count contiguous groups of 1s in a binary series.
• Define a function ‘analyze_batches’ to analyze data columns by counting the number of contiguous 1s in each column, as well as the percentage of 1s.
• Define a function ‘show_statistics_and_plots’ to display the analysis results in a new window.
• Define button click functions: ‘button1_click_singlefile’, ‘button2_click_singlefile’, and ‘button3_click’. These functions are responsible for opening file dialogs to select control and condition CSV files, merging the files, and displaying the results.
• Create and place the label and buttons in the main GUI window.
• Start the main event loop to display the GUI.
The utility allows users to select and merge multiple control and condition CSV files, clean the data by removing rows with missing values, and analyse the data by counting the number of contiguous 1s in each specified column. The results are then displayed in a new window.

Installation and Operation
------------
a. Files
Source Code is: Sleep Analysis Util V2.0
SplashMain.PNG

b. Specific Folders Required
• When processing data, there are no specific folder locations required.
• To operate the application from an IDE then the folder path C:\Images is required to hold the SplashMain.PNG file.

c. Installation & Operation
The code can be installed to work in a Project file in PyCharm IDE or Jupiter Lab/Notebook. The code itself contains details of the packages that must be installed.
