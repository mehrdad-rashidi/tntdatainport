import imaplib


class EmailPars:
    __imap_server = None
    __imap_port = None
    __email_address = None
    __password = None
    __mailbox = None
    __imap_connect = None

    def __init__(self, imap_server, imap_port, email_address, password, mailbox):
        self.imap_server = imap_server
        self.imap_port = imap_port
        self.email_address = email_address
        self.password = password
        self.mailbox = mailbox
        self.imap_connect = imaplib.IMAP4_SSL(imap_server, imap_port)

    def login(self):
        """
        Log in to the IMAP server.

        Returns:
        - imap: The IMAP4_SSL instance

        Raises:
        - Exception: If login fails
        """
        try:
            self.imap_connect.login(self.email_address, self.password)
            print("Login successful.")
            return self.imap_connect
        except imaplib.IMAP4_SSL.error as e:
            raise Exception("IMAP4_SSL error:", e)
        except imaplib.IMAP4.error as e:
            raise Exception("IMAP4 error:", e)

    @property
    def imap_server(self):
        return self.__imap_server

    @property
    def imap_port(self):
        return self.__imap_port

    @property
    def email_address(self):
        return self.__email_address

    @property
    def password(self):
        return self.__password

    @property
    def mailbox(self):
        return self.__mailbox

    @property
    def imap_connect(self):
        return self.__imap_connect

    @imap_server.setter
    def imap_server(self, imap_server):
        self.__imap_server = imap_server

    @imap_port.setter
    def imap_port(self, imap_port):
        self.__imap_server = imap_port

    @email_address.setter
    def email_address(self, email_address):
        self.__email_address = email_address

    @password.setter
    def password(self, password):
        self.__password = password

    @mailbox.setter
    def mailbox(self, mailbox):
        self.__mailbox = mailbox

    @imap_connect.setter
    def imap_connect(self, imap_connect):
        self.__imap_connect = imap_connect
