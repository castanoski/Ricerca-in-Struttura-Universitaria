# definizione di costanti utili per la stampa
PROMPT_BEGIN = "\n$ "
PROMPT_END = ":\n\n  > "


def prompt_request(message : str):
    '''
    Metodo per la richiesta di input all'utente.
    Restituisce l'input dell'utente.
    '''
    result = ""
    while(result == ""):
        result = input(f"{PROMPT_BEGIN}{message}{PROMPT_END}").lower()
    return result


def prompt(message : str):
    '''
    Metodo per la stampa.
    '''
    print(f"{PROMPT_BEGIN}{message}")