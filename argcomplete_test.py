# argcomplete_test.py
import argparse
import argcomplete

def main():
    parser = argparse.ArgumentParser(description="Test Argcomplete")
    parser.add_argument('--option', help='An example option')
    parser.add_argument('--number', type=int, help='An example number')

    # Enable argcomplete for this parser
    argcomplete.autocomplete(parser)

    args = parser.parse_args()
    print(f"Option: {args.option}")
    print(f"Number: {args.number}")

if __name__ == "__main__":
    main()
