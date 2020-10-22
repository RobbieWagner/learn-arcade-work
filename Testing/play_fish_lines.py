
def play_fish_lines():
    fish_lines = open("DJFishLipsLines.txt")
    fish_lines_list = []

    for line in fish_lines:
        line = line.strip
        fish_lines_list.append(line)
    fish_lines.close()
