# Election_Analysis

## Project Overview
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast. 
2. Get a complete list of candidates who received votes. 
3. Calculate the total number of votes each candidate received. 
4. Calculate the percentage of votes each candidate won. 
5. Determine the winner of the election based on popular vote.
6. Calculate the total number of votes each county received. 
7. Calculate the percentage of votes each county won.
8. Determine the county with the largest turnout of voters.

## Resources
* Data Source: election_results.csv

* Software: Python 3.10.6, Visual Studio Code

## Analysis Summary
The analysis of the elction show that (see *figure 1a-b*: 

* There were 369,711 votes cast in the election. 

* The candidates were:

  * Charles Casper Stockham
  * Diana DeGette
  * Raymon Anthony Doane
  
* The candidate results were:

  * Charles Casper Stockham received 23.0% of the vote and 85,123 number of votes. 
  * Diana DeGette received 73.8% of the vote and 272,892 number of votes.
  * Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes.

* The winner of the election was:

  * Diana DeGette, who received 73.8% of the vote and 272,892 number of votes. 

* The counties polled were:

  * Jefferson
  * Denver
  * Arapahoe

* The county results were:

  * Jefferson received 10.5% of the vote and 38,855 number of votes. 
  * Denver received 82.8% of the vote and 306,055 number of votes.
  * Arapahoe received 6.7% of the vote and 24,801 number of votes.

* The county with the largest voter turnout was:
  
  * Denver 

*Figure 1a*- Write to text file

![election_results_txt2](https://github.com/maureengamache/Election_Analysis/blob/main/election_results_txt2.png)

*Figure 1b*- Command line printout

![Command_line_results](https://github.com/maureengamache/Election_Analysis/blob/main/Command_line_results.png)

## Election-Audit Summary and Proposal: 

In summary, the use of Visual Studio Code and Python in analyzing the .csv raw data of the election votes was successful in determining the candidates and counties, number of votes and vote percentage for each candidate and county, respectively. Given that the written code works as written, it would be beneficial to the Colorado Board of Elections to purchase this code. However, there are a few modifications that could be made to make the more useful on a larger scale. The code could be refactored to make this script, with some modifications, useable for any election. This would be completed by using a macro in VBA that would tailor the results to the need, based on either, county or candidate through use of an InputBox and button. Or, through using refactored code in Python/VSC where the values of candidate and county are combined in a list of ditionaries, instead of running seperate script for multiple single dictionaries. By creating the list of dictionaries, more data could be referenced on a larger scale, and looped through,  as well as a potential improvment in run time for the code.



