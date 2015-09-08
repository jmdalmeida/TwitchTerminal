class Printer:

    def print_simple(self, msg):
        print(msg)

    def print_clear(self):
        print("\n" * 100)

    def print_header(self, title):
        tlen = len(title) + 4
        print("*" * tlen)
        print("* {0} *".format(title))
        print("*" * tlen)

    def print_menu(self, channel, streams):
        self.print_clear()
        self.print_header("TWITCH TERMINAL by jmdalmeida")
        print("Account: {0}".format(channel))
        print("Live broadcasts:")
        for x in xrange(len(streams)):
            s = streams[x]
            print("  {0} - {1} - {2} ({3} viewers)".format(str(x + 1),
                                                           str(s['channel']['display_name']),
                                                           str(s['game']),
                                                           str(s['viewers'])))

    def print_help(self):
        self.print_clear()
        self.print_header("HELP")
        print("Available commands:")
        print("  r - reload list")
        print("  pN - open profile page")
        print("  wN - open broadcast")
        print("  cN - open chat")
        print("  (N = number of the stream)")
        print("  q - quit")
        raw_input("Press ENTER to continue...")

    def ask_input(self, msg):
        return raw_input(msg)
