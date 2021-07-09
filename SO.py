import platform


def detectar_sistema() -> str:
    sistema_actual =platform.system()
    print(type(sistema_actual))
    a = "A"
    return a

detectar_sistema()