def filestats():
    while True:
        try:
            filepath = input("Please enter your filepath for analysis: ")
            total_lines_count = 0
            empty_lines_count = 0
            lines_with_z_count = 0
            lines_with_and_count = 0

            with open(filepath, 'r') as f:
                for lines in f:
                    if lines:
                        total_lines_count += 1
                    if not lines.split():
                        empty_lines_count += 1
                    if "z" in lines:
                        lines_with_z_count += 1
                    if "and" in lines:
                        lines_with_and_count += 1

            print('total lines: ', total_lines_count)
            print('empty lines: ', empty_lines_count)
            print('lines with "z": ', lines_with_z_count)
            print('lines with "and": ', lines_with_and_count)
            break
        except Exception as error:
            print("Error:", error)
            continue
    answer = input("Do you want to analyze one more file?: Y/N: ")


filestats()
