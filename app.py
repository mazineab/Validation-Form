from flet import *
from SingIn import SingIn
from Login import Login

def App(page:Page):
    page.title="Form"
    page.window_height=630
    page.window_width=380
    page.window_center()
    def router(e):
        page.views.clear()
        page.views.append(
        View(
            "/Login",[
                Login(page)
                ]
            )
        )
        if page.route=="/SingIn":
            page.views.append(
                View(
                    "/SingIn",[
                        SingIn(page)
                        ]
                    )  
                )
        page.update()
    def PopView():
        page.views.pop()
        topView=page.views[-1]
        page.go(topView.route)
    

    page.on_route_change=router
    page.on_view_pop=PopView


    
    page.go(page.route)
    page.update()


if "__main__"==__name__:
    app(App)
