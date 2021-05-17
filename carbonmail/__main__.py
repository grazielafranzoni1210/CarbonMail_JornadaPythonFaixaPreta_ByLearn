# Arquivo principal (inicial) a ser executado.
# Quando iniciamos o projeto (carbonmail), ele é o primeiro que o Python vai executar.
# Nós usamos também para ser o ponto de entrada da aplicação

from carbonmail.email_sender.manager import initialize as init_sender
from carbonmail.database.initialize import initialize as init_db

init_db()
init_sender()