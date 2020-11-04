from time import sleep

def retry(delay, tries):
    def decorator (func):
        def wrapper(*args, **kwargs):
            for _ in range(tries):
                try:
                    return func(*args, **kwargs)
                except Exception as ex:
                    sleep(delay)
            raise(ex)
        return wrapper
    return decorator
