import pdb

def oxford_comma(items):
    str = ""
    if len(items) == 2:
        str = " and ".join(items)
    elif len(items) > 2:
        items[-1] = f"and {items[-1]}"
        str = ", ".join(items)
        # Welp... heres the code to remove the oxford comma
        # for index, item in enumerate(items):
        #     if index == 0:
        #         str += item
        #     elif index == len(items) - 1:
        #         str += f"{item}"
        #     # elif index == len(items) - 2:
        #     #     str += f" {item}"
        #     else:
        #         str += f", {item}"
    else:
        str = ", ".join(items)
    return str
