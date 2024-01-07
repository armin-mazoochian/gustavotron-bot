stfu_mode = False


def set_stfu_mode():
    global stfu_mode
    stfu_mode = not stfu_mode


def get_stfu_mode():
    return stfu_mode


# Decorators
def stfu_enabled(func):
    async def wrapper(*args, **kwargs):
        if get_stfu_mode():
            return
        await func(*args, **kwargs)
    return wrapper
