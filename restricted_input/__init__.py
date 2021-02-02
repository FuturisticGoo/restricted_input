# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 21:32:05 2021

@author: FuturisticGoo

Contains two functions r_input() and get_input_types().
"""

import platform
import sys


def r_input(prompt="", input_type="normal", exlude="",
            maxlength=-1, warning=""):
    """


    Parameters
    ----------
    prompt : str, optional
        DESCRIPTION. Prompt for input. The default is "".
    input_type : string, optional
        DESCRIPTION. Type of input. print(get_input_types()) for printing all \
input types. The default is "normal".
    exlude : str/list, optional
        DESCRIPTION. The string or list of strings containing the characters \
which is to be allowed in input. The default is "".
    maxlength : int, optional
        DESCRIPTION. Maximum length of input. The default is -1 meaning \
infinite.
    warning : str, optional
        DESCRIPTION. Warning to be shown if the user enters anything not \
allowed. The default is "".

    Raises
    ------
    KeyboardInterrupt
        If CTRL+C is pressed while typing.

    Returns
    -------
    str
        The final entered string.

    """

    special_char = ["`", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(",
                    ")", "-", "_", "=", "+", "[", "{", "]", "}", ";", ":",
                    "'", '"', ",", "<", ".", ">", "/", "?", "\\", "|"]

    if(platform.system() == "Windows"):
        import msvcrt
        is_windows = True
    else:
        # Little bit different for Linux or macOS
        def posix_getch():
            import termios
            import tty
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                ch = sys.stdin.read(1)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            return ch
        is_windows = False

    print(prompt, end="", flush=True)
    ask = ""
    while True:

        if(is_windows):
            temp = msvcrt.getch().decode("UTF-8")
        else:
            temp = posix_getch()

        if(temp == "\r"):
            break
        elif(temp == "\x03"):
            raise KeyboardInterrupt
        elif(temp in ["\b", "\x7f"]):
            if(len(ask) != 0):
                print("\b \b", end="", flush=True)
                ask = ask[:-1]
        else:
            if(maxlength == -1 or len(ask) < maxlength):
                if(input_type == "normal"):
                    ask += temp
                    print(temp, end="", flush=True)

                elif(input_type == "string_all"):
                    if(temp.isalpha() or temp in exlude):
                        ask += temp
                        print(temp, end="", flush=True)
                    elif(warning):
                        print("\r"+(" "*len(prompt+ask+warning))+"\r",
                              end="", flush=True)
                        print(warning+ask, end="", flush=True)
                    else:
                        pass

                elif(input_type == "string_upper"):
                    if((temp.isalpha() and temp.isupper()) or temp in exlude):
                        ask += temp
                        print(temp, end="", flush=True)
                    elif(warning):
                        print("\r"+(" "*len(prompt+ask+warning))+"\r",
                              end="", flush=True)
                        print(warning+ask, end="", flush=True)
                    else:
                        pass

                elif(input_type == "string_lower"):
                    if((temp.isalpha() and temp.islower()) or temp in exlude):
                        ask += temp
                        print(temp, end="", flush=True)
                    elif(warning):
                        print("\r"+(" "*len(prompt+ask+warning))+"\r",
                              end="", flush=True)
                        print(warning+ask, end="", flush=True)
                    else:
                        pass

                elif(input_type == "specials"):
                    if(temp in special_char or temp in exlude):
                        ask += temp
                        print(temp, end="", flush=True)
                    elif(warning):
                        print("\r"+(" "*len(prompt+ask+warning))+"\r",
                              end="", flush=True)
                        print(warning+ask, end="", flush=True)
                    else:
                        pass

                elif(input_type == "integer"):
                    if(temp.isdigit() or temp in exlude):
                        ask += temp
                        print(temp, end="", flush=True)
                    elif(warning):
                        print("\r"+(" "*len(prompt+ask+warning))+"\r",
                              end="", flush=True)
                        print(warning+ask, end="", flush=True)
                    else:
                        pass

                elif(input_type == "float"):
                    if((temp.isdigit() or temp == ".") or temp in exlude):
                        if(ask.find(".") == -1):
                            ask += temp
                            print(temp, end="", flush=True)
                        elif(temp != "."):
                            ask += temp
                            print(temp, end="", flush=True)
                    elif(warning):
                        print("\r"+(" "*len(prompt+ask+warning))+"\r",
                              end="", flush=True)
                        print(warning+ask, end="", flush=True)
                    else:
                        pass
                elif(input_type == "version"):
                    if((temp.isdigit() or temp == ".") or temp in exlude):
                        ask += temp
                        print(temp, end="", flush=True)
                    elif(warning):
                        print("\r"+(" "*len(prompt+ask+warning))+"\r",
                              end="", flush=True)
                        print(warning+ask, end="", flush=True)
                    else:
                        pass
                elif(input_type == "nothing"):
                    if(temp in exlude):
                        ask += temp
                        print(temp, end="", flush=True)
                    elif(warning):
                        print("\r"+(" "*len(prompt+ask+warning))+"\r",
                              end="", flush=True)
                        print(warning+ask, end="", flush=True)
                    else:
                        pass
    print(flush=True)
    return ask


def get_input_types():
    """


    Returns
    -------
    list
        List containing all the input_types.

    """
    return ["normal", "string_all", "string_upper", "string_lower",
            "specials", "integer", "float", "version", "nothing"]


if __name__ == "__main__":
    for i in get_input_types():
        print(r_input(f"Enter {i}: ", i,
                      warning=f"Only {i} allowed. Enter {i}: "))
