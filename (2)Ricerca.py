# imports
from libsRicerca.searchGeneric import AStarSearcher
from libsRicerca.searchProblem import Arc, Search_problem, Search_problem_from_explicit_graph
from pyswip import Prolog

# definizione delle variabili utente
PATH_FACTS_KB = './KB/fatti.pl'
PATH_RULES_KB = './KB/regole.pl'
FILES_LIST = [PATH_FACTS_KB, PATH_RULES_KB]

# definizione di costanti utili per la stampa
PROMPT_BEGIN = "\n"
PROMPT_END = ":\n\n  > "



# classe che traduce i risultati delle query alla KB in un problema di ricerca
class Problema_Ricerca_Edificio():
    pass

        
    
# classe per la manipolazione della Knowledge Base
class Knowledge_Base:

    def __init__(self, files_prolog) -> None:
        # creazione della base di conoscenza
        self.prolog = Prolog()

        # avvaloramento della base di conoscenza con le regole dei files
        for file in files_prolog:
            self.prolog.consult(file)

        # controllo che non sia una Knowledge Base insoddisfacibile (produce false)
        #print(f"La KB è inconsistente? ", self.get_boolean_query_result("falso"))


    def get_boolean_query_result(self, my_query : str) -> bool:
        '''
        Metodo per restituire il risultato di una query alla Knowòedge Base.
        '''
        return bool(list(self.prolog.query(my_query)))

    def get_list_query_result(self, my_query : str) -> list:
        '''
        Metodo per restituire il risultato di una query alla Knowòedge Base.
        '''
        return list(self.prolog.query(my_query))



def prompt(message : str):
    '''
    Metodo per la richiesta di input all'utente.
    Restituisce l'input dell'utente.
    '''
    return input(f"{PROMPT_BEGIN}{message}{PROMPT_END}")



def executeSearch(kb : Knowledge_Base):
    '''
    Metodo per l'esecuzione di una query.
    Restituisce True se l'utente non ha immesso "/quit", Falso se l'utente vuole uscire.
    '''
    
    person = prompt("Identificati per effettuare una query oppure scrivi '/quit' per uscire dallo script")

    if(person == "/quit"): 
        return False
    
    # do something 

    return True


#       --------------------------------------------------------------------------------------------------------------------       #
#                                                   Inizio dello Script                                                            #
#       --------------------------------------------------------------------------------------------------------------------       # 


# main loop per l'esecuzione delle query utente
knowledge_base = Knowledge_Base(FILES_LIST)

keep_going = True
while(keep_going):
    keep_going = executeSearch(knowledge_base)

print("bye.")


