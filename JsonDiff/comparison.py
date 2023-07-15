from deepdiff import DeepDiff
import sys
import argparse
import json


def main():
    parser = argparse.ArgumentParser(description='JSON File Comparison')
    parser.add_argument('ref_json', type=str, help='first/reference json file') # Ex:  ../Resources/ref.json
    parser.add_argument('target_json', type=str, help='second/target json file to be compared with')  # Ex:  ../Resources/target.json
    args = parser.parse_args()

    ref_json_dict: dict = json.load(open(args.ref_json))
    target_json_dict: dict = json.load(open(args.target_json))
    result = DeepDiff(ref_json_dict, target_json_dict)
    print(result)


if __name__ == '__main__':
    main()