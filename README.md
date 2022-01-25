# sb6183-signallevels
Query Arris SurfBoard 6183 Cable Modem signal levels &amp; save to CSV file.  Code liberally reused from examples elsewhere.

I made this in my quest to figure out Comcast's problem with my house.  I scheduled it to run every 5 minutes to record the data.  My upstream signal levels shifted by 15dBmV throughout the day, causing my modem to drop connections frequently.  Yep, it was Comcast's problem, but it took the data to prove that to them.

Usage:
python sb6183_signallevels.py

Notes:
   - Assumes that the SB6183 signal level page is at http:////192.168.100.1/RgConnect.asp  Edit the "statusURL" to change that.
   - Outputs the tables to a CSV file named sb6183log.csv.  Edit the "outputFileName" to change that.
