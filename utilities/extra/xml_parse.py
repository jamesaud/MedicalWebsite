import os 

def parseTable(file):
    """
    Writes a compatible table for cross-reference-table css from an html file.
    Output: html file
    """
    with open(file, 'r') as f:
        text = f.read()
    
    print(tr)


path = os.path.join(os.getcwd(), 'utilities/extra/test_table.html')

parseTable(path)

