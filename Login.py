from flet import *
from reg import Valid

class Login(UserControl):
    def __ini__(self,page):
        self.page=page
        super().__init__()
    def build(self):
        
        self.snk=SnackBar(Text("",color=colors.WHITE),bgcolor=colors.RED)
        self.snkV=SnackBar(Text("valid All",color=colors.WHITE70),bgcolor=colors.GREEN)

        
        def valid(e):
            Res=Valid(self.user.value,"",self.password.value)
            if not Res.validUser():
                self.snk.content=Text("Invalid UserName",color=colors.WHITE)
                self.snk.open=True
                self.page.show_snack_bar(self.snk)
            elif not Res.validPassword():
                self.snk.open=True
                self.snk.content=Text("Invalid Password",color=colors.WHITE)
                self.page.show_snack_bar(self.snk)
            else:
                self.snkV.open=True
                self.page.show_snack_bar(self.snkV)
        
        self.user=TextField(label="UserName",prefix_icon=icons.PERSON,width=250,height=45,
                              text_style=TextStyle(color=colors.WHITE),border_color=colors.WHITE,
                              label_style=TextStyle(color=colors.WHITE),
                              hint_style=TextStyle(color=colors.WHITE,size=10),
                              hint_text="Enter UserName")
        self.password=TextField(label="Password",prefix_icon=icons.PASSWORD,width=250,height=45,password=True,
                              text_style=TextStyle(color=colors.WHITE),label_style=TextStyle(color=colors.WHITE),
                              border_color=colors.WHITE,
                              hint_text="Enter Password",hint_style=TextStyle(color=colors.WHITE,size=10),can_reveal_password=True)
        login=Column(
            controls=[
                    Container(Text("Please Log In",size=45,color=colors.WHITE),alignment=alignment.center),
                    Container(self.user,alignment=alignment.center,margin=margin.only(top=100)),
                    Container(self.password,alignment=alignment.center,margin=margin.only(top=50)),
                    Container(
                        Row(
                        controls=[
                            Container(
                            ElevatedButton("Log In",width=200,height=45,on_click=valid
                                           )
                            ),
                        Container(
                            TextButton("Create Account",on_click=lambda _:self.page.go("/SingIn"))
                            ),
                        ]
                        
                    ),margin=margin.only(top=50)
                    )
                    

        ])
        return login
