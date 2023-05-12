# imports
from libsRicerca.searchGeneric import AStarSearcher
from libsRicerca.searchProblem import Arc, Search_problem, Search_problem_from_explicit_graph
from pyswip import Prolog

# definizione delle variabili utente
PATH_FACTS_KB = './KB/fatti.pl'
PATH_RULES_KB = './KB/regole.pl'

# definizione di costanti utili per la stampa
PROMPT_BEGIN = "\n"
PROMPT_END = ":\n\n  > "

# classe che traduce i risultati delle query alla KB in un problema di ricerca
class Problema_Ricerca_Edificio():
    
    # per comodità definiamo quelli che sono gli attributi della classe
    __slots__ = ("problem","prolog","searcher")

    def __init__(self, files_prolog) -> None:
        
        # creazione della base di conoscenza
        self.prolog = Prolog()

        # avvaloramento della base di conoscenza con le regole dei files
        for file in files_prolog:
            self.prolog.consult(file)

        # controllo che non sia una Knowledge Base insoddisfacibile (produce false)
        print(bool(list(self.prolog.query("falso"))))
    

def get_input(message : str):
    '''
    Metodo per la richiesta di input all'utente.
    Restituisce l'input dell'utente.
    '''
    return input(f"{PROMPT_BEGIN}{message}{PROMPT_END}")


def executeQuery():
    '''
    Metodo per l'esecuzione di una query.
    Restituisce True se l'utente non ha immesso "/quit", Falso se l'utente vuole uscire.
    '''
    
    person = get_input("Identificati per effettuare una query oppure scrivi '/quit' per uscire dallo script")

    if(person == "/quit"): 
        return False
    
    # do something 

    return True


#       --------------------------------------------------------------------------------------------------------------------       #
#                                                   Inizio dello Script                                                            #
#       --------------------------------------------------------------------------------------------------------------------       # 


# main loop per l'esecuzione delle query utente
keep_going = True
while(keep_going):
    keep_going = executeQuery()

print("bye.")


