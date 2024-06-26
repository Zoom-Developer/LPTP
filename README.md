# Lite Procedure Transfer Protocol (LPTP)
*Данный протокол является протоколом RPC вида и служит для вызова процедур на удалённом сервере. Проект является исключительно учебным и не рекомендуется для реального использования.*

## Установка

`pip install lptp`

## Пример использования

### Клиент
```python
import asyncio
from lptp.client import LPTPClient
from lptp.types import AuthType
from lptp_procedures import ProcedureManager

async def main():
    async with ProcedureManager(LPTPClient(
        "127.0.0.1",
        auth_type=AuthType.Key,
        key="someKey"
    )) as proc:

        print(await proc.reverse_text("Привет Пацаны"))

asyncio.run(main())
```

### Сервер
```python
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
```

## Важно
*При запуске серверсайда необходимо вызвать метод generate_proc_file(), который создаст в текущей директории файл lptp_procedures.py с описанием всех процедур сервера. Работа клиентской стороны невозможна без этого файла.*