# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class CounterpartyNetworkType(str, enum.Enum):
    ENTITY = "ENTITY"
    NETWORK = "NETWORK"

    def visit(self, entity: typing.Callable[[], T_Result], network: typing.Callable[[], T_Result]) -> T_Result:
        if self is CounterpartyNetworkType.ENTITY:
            return entity()
        if self is CounterpartyNetworkType.NETWORK:
            return network()
