# File-Search-by-Creation-Time
The "File Search by Creation Time" script is a Python utility that enables users to locate files within a specified directory based on their creation timestamps. This can be particularly useful when you need to filter and identify files created within a specific time frame.

# Features:
Flexible Duration Specification:

Users can input a duration in the format of -days=2, +minutes=60, -seconds=180, where the leading + indicates a duration greater than and - indicates a duration less than the specified time.
Intuitive User Interaction:

The script prompts users to input the desired duration and the path of the directory they want to search, ensuring a straightforward and user-friendly experience.
Timestamp Comparison:

The script leverages the creation time (ctime) of each file and compares it against the specified duration, allowing users to identify files that meet their temporal criteria.
# How to Use:
Run the script:
Execute the script using a Python interpreter.

Enter Duration:
Input the desired duration in the specified format (-days=2, +minutes=60, -seconds=180).

Specify Directory:
Provide the path of the directory where you want to perform the file search.

View Results:
The script will display the paths of files that match the specified temporal criteria.

Example:
Enter Duration i.e: -days=2, +minutes=60, -seconds=180 :
Leading + is for more than, and - is for less than
-days=5
Enter Path i.e c:\Users\ :
C:\Users\YourUsername\
# License:
This project is licensed under the MIT License - see the LICENSE file for details.

Feel free to tailor this description to provide additional details, usage scenarios, or any other information you feel would enhance the understanding and usability of your script.
