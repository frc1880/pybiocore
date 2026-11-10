from typing import override

import magicbot


class Jackie(magicbot.MagicRobot):
    @override
    def create_objects(self) -> None:
        pass

    @override
    def disabled_init(self) -> None:
        pass

    @override
    def disabled_periodic(self) -> None:
        pass

    @override
    def teleop_init(self) -> None:
        pass

    @override
    def teleop_periodic(self) -> None:
        pass
