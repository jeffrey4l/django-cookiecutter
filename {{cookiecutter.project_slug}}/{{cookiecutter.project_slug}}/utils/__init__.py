__all__ = ['enum_for_django']

def human_size(size):
    '''
    size: bytes in size
    '''
    if size < 1024:
        return size


def enum_for_django(cls):
    cls.do_not_call_in_templates = True
    return cls