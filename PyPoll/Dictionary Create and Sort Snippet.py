# Snippet of dictionary code for creating, updating and sorting
candidate[] = {}

# Start for Loop

    if candidate.get(inname) == None
        candidate[inname] = 1
    else candidate[inname] +=1 

print(f'candidate list and votes = {candidate}')

sorted_by_votes = sorted(condidate.items(), key= lambda vote_count: vote_count[1], reverse=True)

print(f'sorted by votes= {sorted_by_votes}')