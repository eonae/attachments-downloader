from time import sleep

def retry(delay, tries):
    def decorator (func):
        def wrapper(*args, **kwargs):
            x = 0
            while True:
                x += 1
                try:
                    return func(*args, **kwargs)
                except Exception as ex:
                    if x >= tries: raise(ex)
                    sleep(delay)
        return wrapper
    return decorator
