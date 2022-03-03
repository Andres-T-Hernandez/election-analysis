import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Print the file object.
     print(election_data)

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

     # Write three counties to the file.
     txt_file.write("Arapahoe\nDenver\nJefferson")

#The data we need to retrieve
#Total number of votes cast
#A complete list of candidates who received votes
#Total number of votes each candidate received
#Percentage of votes each candidate won
#The winner of the election based on popular vote