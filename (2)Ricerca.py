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
    result = ""
    while(result == ""):
        result = input(f"{PROMPT_BEGIN}{message}{PROMPT_END}")
    return result


def executeSearchWithStartRoom(kb: Knowledge_Base, person : str, start_room : str) -> bool:
    print("Implementa esecuzione della query.")
    return False


def executeSearchWithPerson(kb : Knowledge_Base, person : str) -> bool:
    '''
    Metodo per l'esecuzione di una query con una persona specifica.
    Restituisce True se l'utente non ha immesso "/logout", Falso se l'utente vuole fare logout.
    '''
    # richiesta stanza di partenza
    start_room = prompt(f"Ciao {person}, immetti il codice della posizione da cui vuoi partire, /logout per scegliere un altro nome utente")
    
    # se l'utente vuole cambiare nome allora ritorna al ciclo iniziale con una nuova identificazione
    if(start_room == "/logout"): 
        print(f"{PROMPT_BEGIN}Logout in corso...")
        return False
    
    # se l'utente inserisce un codice stanza che non è valido, allora inizierà un nuovo ciclo per acquisire la stanza
    if(not kb.get_boolean_query_result(f"is_room({start_room})")):
        print(f"{PROMPT_BEGIN}Il codice stanza inserito non è corretto.")
        return True
    
    # l'utente ha inserito una stanza di partenza
    keep_going = True
    while(keep_going):
        keep_going = executeSearchWithStartRoom(kb, person, start_room)

    # return iniziando un nuovo ciclo con la stessa persona
    return True


def executeSearch(kb : Knowledge_Base) -> bool:
    '''
    Metodo per l'esecuzione di una query.
    Restituisce True se l'utente non ha immesso "/quit", Falso se l'utente vuole uscire.
    '''
    
    # richiesta codice utente
    person = prompt("Identificati digitando il tuo nome utente per effettuare una query oppure scrivi '/quit' per uscire dallo script")

    # se l'utente vuole uscire allora termina il programma
    if(person == "/quit"): 
        print(f"{PROMPT_BEGIN}Chiusura del programma.")
        return False
    
    # se l'utente inserisce un codice utente che non è valido, allora inizierà un nuovo ciclo di identificazione
    if(not kb.get_boolean_query_result(f"is_person({person})")):
        print(f"{PROMPT_BEGIN}Il codice utente inserito non è corretto.")
        return True

    # l'utente è riuscito ad identificarsi come persona appartenente alla Knowledge Base
    keep_going = True
    while(keep_going):
        keep_going = executeSearchWithPerson(kb, person)

    # return iniziando un nuovo ciclo di identificazione
    return True
        

#       --------------------------------------------------------------------------------------------------------------------       #
#                                                   Inizio dello Script                                                            #
#       --------------------------------------------------------------------------------------------------------------------       # 


# main loop per l'esecuzione delle query utente
knowledge_base = Knowledge_Base(FILES_LIST)

keep_going = True
while(keep_going):
    keep_going = executeSearch(knowledge_base)




