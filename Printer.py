import math


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
                                                           s['channel']['display_name'].encode('utf-8'),
                                                           s['game'].encode('utf-8'),
                                                           str(self.prettify(s['viewers']))))

    def print_info(self, s):
        self.print_clear()
        self.print_header("INFO")
        print("Name: {0}".format(s['channel']['display_name'].encode('utf-8')))
        print("Status: {0}".format(s['channel']['status'].encode('utf-8')))
        print("Game: {0}".format(s['game'].encode('utf-8')))
        print("Viewers: {0}".format(str(self.prettify(s['viewers']))))
        print("FPS: {0}".format(str(math.ceil(s['average_fps']))))
        print("Partner: {0}".format(
            "Yes" if s['channel']['partner'] else "No"))
        print("Mature: {0}".format(
            "Yes" if s['channel']['mature'] else "No"))
        print("Language: {0}".format(s['channel']['language']))
        print("Followers: {0}".format(
            str(self.prettify(s['channel']['followers']))))
        print("Views: {0}".format(str(self.prettify(s['channel']['views']))))
        print("Created at: {0}".format(s['channel']['created_at'][:10]))
        self.ask_input("Press ENTER to continue...")

    def print_help(self):
        self.print_clear()
        self.print_header("HELP")
        print("Available commands:")
        print("  r - reload list")
        print("  pN - open profile page")
        print("  wN - open broadcast")
        print("  cN - open chat")
        print("  iN - show info")
        print("  (N = number of the stream)")
        print("  q - quit")
        self.ask_input("Press ENTER to continue...")

    def ask_input(self, msg):
        return raw_input(msg)

    def prettify(self, n):
        return "{:,}".format(n)
