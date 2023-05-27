from  pyswip import Prolog
from util.utili import prompt_request, prompt

# classe per la manipolazione della Knowledge Base
class Knowledge_Base:


    def __init__(self, files_prolog) -> None:

        # creazione della base di conoscenza
        self.prolog = Prolog()

        # definizione del dizionario per ask_abnormal_facts
        self.PREDICATE_DICT = {
            "PROBLEM" : "there_is_a_problem_in", 
            "WET_FLOOR" : "has_wet_floor"
        }

        # list per capire se dover definire WET_FLOOR oppure THERE_IS_A_PROBLEM_IN
        self.problem_check = {}
        for problem_key in self.PREDICATE_DICT.keys():
            self.problem_check[problem_key] = False

        # avvaloramento della base di conoscenza con le regole dei files
        for file in files_prolog:
            self.prolog.consult(file)

        # immissione delle osservazioni per luoghi irraggiungibili
        self.ask_abnormal_facts()

        # controllo che non sia una Knowledge Base insoddisfacibile (produce false)
        print(f"La KB caricata è consistente? ", self.is_satisfiable())


    def add_clause(self, clause : str):
        self.prolog.assertz(clause)


    def get_boolean_query_result(self, my_query : str) -> bool:
        '''
        Metodo per restituire il risultato di una query booleana alla Knowledge Base.
        Restituisce false se vi è un errore di sintassi dovuto agli argomenti della query.
        '''

        # se richiedo un predicato
        if "(" in my_query:
            # controllo se all'interno delle parentesi non ci siano variabil che inizino con caratteri non alfabetici
            terms = my_query.split("(")[1].split(",")
            for term in terms:
                if(not term[0].isalpha()):
                    return False

        # trasformo in minuscole perchè è una query booleana
        return bool(list(self.prolog.query(my_query)))
       


    def get_list_query_result(self, my_query : str) -> list:
        '''
        Metodo per restituire il risultato di una query che può avere più soluzioni alla Knowledge Base.
        Restituisce una lista di dizionari, dove in ogni dizionario, ad ogni variabile della query è associato un valore.
        '''
        return list(self.prolog.query(my_query))
    

    def get_unique_query_result(self, my_query : str) -> dict:
        '''
        Il metodo restituisce l'unica sostituzione possibile della query. 
        Se non ce n'è alcuna oppure se ce n'è più di una, allora resituisce dizionario vuoto e stampa un messaggio di errore.
        '''
        result = self.get_list_query_result(my_query)
        if(len(result) == 1):
            return result[0]
        elif(len(result) > 1):
            print(f"Query risulta avere più soluzioni:\n{my_query}\n")
        else:
            print(f"Query risulta non avere soluzione:\n{my_query}\n")
        
        return {}
    

    def add_clause_for_place(self, place : str, problem="PROBLEM"):

        upper_problem = problem.upper()
        if(upper_problem not in self.PREDICATE_DICT):
            prompt(f"{problem} non è un parametro accettabile.")
        elif(self.get_boolean_query_result(f"is_place({place})")):
            self.add_clause(f"{self.PREDICATE_DICT[upper_problem]}({place})")
            self.problem_check[upper_problem] = True
            prompt("Aggiunta con successo.")
        else:
            prompt(f"L'argomento '{place}' non è un luogo, pertanto non è possibile aggiungerle una clausola riguardante un luogo.")

    
    def ask_abnormal_facts(self):
        prompt("IMMISSIONE DELLE SITUAZIONI ANORMALI NELL'EDIFICIO:")

        while(True):
            command = prompt_request("Inserisci il nome di un posto e il relativo problema, nel formato < nome_posto problema > oppure /end per terminare l'operazione")
            
            # splitta il comando in più parti
            commands = command.split(" ")

            if(len(commands) == 1 and commands[0] == "/end"):
                for problem_key in self.PREDICATE_DICT:
                    if not self.problem_check[problem_key]:
                        self.add_clause(f"{self.PREDICATE_DICT[problem_key]}(no_place)")
                return

            if(len(commands) == 2):
                
                # aggiunta clausola
                if(self.get_boolean_query_result(f"is_place({commands[0]})")): 
                    self.add_clause_for_place(commands[0], commands[1])
                else:
                    prompt("Il codice immesso non corrisponde ad alcun luogo valido!")
                    
            else:
                prompt("Formato del comando errato! Prova con < nome_posto problema > separato da un singolo spazio.")


    def is_satisfiable(self) -> bool:
        return not self.get_boolean_query_result("false")

            
