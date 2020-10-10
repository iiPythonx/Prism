# Modules
from .logging import Logging

# Initialization
log = Logging()

# Master function
def fetch_value(findKey = None):
    
    data = {}

    try:

        file = open("config.psm", "r").read().split("\n")

        data = {}

        lineNo = 1

        for line in file:

            if line[0] == "[" and line[-1] == "]":

                pass

            else:

                if not "=" in line:

                    log.warn(f"[config.psm (line {lineNo})]: invalid syntax pair")

                elif line.count("=") > 1:

                    log.warn(f"[config.psm (line {lineNo})]: invalid syntax pair")

                parsed = line.split("=")

                key = parsed[0]
                value = parsed[1]

                # check for booleans
                if value == "true":

                    value = True

                elif value == "false":

                    value = False

                # check for integers
                try:

                    value = int(value)

                except:

                    pass

                # pass on data
                data[key] = value

            lineNo += 1

    except:

        pass
    
    if not findKey:

        return findKey

    elif not findKey in data:

        log.error(f"[config.psm]: no value is named '{findKey}'")

        return None

    return data[findKey]
