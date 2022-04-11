def load_theme(themename : str) -> str :
    
    with open(f"themes/{themename}.css", encoding='utf8') as style :
        return style.read()