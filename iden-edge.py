import numpy as np
import xlrd
import pandas as pd

def open_edge_Info():

    # input edge file (ex. column 1: source node, column 2: target node)
    file = xlrd.open_workbook('edge.xlsx').sheet_by_index(0)
    nrows = file.nrows

    edge_Info = []
    for row_num in range(nrows):
        edge_Info.append(file.row_values(row_num))
    return edge_Info

def open_community_result():
    # input edge file (ex. column 1: source node, column 2: community id)
    file = xlrd.open_workbook('community_result.xlsx').sheet_by_index(0)
    nrows = file.nrows

    Community_result = []
    for row_num in range(nrows):
        Community_result.append(file.row_values(row_num))
    Community_result = dict(Community_result)
    Community_result = dict((k, int(v)) for k, v in Community_result.items())
    return Community_result

def matching(Community_result, edge_Info):
    for row in range(0, len(edge_Info)):
        edge_Info[row].insert(0, Community_result[edge_Info[row][0]])
        edge_Info[row].insert(2, Community_result[edge_Info[row][2]])

    print(np.array(edge_Info))
    pd.DataFrame(edge_Info).to_csv('intra edges.csv', header=False, index=False, encoding='ms949')

    Community_diff_edge = []
    for row in range(0, len(edge_Info)):
        if edge_Info[row][0] != edge_Info[row][2]:
            Community_diff_edge.append(edge_Info[row])

    Community_diff_edge = pd.DataFrame(Community_diff_edge)
    Community_diff_edge.to_csv('inter edges.csv', header=False, index=False, encoding='ms949')

if __name__ == "__main__":
    edge_Info = open_edge_Info()
    Community_result = open_community_result()
    matching(Community_result, edge_Info)