import logging
from lptp.server import LPTPServer, Manager
from lptp.types import AuthType

logging.basicConfig(level=logging.DEBUG)

server = LPTPServer(
    "127.0.0.1",
    auth_type = AuthType.Key,
    key = "someKey"
)

manager = Manager()

@manager.procedure
async def reverse_text(text: str) -> str:
    return text[::-1]

@manager.procedure
async def sum_numbers(a: int, b: int) -> int:
    return a + b

@manager.sub_procedure(sum_numbers, 1)
async def sum_numbers_list(nums: list) -> int:
    return sum(nums)

server.add_manager(manager)
server.generate_proc_file()
server.run_forever()