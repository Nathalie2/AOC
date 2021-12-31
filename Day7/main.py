with open('Day7/input.txt') as f:
    data = list(map(int,f.read().split(',')))

delta_const = [[] for pos in range(min(data), max(data)+1)]
delta_notconst = [[] for pos in range(min(data), max(data)+1)]
positions = range(min(data), max(data)+1)
for i_pos in range(len(positions)):
    delta_const[i_pos] = [abs(number - positions[i_pos]) for number in data]
    delta_notconst[i_pos] = [(abs(number - positions[i_pos]) *(abs(number - positions[i_pos]) +1))/2 for number in data]

delta_sum = [sum(pos) for pos in delta_const]
min_delta_sum = min(delta_sum)
print('Part 1 solution:'+str(min_delta_sum))

delta_nc_sum = [sum(pos) for pos in delta_notconst]
min_delta_nc_sum = min(delta_nc_sum)
print('Part 2 solution:'+str(min_delta_nc_sum))