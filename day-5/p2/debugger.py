import time

def debug(log_type: str, log_text: str, data: str | list | int = "") -> None:
    match log_type:
        case "data":
            symbol = "\t[>]"
        case "log":
            symbol = "[+]"
        case _:
            symbol = "\t[>]"

    #print(symbol, log_text, data)
    #time.sleep(0.5)
