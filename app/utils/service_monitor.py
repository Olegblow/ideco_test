import asyncio
import logging
import logging.handlers


class Service:
    """Класс сервис позволяет управлять сервисами."""

    _ctl = 'systemctl'

    def __init__(self, service_name: str):
        self.logger = logging.getLogger('ServiceLogger')
        self.logger.setLevel(logging.DEBUG)
        handler = logging.handlers.SysLogHandler(address='/dev/log')
        self.logger.addHandler(handler)
        self._service_name = service_name

    @property
    def service_name(self) -> str:
        """Возвращает имя сервиса."""
        return self._service_name

    @property
    async def is_active(self) -> bool:
        """Проверяет активный или не активынй сервис.
        Возвращает True или False.
        """
        self.logger.debug('Проверка состояния сервиса.')
        cmd = f'{self._ctl} is-active {self._service_name}'
        proc = await self.async_get_proc(cmd)
        output, _ = await proc.communicate()
        output = output.decode('utf-8').rstrip()
        return 'active' == output

    async def start(self) -> None:
        """Запускает сервис."""
        self.logger.debug('Запуск сервиса')
        cmd = f'{self._ctl} start {self._service_name}'
        proc = await self.async_get_proc(cmd)
        await proc.communicate()

    async def stop(self) -> None:
        """Останавливет сервис."""
        self.logger.debug('Останова сервиса')
        cmd = f'{self._ctl} stop {self._service_name}'
        proc = await self.async_get_proc(cmd)
        await proc.communicate()

    async def restart(self) -> None:
        """Перезапускает севрис."""
        self.logger.debug(' Перезапуск логгера')
        cmd = f'{self._ctl} restart {self._service_name}'
        proc = await self.async_get_proc(cmd)
        await proc.communicate()

    async def async_get_proc(self, cmd: str) -> asyncio.subprocess.Process:
        """Возвращает субпроцесс."""
        proc = await asyncio.create_subprocess_shell(
            cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        return proc
