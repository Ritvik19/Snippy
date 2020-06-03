def tag(name):
    
    def data(*content, **attrs):
        attr_str = ''.join(f' {attr}="{value}"' for attr, value in sorted(attrs.items())) if attrs else ''
        if content:
            return '\n'.join(f'&lt;{name}{attr_str}&gt;{c}&lt;/{name}&gt;' for c in content)
        else:
            return f'&lt;{name}{attr_str}/&gt;'
    
    return data
    
tag('h1')('Hey')