def initialize():
    
    from carbonmail.email_sender import Email_Sender # porque esse import dentro da função?
    # porque se colocar fora ele vai importar o email sender todo, e queremos importar só quando iniciar
    # pode criar até um loop de dependência se estiver fora da função
    
    ems = Email_Sender()
    ems.enable_window()