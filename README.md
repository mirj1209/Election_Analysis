# Election_Analysis

## Project Overview
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received. 
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the eleciton based on popular vote.

## Resources 
- Data source: election_results.csv
- Software: Python 3.10.4, Visual Studio Code, 1.38.1

## Summary
The analysis of the election show that:
- There were 369,711 votes cast in the election.
- The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
- The candidate results were:
    - Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes.
    - Diana DeGette received 73.8% of the vote and 272,892 number of votes.
    - Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes.
- The winner of the election was:
    - Diana DeGette, who received 73.8% of the vote and 272,892 number of votes.

## Challenge Overview
The purpose of the election audit is to make the data taken from all voters much nicer to work with and to have a clear-cut winner almost instantly

## Challenge Summary
### Election-Audit results
-	Total votes were: 369,711
-	Votes per county:
	- Jefferson: 38,855 holding 10.5% of the overall votes
	- Denver: 306,055 holding 82.8%
	- Arapahoe: 24,801 holding 6.7% of all voters
-	Votes per candidate
	- Charles Casper Stockham had 85,213 votes holding a percentage of 23.0%
	- Diana DeGette had 272,892 votes holding a percentage of 73.8%
	- Raymon Anthony Doane had 11,606 votes holding a percentage of 3.1%

Thus, Denver had the highest amount of voters and therefore, the county with the most numerical weight. And the winner of the election was Diana DeGette 

### Election_Audit Summary
The general template of the code can be reused for any election as it’s reader-friendly thus, anyone with minimal/general knowledge in python will know exactly where to edit the code according to what they’re looking for. For example, if you wish to expand on the information given, you could find out in which county each candidate was the most popular on. This is useful as it’ll give a more detailed answer instead of just the speculation of Diana DeGette being most popular in Denver since she was the winner and Denver hold the most numerical value.     

