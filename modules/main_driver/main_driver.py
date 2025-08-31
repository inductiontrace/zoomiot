"""Main driver for the RC car firmware modules."""


class MainDriver:
    """Registers modules and shuffles messages between them."""

    def __init__(self):
        self.modules = {}
        self.mailboxes = {}

    def register(self, name, module):
        """Register a module with a mailbox."""
        self.modules[name] = module
        self.mailboxes[name] = []

    def send(self, target, message):
        """Queue a message for a module."""
        if target in self.mailboxes:
            self.mailboxes[target].append(message)

    def run_once(self):
        """Call `tick` on each module once."""
        for name in self.modules:
            module = self.modules[name]
            inbox = self.mailboxes.get(name, [])
            self.mailboxes[name] = []

            def send_mail(target, msg):
                if target in self.mailboxes:
                    self.mailboxes[target].append(msg)

            module.tick(inbox, send_mail)
