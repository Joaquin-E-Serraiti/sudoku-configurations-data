# Sudoku Configurations Data
This is a completed project in which I learnt the basics about databases and data analysis tools. The goal of this project was to explore patterns in randomly generated Sudoku configurations and practice data analysis.

### Technologies utilized:
-	Python
-	Pandas library
-	SQLite (sqlite3 module)
-	Power BI
  
## What I did
> [!IMPORTANT]
> This project is based on [this article](https://github.com/Joaquin-E-Serraiti/jes-sudoku-lab/blob/main/Classification%20of%20Sudoku%20Patterns%20and%20Transformations.pdf) where I classificated many Sudoku patterns, and on [this tool](https://github.com/Joaquin-E-Serraiti/jes-sudoku-lab) I created to analyze those patterns. Reading the article will help understand better what is being analyzed on this project.
- I generated 10000 random sudoku configurations using `sudokuLab.py`, a tool I developed.
- With that tool, I also analyzed the patterns of each configuration and obtained relevant data.
- Using SQLite, I created a database (`sudokuConfigurations.db`) containing all generated configurations along with the data from the analysis of their patterns (`databaseCreation.py`).
- I converted the data into a CSV file (`sudoku_configurations.csv`) using Pandas, to import it into Power BI.
- With Power BI, I created reports / charts to visualize the relationships between the configurations and compare their data.
  
## Charts
Here is an example with only 10 configurations:

![chart_1](/chart_1.jpg)

In the X axis are the configurations and in the Y axis are the proximity values of the IBPU (Intra-Box Positional Uniqueness), IBPA (Intra-Box Positional Alignment) and TDC (Triplet Digit Consistency) patterns, expressed in percentages.

The following charts show the values of all 10000 configurations.

Configurations ordered by their IBPA proximity values (blue line), in ascending order:

![chart_2](/chart_2.jpg)

Configurations ordered by their TDC proximity values (orange line), in ascending order:

![chart_3](/chart_3.jpg)

Configurations ordered by their IBPU proximity values (light blue line), in ascending order:

![chart_4](/chart_4.jpg)

## Conclusions based on the charts

One thing I noticed is that the values for TDC proximity (orange line) are, overall, lower than the values for IBPU and IBPA proximity. From this I conclude that, in randomly generated configurations, the proximity values of the IBPU and IBPA patterns tend to be higher than the proximity values of the TDC pattern. This suggest than the TDC pattern is more constrained than the other patterns.

Another thing I noticed is that, for all configurations, the proximity values of the IBPU pattern tend to lie in a similar level as the proximity values of the IBPA pattern. In contrast, the TDC pattern proximity tends to be much lower.

## What I learnt by doing this project
- The basics on relational databases and how they work.
- The Structured Query Language (SQL).
- How to create and query data bases with SQLite.
- How to manipulate data with Pandas.
- How to visualize data with Power BI.
