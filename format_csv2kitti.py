import csv
from tqdm import tqdm

def main(args):
    result_tam = []
    print("Reading file")
    with open(args.input_path) as f:
        reader = csv.reader(f)
        data_num = 0
        for i, row in tqdm(enumerate(reader)):
            if args.format == "slam_pose":
                pos_x = float(row[3])
                pos_y = float(row[4])
                pos_z = float(row[5])
                result_tam.append([1, 0, 0, pos_x, 0, 1, 0, pos_y, 0, 0, 1, pos_z])
                data_num += 1
            elif args.format == "utm":
                if i == 0:
                    continue
                # pos_x = float(row[4]) - (-2864096.573149612)
                # pos_y = float(row[5]) - (19826261.91563966)
                pos_y = -(float(row[4]) - (-2864096.573149612))
                pos_x = float(row[5]) - (19826261.91563966)
                pos_z = float(row[6]) - (21.235)
                result_tam.append([1, 0, 0, pos_x, 0, 1, 0, pos_y, 0, 0, 1, pos_z])
                data_num += 1
            else:
                raise ValueError("Unknown format")
    print(f"Loaded total {data_num} data")
    
    with open(args.output_path, 'w') as f:
        for row in tqdm(result_tam):
            f.write(' '.join([str(item) for item in row]))
            f.write('\n')
    print("Done!")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_path", type=str, required=True, help="input file path")
    parser.add_argument("--output_path", type=str, required=True, help="output file path")
    parser.add_argument("--format", type=str, required=True, choices=["slam_pose", "utm"], help="format of the input file")
    args = parser.parse_args()
    main(args)