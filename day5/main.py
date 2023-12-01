from dataclasses import dataclass

almanac_file = "./day5/almanac.txt"

@dataclass
class Conversion:
    source_start: int
    source_end: int
    dest_start: int
    dest_end: int
    range: int

@dataclass
class RatioMap:
    converstions: list[Conversion]


def do_converstion(ratio_map, value):
    for conversion in ratio_map.converstions:
        if conversion.source_start <= value <= conversion.source_end:
            return conversion.dest_start + (value - conversion.source_start)
        
    return value

def part1(seeds, seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temp, temp_to_humidity, humidity_to_location):
    result_locations = []
    completed = 0
    for seed in seeds:
        soil = do_converstion(seed_to_soil, seed)
        fertilizer = do_converstion(soil_to_fertilizer, soil)
        water = do_converstion(fertilizer_to_water, fertilizer)
        light = do_converstion(water_to_light, water)
        temp = do_converstion(light_to_temp, light)
        humidity = do_converstion(temp_to_humidity, temp)
        location = do_converstion(humidity_to_location, humidity)
        result_locations.append(location)
        completed += 1

        if completed % 100000 == 0:
            print(f"Percent completed: {completed / len(seeds) * 100}%")
    
    # return lowest location
    return min(result_locations)

def part2(seeds, seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temp, temp_to_humidity, humidity_to_location):
    new_seeds = []
    index = 0
    while index < len(seeds):
        start = seeds[index]
        num = seeds[index+1]
        for j in range(start, start+num):
            new_seeds.append(j)
        index += 2
    
    print(f"Number of new seeds: {len(new_seeds)}")    

    print("Computing part 2...")
    return part1(new_seeds, seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temp, temp_to_humidity, humidity_to_location)

def main():
    seeds = []
    seed_to_soil = RatioMap([])
    soil_to_fertilizer = RatioMap([])
    fertilizer_to_water = RatioMap([])
    water_to_light = RatioMap([])
    light_to_temp = RatioMap([])
    temp_to_humidity = RatioMap([])
    humidity_to_location = RatioMap([])

    with open(almanac_file, 'r') as f:
        lines = f.readlines()

    index = 0
    while index < len(lines):
        line = lines[index]
        if "seeds:" in line:
            seeds = line.split(": ")[1].split(" ")
            seeds = [int(s) for s in seeds]
        elif "seed-to-soil map:" in line:
            index += 1
            while lines[index] != "\n":
                line = lines[index]
                line = line.replace("\n", "")
                line = line.split(" ")
                nums = [int(c) for c in line]
                conversion = Conversion(
                    source_start=int(nums[1]),
                    source_end=int(nums[1] + nums[2]),
                    dest_start=int(nums[0]),
                    dest_end=int(nums[0] + nums[2]),
                    range=int(line[2])
                )
                seed_to_soil.converstions.append(conversion)
                index += 1
        elif "soil-to-fertilizer map:" in line:
            index += 1
            while lines[index] != "\n":
                line = lines[index]
                line = line.replace("\n", "")
                line = line.split(" ")
                nums = [int(c) for c in line]
                conversion = Conversion(
                    source_start=int(nums[1]),
                    source_end=int(nums[1] + nums[2]),
                    dest_start=int(nums[0]),
                    dest_end=int(nums[0] + nums[2]),
                    range=int(line[2])
                )
                soil_to_fertilizer.converstions.append(conversion)
                index += 1
        elif "fertilizer-to-water map:" in line:
            index += 1
            while lines[index] != "\n":
                line = lines[index]
                line = line.replace("\n", "")
                line = line.split(" ")
                nums = [int(c) for c in line]
                conversion = Conversion(
                    source_start=int(nums[1]),
                    source_end=int(nums[1] + nums[2]),
                    dest_start=int(nums[0]),
                    dest_end=int(nums[0] + nums[2]),
                    range=int(line[2])
                )
                fertilizer_to_water.converstions.append(conversion)
                index += 1
        elif "water-to-light map:" in line:
            index += 1
            while lines[index] != "\n":
                line = lines[index]
                line = line.replace("\n", "")
                line = line.split(" ")
                nums = [int(c) for c in line]
                conversion = Conversion(
                    source_start=int(nums[1]),
                    source_end=int(nums[1] + nums[2]),
                    dest_start=int(nums[0]),
                    dest_end=int(nums[0] + nums[2]),
                    range=int(line[2])
                )
                water_to_light.converstions.append(conversion)
                index += 1
        elif "light-to-temperature map:" in line:
            index += 1
            while lines[index] != "\n":
                line = lines[index]
                line = line.replace("\n", "")
                line = line.split(" ")
                nums = [int(c) for c in line]
                conversion = Conversion(
                    source_start=int(nums[1]),
                    source_end=int(nums[1] + nums[2]),
                    dest_start=int(nums[0]),
                    dest_end=int(nums[0] + nums[2]),
                    range=int(line[2])
                )
                light_to_temp.converstions.append(conversion)
                index += 1

        elif "temperature-to-humidity map:" in line:
            index += 1
            while lines[index] != "\n":
                line = lines[index]
                line = line.replace("\n", "")
                line = line.split(" ")
                nums = [int(c) for c in line]
                conversion = Conversion(
                    source_start=int(nums[1]),
                    source_end=int(nums[1] + nums[2]),
                    dest_start=int(nums[0]),
                    dest_end=int(nums[0] + nums[2]),
                    range=int(line[2])
                )
                temp_to_humidity.converstions.append(conversion)
                index += 1
        elif "humidity-to-location map:" in line:
            index += 1
            while lines[index] != "\n":
                line = lines[index]
                line = line.replace("\n", "")
                line = line.split(" ")
                nums = [int(c) for c in line]
                conversion = Conversion(
                    source_start=int(nums[1]),
                    source_end=int(nums[1] + nums[2]),
                    dest_start=int(nums[0]),
                    dest_end=int(nums[0] + nums[2]),
                    range=int(line[2])
                )
                humidity_to_location.converstions.append(conversion)
                index += 1
        index += 1

    print(part1(seeds, seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temp, temp_to_humidity, humidity_to_location))
    print(part2(seeds, seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temp, temp_to_humidity, humidity_to_location))

main()