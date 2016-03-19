import sys

class CommandsManager:

    def __init__(self, app):
        self.app = app
        self.setup_commands()

    def setup_commands(self):
        self.commands = {}
        self.add_command('h', Commands.help)
        self.add_command('q', Commands.quit)
        self.add_command('r', Commands.reload_stream_list)
        self.add_command('p', Commands.open_profile)
        self.add_command('c', Commands.open_chat)
        self.add_command('w', Commands.open_broadcast)
        self.add_command('i', Commands.list_info)

    def add_command(self, identifier, callback):
        c = Command(identifier, callback)
        self.commands[identifier] = c

    def run_command(self, command):
        identifier = command[0]
        if not identifier or not self.commands[identifier]:
            return False
        Commands.c = command
        self.commands[identifier].run(self.app)

class Command:

    def __init__(self, identifier, callback):
        self.identifier = identifier
        self.callback = callback

    def run(self, app):
        self.callback(app)

class Commands:
    c = None

    @staticmethod
    def help(app):
        app.printer.print_help()

    @staticmethod
    def quit(app):
        app.printer.print_simple("Exiting...")
        sys.exit(0)

    @staticmethod
    def reload_stream_list(app):
        app.printer.print_simple("Reloading list...")
        app.fetch_streams_list()

    @staticmethod
    def open_profile(app):
        n = app.get_command_number(Commands.c)
        if n is not None:
            stream = app.streams[n]
            cmd = "python -m webbrowser -t '{0}'".format(stream['channel']['url'] + "/profile")
            app.open_subprocess(cmd)

    @staticmethod
    def open_chat(app):
        n = app.get_command_number(Commands.c)
        if n is not None:
            stream = app.streams[n]
            cmd = "python -m webbrowser -t '{0}'".format(stream['channel']['url'] + "/chat?popout=")
            app.open_subprocess(cmd)

    @staticmethod
    def open_broadcast(app):
        n = app.get_command_number(Commands.c)
        if n is not None:
            stream = app.streams[n]
            cmd = "livestreamer {0} {1} -p {2}".format(
                stream['channel']['url'],
                app.config.QLTY,
                app.config.SFTW)
            app.open_subprocess(cmd)

    @staticmethod
    def list_info(app):
        n = app.get_command_number(Commands.c)
        if n is not None:
            stream = app.streams[n]
            app.printer.print_info(stream)

