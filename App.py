from Commands import CommandsManager
from TwitchAPI import TwitchAPI
from Printer import Printer

import os
import subprocess
import shlex


class App:

    def __init__(self, _config):
        self.config = _config
        self.api = TwitchAPI()
        self.printer = Printer()
        self.cm = CommandsManager(self)

    def run(self):
        self.printer.print_simple("Loading...")
        self.fetch_streams_list()
        # Main loop
        while True:
            self.printer.print_menu(self.config.CHNL, self.streams)
            c = self.printer.ask_input("Command (h for help): ")
            c = c.strip()
            if not c:
                continue
            self.cm.run_command(c)

    def get_command_number(self, cmd):
        slen = len(self.streams)
        try:
            n = int(cmd[1:]) - 1
            if n >= 0 and n < slen:
                return n
            else:
                return None
        except ValueError:
            return None

    def open_subprocess(self, cmd):
        '''
        Open a new process without it taking ownership of the terminal.
        '''
        p = None
        savout = os.dup(1)
        os.close(1)
        os.open(os.devnull, os.O_RDWR)
        try:
            args = shlex.split(cmd)
            p = subprocess.Popen(args)
        finally:
            os.dup2(savout, 1)
        return p

    def fetch_streams_list(self):
        self.streams = self.api.get_live_followed_channels(self.config.CHNL)

