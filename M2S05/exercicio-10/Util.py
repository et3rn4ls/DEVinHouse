class DEVinException(Exception):

    def __init__(self, message):
        super().__init__(message)


class TimeException(Exception):

    def __init__(self, message):
        super().__init__(message)


def execution_time(f):

    def valida(hi, hf):
        if hi is None or hf is None:
            raise TimeException('Problema na coleta da hora inicial e/ou hora final.')
        if not isinstance(hi, float) or not isinstance(hf, float):
            raise TimeException('Hora inicial e hora final precisam ser valores float.')

        return f(hi, hf)

    return valida


@execution_time
def tempo(hi, hf):
    return hf - hi
