from st_pages import Page, show_pages

show_pages(
    [
        Page("app/pages/index/index.py", "Home", "🏠"),
        Page("app/pages/session_1/session_1.py", "Section_1", ":books:"),
    ]
)