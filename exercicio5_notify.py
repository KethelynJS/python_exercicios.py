from plyer import notification
from datetime import datetime

def alerta(nivel, base, etapa):
    
    if nivel == 1:
        titulo = "Alerta Baixo"
    elif nivel == 2:
        titulo = "Alerta Médio"
    elif nivel == 3:
        titulo = "Alerta Alto"
    
    mensagem = f"Falha no carregamento da base {base} na etapa {etapa}\nData: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

    notification.notify(
        title = titulo,
        message = mensagem,
    )

alerta(base="Base", etapa="Etapa", nivel=2)