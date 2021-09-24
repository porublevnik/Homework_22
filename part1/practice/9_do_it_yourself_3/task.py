from __future__ import annotations
import sys
from typing import List
#### Блок кода для перехвата вывода в консоль ####

output_data = []


def print(s):
    if not isinstance(s, str):
        s = str(s)
    sys.stdout.write(s)
    sys.stdout.write('\n')
    output_data.append(s)


#### /Блок кода для перехвата вывода в консоль ####

# Стартовый код


class ServerConnectionError(Exception):
    pass

class Server:
    pass


class BuildServer:

    def __init__(self, title: str):
        self.title = title
        self.opened_ports = set()
        self.visible_servers = set()

    def add_ports(self, ports: List[int]):
        self.opened_ports |= set(ports)

    def add_visible_server(self, server_title: str):
        self.visible_servers.add(server_title)

    def get_title(self) -> str:
        return self.title

    def get_opened_ports(self) -> set:
        return self.opened_ports

    def get_visitable_severs(self) -> set:
        return self.visible_servers

    def check_connection(self, server_1, server_2):
        if not self._check_visibility(server_1, server_2) & self._check_opened_ports(server_1, server_2):
            raise ServerConnectionError(
                f" Servers {server_1.__class__.__name__} and {server_2.__class__.__name__} have no connection")

    def _check_visibility(self, server_1, server_2):
        title_1 = server_1.get_title()
        title_2 = server_2.get_title()
        return all(
            [self._check_is_visible_server(title_1, server_2),
             self._check_is_visible_server(title_2, server_1)]
        )

    @staticmethod
    def _check_is_visible_server(title: str, server) -> bool:
        return title in server.visible_servers

    @staticmethod
    def _check_opened_ports(server_1, server_2):
        return bool(server_1.get_opened_ports() & server_2.get_opened_ports())

    def make_connection_between_to_servers(self, server_1, server_2, ports: List[int]):
        self._set_visitable_servers(server_1, server_2)
        self._set_visitable_ports(server_1=server_1, server_2=server_2, ports=ports)

    def _set_visitable_servers(self, server_1, server_2):
        title_1 = server_1.get_title()
        title_2 = server_2.get_title()
        server_1.add_visible_server(title_2)
        server_2.add_visible_server(title_1)

    def _set_visitable_ports(self, server_1, server_2, ports: List[int]):
        server_1.add_ports(ports)
        server_2.add_ports(ports)


class DataBaseServer:

    def __init__(self, title: str):
        self.title = title
        self.opened_ports = set()
        self.visible_servers = set()

    def add_ports(self, ports: List[int]):
        self.opened_ports |= set(ports)

    def add_visible_server(self, server_title: str):
        self.visible_servers.add(server_title)

    def get_title(self) -> str:
        return self.title

    def get_opened_ports(self) -> set:
        return self.opened_ports

    def get_visitable_severs(self) -> set:
        return self.visible_servers

    def check_connection(self, server_1, server_2):
        if not self._check_visibility(server_1, server_2) & self._check_opened_ports(server_1, server_2):
            raise ServerConnectionError(
                f" Servers {server_1.__class__.__name__} and {server_2.__class__.__name__} have no connection")

    def _check_visibility(self, server_1, server_2):
        title_1 = server_1.get_title()
        title_2 = server_2.get_title()
        return all(
            [self._check_is_visible_server(title_1, server_2),
             self._check_is_visible_server(title_2, server_1)]
        )

    @staticmethod
    def _check_is_visible_server(title: str, server) -> bool:
        return title in server.visible_servers

    @staticmethod
    def _check_opened_ports(server_1, server_2):
        return bool(server_1.get_opened_ports() & server_2.get_opened_ports())

    def add_record(self, record):
        print(f'New record in DB - {record}')


class MailServer:

    def __init__(self, title: str):
        self.title = title
        self.opened_ports = set()
        self.visible_servers = set()

    def add_ports(self, ports: List[int]):
        self.opened_ports |= set(ports)

    def add_visible_server(self, server_title: str):
        self.visible_servers.add(server_title)

    def get_title(self) -> str:
        return self.title

    def get_opened_ports(self) -> set:
        return self.opened_ports

    def get_visitable_severs(self) -> set:
        return self.visible_servers

    def check_connection(self, server_1, server_2):
        if not self._check_visibility(server_1, server_2) & self._check_opened_ports(server_1, server_2):
            raise ServerConnectionError(
                f" Servers {server_1.__class__.__name__} and {server_2.__class__.__name__} have no connection")

    def _check_visibility(self, server_1, server_2):
        title_1 = server_1.get_title()
        title_2 = server_2.get_title()
        return all(
            [self._check_is_visible_server(title_1, server_2),
             self._check_is_visible_server(title_2, server_1)]
        )

    @staticmethod
    def _check_is_visible_server(title: str, server) -> bool:
        return title in server.visible_servers

    @staticmethod
    def _check_opened_ports(server_1, server_2):
        return bool(server_1.get_opened_ports() & server_2.get_opened_ports())

    def send_mail(self, message, _to: MailServer):
        self.check_connection(server_1=self, server_2=_to)
        _to.get_mail(message=message, _from=self)

    def get_mail(self, message, _from: MailServer):
        print(f'We get message = "{message}" from {_from.__class__.__name__}')


class WebServer:

    def __init__(self, title: str):
        self.title = title
        self.opened_ports = set()
        self.visible_servers = set()

    def add_ports(self, ports: List[int]):
        self.opened_ports |= set(ports)

    def add_visible_server(self, server_title: str):
        self.visible_servers.add(server_title)

    def get_title(self) -> str:
        return self.title

    def get_opened_ports(self) -> set:
        return self.opened_ports

    def get_visitable_severs(self) -> set:
        return self.visible_servers

    def check_connection(self, server_1, server_2):
        if not self._check_visibility(server_1, server_2) & self._check_opened_ports(server_1, server_2):
            raise ServerConnectionError(
                f" Servers {server_1.__class__.__name__} and {server_2.__class__.__name__} have no connection")

    def _check_visibility(self, server_1, server_2):
        title_1 = server_1.get_title()
        title_2 = server_2.get_title()
        return all(
            [self._check_is_visible_server(title_1, server_2),
             self._check_is_visible_server(title_2, server_1)]
        )

    @staticmethod
    def _check_is_visible_server(title: str, server) -> bool:
        return title in server.visible_servers

    @staticmethod
    def _check_opened_ports(server_1, server_2):
        return bool(server_1.get_opened_ports() & server_2.get_opened_ports())

    def run_web_application(self):
        print('Yahoo! We are online!')

    def error_report(self, _from: MailServer, _to: MailServer):
        self.check_connection(server_1=self, server_2=_from)
        _from.send_mail(message='Something Wrong', _to=_to)

    def save_order(self, db: DataBaseServer):
        self.check_connection(server_1=self, server_2=db)
        db.add_record(record='We got new oder!')


# Все объекты для работы магазина созданы корректно и в достаточном количестве
build_server = BuildServer(title='Build Machine')
db = DataBaseServer(title='DataBase')
report_mail_server = MailServer(title='Report Server')
maintainers_mail_server = MailServer(title='Maintainers Mailboxes')
web = WebServer(title='Our Site')

# Проверим - работает ли наш магазин
web.run_web_application()
web.save_order(db=db)
web.error_report(_from=report_mail_server, _to=maintainers_mail_server)


# Тесты
def test_assert(condition, correct, incorrect):
    try:
        assert condition, incorrect
        print(correct)
    except AssertionError as e:
        print(e.args[0])

test_assert(
    output_data == ["Yahoo! We are online!",
                    "New record in DB - We got new oder!",
                    'We get message = "Something Wrong" from MailServer',
                    ], correct='Вывод в консоль верный',
    incorrect='Вывод в консоль НЕ верный')


test_assert('Server' in globals(), correct='Выделен общий класс Server',
            incorrect='Нужно определить класс-родитель Server')
test_assert('add_ports' in Server.__dict__, correct='У класса Server есть метод "add_ports"',
            incorrect='У класса Server отсутствует метод "add_ports"')
test_assert('add_visible_server' in Server.__dict__, correct='У класса Server есть метод "add_visible_server"',
            incorrect='У класса Server отсутствует метод "add_visible_server"')
test_assert('get_title' in Server.__dict__, correct='У класса Server есть метод "get_title"',
            incorrect='У класса Server отсутствует метод "get_title"')
test_assert('get_opened_ports' in Server.__dict__, correct='У класса Server есть метод "get_opened_ports"',
            incorrect='У класса Server отсутствует метод "get_opened_ports"')
test_assert('get_visitable_severs' in Server.__dict__, correct='У класса Server есть метод "get_visitable_severs"',
            incorrect='У класса Server отсутствует метод "get_visitable_severs"')
test_assert('check_connection' in Server.__dict__, correct='У класса Server есть метод "check_connection"',
            incorrect='У класса Server отсутствует метод "check_connection"')
test_assert('_check_visibility' in Server.__dict__, correct='У класса Server есть метод "_check_visibility"',
            incorrect='У класса Server отсутствует метод "_check_visibility"')
test_assert('_check_is_visible_server' in Server.__dict__,
            correct='У класса Server есть метод "_check_is_visible_server"',
            incorrect='У класса Server отсутствует метод "_check_is_visible_server"')
test_assert('_check_opened_ports' in Server.__dict__, correct='У класса Server есть метод "_check_opened_ports"',
            incorrect='У класса Server отсутствует метод "_check_opened_ports"')

