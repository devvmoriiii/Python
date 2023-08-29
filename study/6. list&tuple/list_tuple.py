# =============================================================================
# mutable (변할 수 있는) : list
# immutable (변할 수 없는) : tuple
# =============================================================================

#%% mutable

dataList1 = [1, 2, 3]
dataList2 = dataList1 

dataList2.append(4)

print(dataList1)

#%% immutable

dataTuple1 = 1,2,3
dataTuple2 = dataTuple1

dataTuple2 += 4, 5

dataTuple1[0] = 10