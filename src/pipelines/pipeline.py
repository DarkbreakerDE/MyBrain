import builtins
import inspect


class Pipline:

    def __init__(self, *args) -> None:
        self._args = list(args)

    def run(self, *args):
        for step in self._args:
            sig = inspect.signature(step)
            params = list(sig.parameters.values())

            required = [
                p
                for p in params
                if p.default is inspect.Parameter.empty
                and p.kind in (p.POSITIONAL_ONLY, p.POSITIONAL_OR_KEYWORD)
            ]

            accepts_varargs = any(
                p.kind == inspect.Parameter.VAR_POSITIONAL for p in params
            )

            total_allowed = len(
                [
                    p
                    for p in params
                    if p.kind in (p.POSITIONAL_ONLY, p.POSITIONAL_OR_KEYWORD)
                ]
            )

            if not accepts_varargs and not (
                len(required) <= len(args) <= total_allowed
            ):
                raise TypeError(
                    f"Step {step.__name__} expects between {len(required)} and {total_allowed} arguments, "
                    f"but got {len(args)}: {args}"
                )
            elif accepts_varargs and len(args) < len(required):
                raise TypeError(
                    f"Step {step.__name__} requires at least {len(required)} arguments, "
                    f"but got {len(args)}: {args}"
                )

            # Führe aus – übergebe alle args, egal ob *args erlaubt oder nicht
            result = step(*args)

            # Ergebnis wird wieder als neues args-Tupel durchgereicht
            args = (result,) if not isinstance(result, tuple) else result

        return args[0] if len(args) == 1 else args


class Printer:
    def __init__(self, prefix=""):
        self.prefix = prefix

    def __call__(self, *args, **kwargs):
        builtins.print(self.prefix, *args, **kwargs)
        if args and kwargs:
            return args, kwargs
        elif args:
            return args
        elif kwargs:
            return kwargs
        else:
            return None


printer = Printer()


class Map_Args:
    def __call__(self, func, *args):
        return tuple(func(arg) for arg in args)


map_args = Map_Args()
