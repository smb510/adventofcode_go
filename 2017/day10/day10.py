import os
def main():
    twists = "83,0,193,1,254,237,187,40,88,27,2,255,149,29,42,100"
    twists = [ord(x) for x in twists] + [17, 31, 73, 47, 23]
    values = range(256)
    current_position = 0
    skip_size = 0
    for x in xrange(64):
        for twist in twists:
            end = current_position + twist
            end_segment = values[current_position:min(end, len(values))]
            if end > len(values):
                beginning_segment = values[0:end-len(values)]
            else:
                beginning_segment = []
            segment = (end_segment + beginning_segment)[::-1]
            end_length = min(end, len(values)) - current_position
            values[current_position:min(end, len(values))] = segment[:end_length]
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
    print "Part 1", values[0] * values[1]
    print "Part 2", ''.join([hex(x)[2:] for x in dense_hash])
        

if __name__ == '__main__':
    main()
