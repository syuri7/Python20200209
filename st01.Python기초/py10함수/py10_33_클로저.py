def outer_func(tag):
    text = "Some text"
    tag = tag
    
    def inner_func():
        str = "<%s> %s </%s>" %(tag, text, tag)
        return str
    
    return inner_func

h1_func = outer_func("h1")
p_func = outer_func("p")


print(h1_func())
print(p_func())