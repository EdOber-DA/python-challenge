thisdict = {"Cand-8":1}
#print(thisdict)
thisdict["Cand-9"] = 1
#print(thisdict)
thisdict["Cand-3"] = 1
#print(thisdict)
thisdict["Cand-9"] += 1
#print(thisdict)
thisdict["Cand-9"] += 1
#print(thisdict)
thisdict["Cand-3"] += 1
#print(thisdict)
setkey = thisdict.get("Cand-8")
#print(setkey)
setkey = thisdict.get("Cand-9")
#print(setkey)
setkey = thisdict.get("Cand-3")
#print(setkey)
setkey = thisdict.get("Cand-bad")
#print(setkey)
# GOOD TO HERE
print(f'thisdict= {thisdict}')
print(f'Sorted(thisdict)= {sorted(thisdict)}') # This worked, sorting by the candidates name

#def take_second(elem):
#    print(elem[4],elem)
#    return elem[4]
sorted_thisdict=sorted(thisdict.items(), key= lambda candidate_count: candidate_count[1], reverse=True)

print(f'sorted_thisdict= {sorted_thisdict}')

#Winner = 