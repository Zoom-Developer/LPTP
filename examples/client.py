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