from flet import *

class Mazine(UserControl):
    def __init__(self,zp):
        super().__init__()
        self.zp=zp
    def build(self):
        def vld(zb,e):
            if not self.user.value:
                self.snk.open=True
                zb.show_snack_bar(self.snk)
            else:
                self.snk.open=False
                
        

        self.user=TextField(label="userName",prefix_icon=icons.PERSON,width=250,height=45,
                              text_style=TextStyle(color=colors.BLACK26),
                              label_style=TextStyle(color=colors.BLACK26),
                              hint_style=TextStyle(color=colors.BLACK26,size=10),
                              hint_text="enter userName")

        self.btn=ElevatedButton("Sing in",width=200,height=45,bgcolor=colors.GREY_300,on_click=lambda e:vld(self.zp,e))
                                        #    on_click=lambda e: vld(zp,e)
        self.snk=SnackBar(Text("error:Invalid user name"),bgcolor=colors.RED)
        # self.snk.open=True
        c=Column(
            controls=[
                self.user,
                self.btn,
                self.snk
            ]
        )
        return c






def App(page:Page):

        
    page.title="Form"
    page.window_height=630
    page.window_width=380
    page.bgcolor=colors.GREY_300
    page.window_center()
    page.add(Mazine(page))

    page.update()
    

if "__main__"==__name__:
    app(App)