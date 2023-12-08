

from dataclasses import dataclass

import time

@dataclass
class MapEntry:
    destination_start: int
    source_start: int
    length: int


@dataclass
class Map:
    destination: str
    source: str
    entries: [MapEntry]

    def range_mapper(self,value,length):
        new_ranges = []
        ranges = [(value,length)]
        # map overlaps of the range for each entry
        for entry in self.entries:
            temp_ranges = []
            while ranges:
                (value,length) = ranges.pop()
                start = value
                end = value+length
                entry_end = entry.source_start+entry.length
                shift = entry.destination_start - entry.source_start

                # range before
                #  [--] { }
                #  [--{ ] }
                # start to min end or entry_end
                before = min(entry.source_start,end)
                if before > start:
                    # these get saved for next map entry
                    temp_ranges.append((start,before-start))

                # range overlap
                #  [ {--] }
                #  { [--] }
                #  { [--} ]
                # max start or entry_start to min end or entry_end
                inter_start = max(start,entry.source_start)
                inter_end = min(end,entry_end)
                if inter_end > inter_start:
                    # these get converted
                    new_ranges.append((inter_start+shift,inter_end-inter_start))

                # range after
                #  { } [--]
                #  { [ }--]
                # max start or entry_end to end
                after = max(start,entry_end)
                if end > after:
                    # these get saved for next map entry
                    temp_ranges.append((after,end-after))
            # re-fill ranges from the saved ranges not overlapping previous map entry
            ranges = temp_ranges
        # Any ranges left don't overlap with map entries so stay same
        new_ranges.extend(ranges)
        return new_ranges

    def mapper(self,value):
        for entry in self.entries:
            if entry.source_start <= value <= entry.source_start + entry.length:
                return value + (entry.destination_start - entry.source_start )
        return value

    def rev_mapper(self,value):
        for entry in self.entries:
            if entry.destination_start <= value <= entry.destination_start + entry.length:
                return value + (entry.source_start - entry.destination_start )
        return value


start = time.time()

with open("input.txt","r") as infile:
    maps = {}
    seeds = []
    wip_map = None
    for l in infile:
        l = l.strip()
        #print(f"=={l}==")
        if len(seeds) == 0:
            seeds = l.split(":")[1].strip().split()
            seeds = [int(seed) for seed in seeds]
        elif l == '':
            if wip_map:
                maps[wip_map.source] = wip_map
            wip_map = Map(None,None,[])
        elif wip_map and not wip_map.destination:
            keys = l.split()[0].split("-")
            wip_map.source = keys[0]
            wip_map.destination = keys[2]
        elif wip_map:
            nums = l.split()
            entry = MapEntry(int(nums[0]),int(nums[1]),int(nums[2]))
            wip_map.entries.append(entry)
    maps[wip_map.source] = wip_map

#print(seeds,maps)

mapped_seeds = {}
closest_seed = None

for seed in seeds:
    next = 'seed'
    value = seed
    #print(next,value)
    mapping = {next:value}
    while next != 'location':
        map : Map = maps[next]
        next = map.destination
        value = map.mapper(value)
        mapping[next] = value
    mapped_seeds[seed] = mapping
    if not closest_seed:
        closest_seed = seed
    if mapped_seeds[closest_seed]['location'] > mapping['location']:
        closest_seed = seed

print("== P1 ==")
print(closest_seed, mapped_seeds[closest_seed]['location'])
print(time.time()-start)

def pairwise(iterable):
    a = iter(iterable)
    return zip(a, a)

# # Full brute force
# # No optimisation
# # 1 seed to 1 location

# closest_location = None

# for x,y in pairwise(seeds):

#     for i in range(0,y):
#         seed = x+i
#         next = 'seed'
#         value = seed
#         #print(next,value)
#         while next != 'location':
#             map : Map = maps[next]
#             next = map.destination
#             value = map.mapper(value)
#             mapping[next] = value
#         if not closest_location:
#             closest_location = value
#         if closest_location > value:
#             closest_location = value
# print("==P2==")
# print(closest_location)

# rev_maps = {}
# for map in maps.values():
#     rev_maps[map.destination] = map

# # Optimisation 1
# # brute force from smallest location to first valid seed

# start = time.time()

# location = -1
# stop = False
# while not stop:
#     location += 1
#     if location % 1000000 == 0:
#         print(location,time.time()-start, end='\r')
#     next = 'location'
#     value = location
#     while next != 'seed':
#         map : Map = rev_maps[next]
#         next = map.source
#         value = map.rev_mapper(value)
#     for x,y in pairwise(seeds):
#         if x <= value <= x+y:
#             stop = True
#             break
# print(location,time.time()-start)

# # Optimisation 2
# # Track the ranges for the seeds through each level, only 1 calculation per range split as required

ranges = []
next = 'seed'

for x,y in pairwise(seeds):
    ranges.append((x,y))
start = time.time()
#print(next,ranges)
while True:
    map : Map = maps[next]
    new_ranges = []
    for (x,y) in ranges:
        new_ranges.extend(map.range_mapper(x,y))
    ranges = new_ranges
    next = map.destination
    #print(next,ranges)
    if next == 'location':
        break

mins = [ v for (v,l) in ranges ]
print(min(mins),time.time()-start)
