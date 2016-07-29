# Example 5_15/5_19 from FluentPython
# Try calling clip.clip.__annotations__ (on the function object)

def clip(text:str, max_len:'int > 0'=80) -> str:
    '''
    Return text clipped at last space before max_len, 
    or at first space after max_len.
    '''
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ', max_len)
            if space_after >= 0:
                end = space_after
    if end is None:
        end = len(text)
    return text[:end].rstrip()
