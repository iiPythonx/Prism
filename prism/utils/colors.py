# Modules
import colorama

# Color initialization
colorama.init()
colors = {
    "red": "\033[91m",
    "green": "\033[92m",
    "cyan": "\033[36m",
    "blue": "\033[94m",
    "yellow": "\033[93m",
    "reset": "\033[0m"
}

# Colored function
def colored(text, color):
    return colors[color] + str(text) + colors["reset"]
