from st_pages import Page, show_pages

show_pages(
    [
        Page("app/pages/index/index.py", "Home", "🏠"),
        Page("app/pages/session_1/session_1.py", "Seção_1", ":books:"),
        Page("app/pages/session_2/session_2.py", "Seção_2", ":books:"),
        Page("app/pages/operations/operations.py", "Operações", ":books:"),
    ]
)