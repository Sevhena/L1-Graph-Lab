# import the graphbuilder

#use extracor to aquire the stations

#use extractor to obtain the connections

#build the graph


connections = {

    11: {163:[[1,1]], 83:[[3,3],[6,3]] },
    49: {87:[[1,1]]}
}

print(connections[11][83][0])