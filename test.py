#  __________________
#  Import LIBRARIES
from typing import Annotated, Any, get_type_hints, get_origin, get_args
from functools import wraps
#  Import FILES
#  __________________

#  on line 7 should it be "get_type_hints(    func    , include_extras =True") intead of "get_type_hints(   double    , include_extras =True)"


def check_value_range(
    func,
):  # -> _Wrapped[Callable[..., Any], Any, Callable[..., Any], Any]:
    @wraps(func)
    def wrapped(x):
        type_hints: dict[str, Any] = get_type_hints(double, include_extras=True)
        hint = type_hints["x"]
        if get_origin(hint) is Annotated:
            hint_type, *hint_args = get_args(hint)
            low, high = hint_args[0]
            print(f"low = {low}")
            print(f"high = {high}")

            if not low <= x <= high:
                raise ValueError(f"-- {x} fallsoutside boundary {low}-{high}")
        #  Execute function once all checks passed
        return func(x)

    return wrapped


@check_value_range
def double(x: Annotated[int, (0, 100)]) -> int:
    # type_hints: dict[str, Any] = get_type_hints(double, include_extras=True)
    # # print(type_hints)
    # hint = type_hints["x"]
    # if get_origin(hint) is Annotated:
    #     hint_type, *hint_args = get_args(hint)
    #     low, high = hint_args[0]
    #     # print(f"hint_type = {hint_type}")  # int
    #     # print(f"Int_args  = {hint_args}")  # The value
    #     print(f"low = {low}")
    #     print(f"high = {high}")

    #     if not low <= x <= high:
    #         raise ValueError(f"-- {x} fallsoutside boundary {low}-{high}")

    # # print(hint)
    # # def double(x: int) -> int:
    return x * 2


result = double(4)
print(f"Result = {result}")
result = double(15)
print(f"Result = {result}")
result = double(400)
print(f"Result = {result}")
