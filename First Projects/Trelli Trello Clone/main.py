import flet
from appbar import TrelloApp
from flet import (Page, colors)


if __name__ == "__main__":
    
    def main(page: Page):
        
        page.title = "Flet Trello Clone"
        page.padding = 0
        page.bgcolor = colors.BLUE_GREY_200
        app = TrelloApp(page)
        page.add(app)
        page.update()
    
    flet.app(target=main, view=flet.WEB_BROWSER)