from sudokuLab import SudokuLab
import sqlite3
import pandas

conn = sqlite3.connect("sudokuConfigurations.db")
cursor = conn.cursor()

cursor.execute("""
            CREATE TABLE IF NOT EXISTS sudoku_configurations (
                id INTEGER PRIMARY KEY,
                sudoku_string TEXT UNIQUE,
                ibpu_percentage REAL,
                ibpa_percentage REAL,
                tdc_percentage REAL,
                repeated_ib_positions INTEGER,
                repeated_horizontal_ib_positions INTEGER,
                repeated_vertical_ib_positions INTEGER,
                unique_horizontal_triplet_sets INTEGER,
                unique_vertical_triplet_sets INTEGER,
                repeated_horizontal_triplet_sets INTEGER,
                repeated_vertical_triplet_sets INTEGER
            )
            """)


def insertSudokuConfigData(dataTuples):
    cursor.executemany("""
                    INSERT OR IGNORE INTO sudoku_configurations (
                        sudoku_string,
                        ibpu_percentage,
                        ibpa_percentage,
                        tdc_percentage,
                        repeated_ib_positions,
                        repeated_horizontal_ib_positions,
                        repeated_vertical_ib_positions,
                        unique_horizontal_triplet_sets,
                        unique_vertical_triplet_sets,
                        repeated_horizontal_triplet_sets,
                        repeated_vertical_triplet_sets)
                    VALUES (?,?,?,?,?,?,?,?,?,?,?)
                    """, dataTuples)


def clearTable():
    cursor.execute("DELETE FROM sudoku_configurations")
    conn.commit()


def printTable():
    df = pandas.read_sql_query(
        """SELECT ibpu_percentage, ibpa_percentage, tdc_percentage 
        FROM sudoku_configurations
        """, conn)
    print(df)


def dataToTuple(sudokuString, reportDict):

    ibpuPercentage = reportDict["IBPU"]["percentage"]
    ibpaPercentage = reportDict["IBPA"]["percentage"]
    tdcPercentage = reportDict["TDC"]["percentage"]
    repeatedIBPositions = reportDict["IBPU"]["metrics"][0]
    repeatedHorizontalIBPositions = reportDict["IBPA"]["metrics"][0]
    repeatedVerticalIBPositions = reportDict["IBPA"]["metrics"][1]
    uniqueHorizontalTripletSets = reportDict["TDC"]["metrics"][0]
    uniqueVerticalTripletSets = reportDict["TDC"]["metrics"][1]
    repeatedHorizontalTripletSets = reportDict["TDC"]["metrics"][2]
    repeatedVerticalTripletSets = reportDict["TDC"]["metrics"][3]

    return (sudokuString, ibpuPercentage, ibpaPercentage, tdcPercentage, repeatedIBPositions, repeatedHorizontalIBPositions, repeatedVerticalIBPositions, uniqueHorizontalTripletSets, uniqueVerticalTripletSets, repeatedHorizontalTripletSets, repeatedVerticalTripletSets)


def generateAndInsertConfigs(numberOfBatches, batchSize=1000, sudokuLab=SudokuLab()):

    configDataTuples = []
    counter = 0
    totalConfigs = numberOfBatches*batchSize
    for batch in range(numberOfBatches):
        configs = sudokuLab.generateRandomGrids(batchSize)
        for config in configs:
            counter += 1
            sudokuLab.setNewGrid(config)
            report = sudokuLab.analysisReport()
            recordTuple = dataToTuple(config, report)
            configDataTuples.append(recordTuple)
            if (counter % 100) == 0:
                print(f"Progress: {int((counter/(totalConfigs))*1000)/10}%  ",
                      end="\r")
        insertSudokuConfigData(configDataTuples)
        configDataTuples.clear()
    conn.commit()


def convertToCSV(tableName="sudoku_configurations", chunkSize=2000):
    for i, chunk in enumerate(pandas.read_sql_query(f"SELECT id, ibpu_percentage, ibpa_percentage, tdc_percentage FROM {tableName}", conn, chunksize=chunkSize)):
        if i == 0:
            chunk.to_csv(f'{tableName}.csv', index=False)
        else:
            chunk.to_csv(f'{tableName}.csv', mode='a',
                         header=False, index=False)


conn.commit()
conn.close()
