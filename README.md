# Delete Logs Script
Some of the systems will keep updating the modification date timestamp of their logs to the current date, and since Unix-based systems normally do not have a timestamp for the creation date of a file, updating the modification date will cause an issue in case there is a crontab that runs every day to delete the log files that are older than a specified number of days, and since crontab uses the modification date timestamp to decide if a log file should be deleted or not, this will result in not deleting any log file.

But log files are normally named with their creation date like "20200301.log", here is a Python script that takes the creation date from the log file name and compares it with the current date to if the log file should be deleted or not.

Then you can put this script in a crontab (:
