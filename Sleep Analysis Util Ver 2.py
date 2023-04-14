###########################################################
# Sleep Analysis Utility
# Date 12th April 2023
# Version 1
###########################################################

import customtkinter
import pandas as pd

from tkinter.filedialog import askopenfilenames
from itertools import groupby
from tkinter import Toplevel, Text, END, font
from customtkinter import CTkFrame
from tkinter import PhotoImage, Label

###########################################################
# Sleep Analysis Utility
# Date 12th April 2023
# Version 1
###########################################################

# Throw Up Our Main Window
##################################################

print("At: Throw Up Main Window")

my_main = customtkinter.CTk()
my_main.geometry("1000x600")
my_main.update_idletasks()
my_main.after(0, lambda: my_main.state('zoomed'))
my_main.title("Sleep Data Analysis Utility")
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# Create frames for buttons and image
#####################################

print("At: Create Frames")
buttons_frame = CTkFrame(my_main, width=275, height=200)
buttons_frame.place(x=20, y=10)
image_frame = CTkFrame(my_main, width=1187, height=1085)
image_frame.place(x=300, y=0)

# Load the image
#################

image_path = "C:/Images/SplashMain.png"  # Replace with the actual path to your image
image = PhotoImage(file=image_path)

# Create a Label widget to display the image and add it to the image_frame
##########################################################################
print("At: Create text Widget")
image_label = Label(image_frame, image=image, bg="#2B2B2B")
image_label.place(x=0, y=0)

# Clean The Data ###########
############################

def clean_dataframe(df):
    print("At: Clean Data")
    total_rows_before = len(df)
    missing_data_rows = df.isna().any(axis=1)
    missing_data_count = missing_data_rows.sum()
    clean_df = df.dropna(axis=0, how='any')
    total_rows_after = len(clean_df)
    return clean_df, missing_data_count, missing_data_rows, total_rows_before, total_rows_after

# Merge the selected files
#########################

def merge_csv_files(file_paths):
    print("At: Merge CSV Files")

    dataframes = []
    files_with_missing_data = {}

    for file_path in file_paths:
        df = pd.read_csv(file_path)
        cleaned_df, missing_data_count, missing_data_rows, total_rows_before, total_rows_after = clean_dataframe(df)

        print(f"File: {file_path}")
        print(f"Total rows before cleaning: {total_rows_before}")
        print(f"Total rows after cleaning: {total_rows_after}\n")

        if missing_data_count > 0:
            files_with_missing_data[file_path] = {
                'missing_data_count': missing_data_count,
                'total_rows': len(df),
                'missing_data_percentage': (missing_data_count / len(df)) * 100,
                'missing_data_rows': missing_data_rows
            }
        dataframes.append(cleaned_df)

    merged_df = pd.concat(dataframes, ignore_index=True)
    return merged_df, files_with_missing_data


# Find Batches
# #######################

def count_contiguous_ones(series):
    return len([list(g) for k, g in groupby(series, key=lambda x: x == 1) if k])

def analyze_batches(df, column_names):
    print("At: analyze batches")

    results = {}

    for column in column_names:
        ones_count = df[column].value_counts().get(1, 0)
        ones_percentage = (ones_count / len(df)) * 100

        # Count the number of batches of contiguous 1's
        batches_count = count_contiguous_ones(df[column])

        results[column] = {
            'ones_count': ones_count,
            'ones_percentage': ones_percentage,
            'batches_count': batches_count
        }

    return results

# Show Stats and Plots
###########

def show_statistics_and_plots(df_merge_control, df_merge_condition):
    print("At: Show Stats n Plots")

    # Specify the column names to analyze (change this to match the actual column names in your data)
    column_names = ['light', 'moderate-vigorous', 'sedentary', 'sleep']  # replace with your actual column names

    # Analyze batches for control and condition DataFrames
    control_results = analyze_batches(df_merge_control, column_names)
    condition_results = analyze_batches(df_merge_condition, column_names)

    # Create a new Toplevel window and Text widget
    result_window = Toplevel()
    result_window.title("Batch Analysis Results")
    result_window.geometry("600x400")
    result_window.state("zoomed")

    # Set the font size for the Text widget
    text_font = font.Font(size=28)
    result_text = Text(result_window, wrap="word", font=text_font)
    result_text.pack(expand=True, fill="both")

    # Add information for control and condition DataFrames
    result_text.insert(END, "Control DataFrame:\n\n")
    for column, result in control_results.items():
        result_text.insert(END, f"{column}: {result['batches_count']} batches of 1's\n")

    result_text.insert(END, "\n\nControl Files Missing Data Percentage:\n\n")
    for file_path in file_paths_control:
        df = pd.read_csv(file_path)
        total_rows = len(df)
        missing_data_count = df.isna().any(axis=1).sum()
        missing_data_percentage = round((missing_data_count / total_rows) * 100)
        result_text.insert(END, f"{file_path}: {missing_data_percentage}% missing data\n")

    result_text.insert(END, "\n\nCondition DataFrame:\n\n")
    for column, result in condition_results.items():
        result_text.insert(END, f"{column}: {result['batches_count']} batches of 1's\n")

    result_text.insert(END, "\n\nCondition Files Missing Data Percentage:\n\n")
    for file_path in file_paths_condition:
        df = pd.read_csv(file_path)
        total_rows = len(df)
        missing_data_count = df.isna().any(axis=1).sum()
        missing_data_percentage = round((missing_data_count / total_rows) * 100)
        result_text.insert(END, f"{file_path}: {missing_data_percentage}% missing data\n")

    # Make the text widget read-only
    result_text.config(state="disabled")

# Click Button 1
################

def button1_click_singlefile():
    print("At: Button 1 Click")
    global file_paths_control
    file_paths_control = askopenfilenames(filetypes=[("CSV Files", "*.csv")])

    if file_paths_control:
        df_merge_control, files_with_missing_data_control = merge_csv_files(file_paths_control)
        globals()['df_merge_control'] = df_merge_control  # Save the merged dataframe to global scope
        globals()['files_with_missing_data_control'] = files_with_missing_data_control

# Click Button 2
################

def button2_click_singlefile():
    print("At: Button 2 Click")
    global file_paths_condition
    file_paths_condition = askopenfilenames(filetypes=[("CSV Files", "*.csv")])

    if file_paths_condition:
        df_merge_condition, files_with_missing_data_condition = merge_csv_files(file_paths_condition)
        globals()['df_merge_condition'] = df_merge_condition  # Save the merged dataframe to global scope
        globals()['files_with_missing_data_condition'] = files_with_missing_data_condition

# Click Button 3
################

def button3_click():
    print("At: Button 3 Click")
    if 'df_merge_control' in globals() and 'df_merge_condition' in globals():
        show_statistics_and_plots(globals()['df_merge_control'], globals()['df_merge_condition'])
    else:
        print(
            "Please ensure both control and condition DataFrames are available before generating statistics and plots.")

# Create and Place Labels and Buttons on Main Window
######################################################

print("At: Create Buttons on Main Window")
# Create and Place Label
info_label = customtkinter.CTkLabel(my_main, text="Files need to be in CSV Format...")
info_label.place(x=20, y=10)

# Create and Place Button 1
button1 = customtkinter.CTkButton(my_main, text="Select Multiple 'CONTROL' Files to Merge",
                                  command=button1_click_singlefile)
button1.place(x=20, y=40)

# Create and Place Button 2
button2 = customtkinter.CTkButton(my_main, text="Select Multiple 'CONDITION' Files to Merge",
                                  command=button2_click_singlefile)
button2.place(x=20, y=80)

# Create and Place Button 3
button3 = customtkinter.CTkButton(buttons_frame, text="Generate Statistics and Plots", command=button3_click)
button3.place(x=1, y=110)

# Main Loop
###############

my_main.mainloop()
