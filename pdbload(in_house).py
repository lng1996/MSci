import wget
import csv



acclist=[]
with open('AlphaBlast.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        acclist.append(row[1].split('.')[0])
ele_load=list(set(acclist))
print(ele_load)
for ele in ele_load:
    try:
        url = f'https://swissmodel.expasy.org/repository/uniprot/{ele}.pdb'
        #url = f'https://files.rcsb.org/download/{ele}.pdb'
        filename = wget.download(url,out="C:/Users/Leo/Desktop/Disser/Computational/Jupyter/Alpha80100SwissBlast")
        filename
    except: 
        print(ele + " Not Found")