from dotenv import load_dotenv
import os


def main():
    load_dotenv()
    SQUARE_ACCESS_TOKEN = os.environ["SQUARE_ACCESS_TOKEN"]


if __name__ == "__main__":
    main()
