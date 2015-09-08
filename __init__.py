import pdb

from App import App
from TwitchAPI import TwitchAPI
import config


def main():
    app = App(config)
    app.run()

if __name__ == "__main__":
    main()
