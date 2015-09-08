import pdb

from TwitchAPI import TwitchAPI
from Printer import Printer

import os
import webbrowser
import subprocess
import shlex


class App:

    def __init__(self, _config):
        self.config = _config
        self.api = TwitchAPI()
        self.printer = Printer()

    def run(self):
        self.set_streams_list()
        # Main loop
        while True:
            self.printer.print_menu(self.config.CHNL, self.streams)
            c = self.printer.ask_input("Command (h for help): ")
            if len(c) is 0:
                pass
            elif c is "h":  # help
                self.printer.print_help()
            elif c is "q":  # quit app
                self.printer.print_simple("Exiting...")
                break
            elif c is "r":  # reload list
                self.printer.print_simple("Reloading list...")
                self.set_streams_list()
            elif c[0] is "p":  # open profile page
                n = self.get_command_number(c, len(self.streams))
                if n is not None:
                    stream = self.streams[n]
                    cmd = "python -m webbrowser -t '{0}'".format(
                            stream['channel']['url'] + "/profile")
                    self.open_subprocess(cmd)
            elif c[0] is "c": # open the chat window
                n = self.get_command_number(c, len(self.streams))
                if n is not None:
                    stream = self.streams[n]
                    cmd = "python -m webbrowser -t '{0}'".format(
                            stream['channel']['url'] + "/chat?popout=")
                    self.open_subprocess(cmd)
            elif c[0] is "w":  # open the broadcast
                n = self.get_command_number(c, len(self.streams))
                if n is not None:
                    stream = self.streams[n]
                    cmd = "livestreamer {0} {1} -p {2}".format(
                            stream['channel']['url'], self.config.QLTY, self.config.SFTW)
                    self.open_subprocess(cmd)

    def get_command_number(self, cmd, slen):
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

    def set_streams_list(self):
        if self.config.RAUT:
            self.streams = self.api.get_online_followed_channels_oauth(
                self.config.AUTH)
        else:
            self.streams = self.api.get_online_followed_channels(
                self.config.CHNL)
