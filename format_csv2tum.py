import csv
from tqdm import tqdm

def main(args):
    result_tam = []
    print("Reading file")
    with open(args.input_path) as f:
        reader = csv.reader(f)
        origin
        for i, row in tqdm(enumerate(reader)):
            if args.format == "slam_pose":
                time = int(row[0])
                pos_x = float(row[3])
                pos_y = float(row[4])
                pos_z = float(row[5])
                qx = float(row[6])
                qy = float(row[7])
                qz = float(row[8])
                qw = float(row[9])
                result_tam.append([time, pos_x, pos_y, pos_z, qx, qy, qz, qw])
            elif args.format == "utm":
                if i == 0:
                    continue
                time = int(row[0])
                pos_x = float(row[4])
                pos_y = float(row[5])
                pos_z = float(row[6])
                qx = float(row[7])
                qy = float(row[8])
                qz = float(row[9])
                qw = float(row[10])
                result_tam.append([time, pos_x, pos_y, pos_z, qx, qy, qz, qw])
            else:
                raise ValueError("Unknown format")
    
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