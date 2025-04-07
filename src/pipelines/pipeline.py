import builtins


class Pipline:

    def __init__(self, *args) -> None:
        self._args = list(args)

    def run(self, data):
        for step in self._args:
            data = step(data)
        return data


def print(data):
    builtins.print("\nPipline Step\n")
    builtins.print(data)
    return data
