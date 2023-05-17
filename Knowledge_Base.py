from  pyswip import Prolog

# classe per la manipolazione della Knowledge Base
class Knowledge_Base:

    def __init__(self, files_prolog) -> None:
        # creazione della base di conoscenza
        self.prolog = Prolog()

        # avvaloramento della base di conoscenza con le regole dei files
        for file in files_prolog:
            self.prolog.consult(file)

        # controllo che non sia una Knowledge Base insoddisfacibile (produce false)
        print(f"La KB caricata è consistente? ", not self.get_boolean_query_result("falso"))


    def get_boolean_query_result(self, my_query : str) -> bool:
        '''
        Metodo per restituire il risultato di una query booleana alla Knowòedge Base.
        '''
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