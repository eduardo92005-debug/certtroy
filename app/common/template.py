def common_components(function):
    from .components import title                                                        
    def use_render():
        title.__render__()
        function()
    return use_render