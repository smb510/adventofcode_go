def main():
    strings = ["ljoxqyyw-" + str(x) for x in range(128)]
    hashes = [calculate_dense_hash(x) for x in strings]
    counts = [len(filter(lambda y: y == 1, x)) for x in hashes]
    print "Part 1 ", sum(counts)
    print "Part 2 ", calculate_components(hashes)

def calculate_components(hashes):
    sum = 0
    for i in range(len(hashes)):
        for j in range(len(hashes[0])):
            sum += flood_fill(hashes, i, j)
    return sum

def flood_fill(hashes, row, col):
    left = None if col == 0 else col - 1
    right = None if col == len(hashes[0]) - 1 else col + 1
    up = None if row == 0 else row - 1
    down = None if row == len(hashes) - 1 else row + 1
    if hashes[row][col] == 1:
        hashes[row][col] = 2
        if left is not None:
            flood_fill(hashes, row, left)
        if right is not None:
            flood_fill(hashes, row, right)
        if up is not None:
            flood_fill(hashes, up, col)
        if down is not None:
            flood_fill(hashes, down, col)
        return 1
    return 0





def calculate_dense_hash(str_):
    twists = [ord(x) for x in str_] + [17, 31, 73, 47, 23]
    values = range(256)
    current_position = 0
    skip_size = 0
    for x in xrange(64):
        for twist in twists:
            end = current_position + twist
            end_segment = values[current_position:min(end, len(values))]
            if end > len(values):
                beginning_segment = values[0:end - len(values)]
            else:
                beginning_segment = []
            segment = (end_segment + beginning_segment)[::-1]
            end_length = min(end, len(values)) - current_position
            values[current_position:min(end, len(values))] = segment[
                :end_length]
            if end > len(values):
                values[0:end - len(values)] = segment[end_length:]
            current_position += twist + skip_size
            current_position = current_position % len(values)
            skip_size += 1
    dense_hash = []
    for x in xrange(16):
        sparse = values[16 * x:16 * x + 16]
        dh = reduce(lambda a, b: a ^ b, sparse)
        dense_hash.append(dh)
    val =  ''.join(["{0:08b}".format(x) for x in dense_hash])
    val = [int(x) for x in val]
    return val

if __name__ == '__main__':
    main()