def enforce(*types):
    def decorator(f):
        def new_func(*args, **kwargs):
            # convert args into someting mutable
            newargs = []
            for (a, t) in zip(args, types):
                newargs.append(t(a))  # feel free to have more elaboration
            return f(*newargs, **kwargs)

        return new_func

    return decorator


@enforce(str, int)
def repeat_msg(msg, times):
    for time in range(times):
        print(msg)


repeat_msg("Hello", '8')
