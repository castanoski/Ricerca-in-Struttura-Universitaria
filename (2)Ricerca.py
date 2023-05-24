# imports
from libsRicerca.searchGeneric import Searcher, AStarSearcher
from libsRicerca.searchProblem import Arc, Search_problem, Search_problem_from_explicit_graph
from Knowledge_Base import Knowledge_Base
import math
import time
from libsRicerca.searchMPP import SearcherMPP
from utili import prompt_request, prompt


# definizione delle variabili utente
PATH_FACTS_KB = './KB/fatti.pl'
PATH_RULES_KB = './KB/regole.pl'
FILES_LIST = [PATH_FACTS_KB, PATH_RULES_KB]

# AGGIUNGI INPUT TIME PER COMPLETARE
TIME_DEFAULT = "get_time(friday,11,30)"


# classe per la rappresentazione di un nodo del grafo, rappresentato dal suo nome, le coordinate spaziali e una lista dei nomi dei nodi adiacenti
class My_Node:

    def __init__(self, node_name : str, kb : Knowledge_Base) -> None:
        # query per trovare le coordinate X,Y del nodo
        query_result = kb.get_unique_query_result(f"position({node_name}, X, Y)")
        
        # inizializzazione del nome, delle coordinate, del piano
        self.node_name = node_name
        self.coord_x = query_result["X"]
        self.coord_y = query_result["Y"]
        self.floor = kb.get_unique_query_result(f"floor({node_name}, Floor)")["Floor"]

        # inizializzazione dei vicini
        self.neighbors_names = []

        for neighbor in kb.get_list_query_result(f"direct_arc({node_name}, Neighbor)"):
            self.neighbors_names.append(neighbor["Neighbor"])
        
    def get_name(self) -> str:
        return self.node_name
    
    def get_neighbors_names(self) -> list:
        return self.neighbors_names

def calculate_heuristic(start,kb:Knowledge_Base, nodes:list,user_name, rounding=2) -> float:
    heuristic = math.inf
    for goal in nodes:
        heuristic = min(heuristic,calculate_single_heuristic(start,kb,goal,user_name))
    return round(heuristic, rounding)
    

def calculate_single_heuristic(start,kb:Knowledge_Base,goal,user_name) -> float:
    
    if(kb.get_boolean_query_result(f"is_same_floor({start},{goal})")):
        heuristic = kb.get_unique_query_result(f"distance({start},{goal},Distance)")["Distance"]
    elif(kb.get_boolean_query_result(f"is_lower_floor({start},{goal})")):
        heuristic = math.inf
        for Method in kb.get_list_query_result(f"can_go_up_with_from({user_name},Method,{start})"):
            new_heuristic = kb.get_unique_query_result(f'distance({start},{Method["Method"]},D)')["D"] + calculate_single_heuristic(kb.get_unique_query_result(f'get_destination_up({Method["Method"]},D)')["D"],kb,goal,user_name)
            heuristic = min(heuristic,new_heuristic)
    else:
        heuristic = math.inf
        for Method in kb.get_list_query_result(f"can_go_down_with_from({user_name},Method,{start})"):
            new_heuristic = kb.get_unique_query_result(f'distance({start},{Method["Method"]},D)')["D"] + calculate_single_heuristic(kb.get_unique_query_result(f'get_destination_down({Method["Method"]},D)')["D"],kb,goal,user_name)
            heuristic = min(heuristic,new_heuristic)
    return heuristic
            
    

# classe per la costruzione del problema di ricerca da risolvere
class My_Problem(Search_problem_from_explicit_graph):

    def __init__(self, kb : Knowledge_Base, start_node_name : str, goal_nodes_names : list, user_name : str):
        
        nodes = set()
        nodes_names = set()
        arcs = []
        goal_nodes = set()
        heuristics = {}
        
        # per ogni stanza creo il nodo sfruttando le info della Knowledge Base
        for node_name in kb.get_list_query_result("is_place(X)"):
            node = My_Node(node_name["X"], kb)
            
            # aggiungo il nodo all'insieme dei nodi
            nodes.add(node)
            nodes_names.add(node_name["X"])

            # se il nome del nodo coincide con uno dei nodi goal, lo memorizzo per poi passarlo al costruttore di default
            if(node.get_name() in goal_nodes_names): #controlla se togliere(?)
                goal_nodes.add(node)
    
        # per ogni nodo calcolo il valore euristico e, per ogni adiacente, effettuo la query sul valore dell'arco che li collega e aggiungo l'arco alla lista (Euclidean Distance)
        for n in nodes:
            heuristics[n.get_name()] = calculate_heuristic(n.get_name(),kb,goal_nodes_names,user_name)
            for neigh in n.get_neighbors_names():
                if (kb.get_boolean_query_result(f"has_access({user_name},{n.get_name()},{TIME_DEFAULT}),has_access({user_name},{neigh},{TIME_DEFAULT})")):
                    cost = kb.get_unique_query_result(f"distance({n.get_name()},{neigh}, Cost)")["Cost"]
                    arcs.append(Arc(n.get_name(), neigh, cost))

        # richiamo al costruttore di default per costruire il problema
        super().__init__(nodes=nodes_names, arcs=arcs, start=start_node_name, goals=goal_nodes_names, hmap=heuristics)


class My_Solver:
    
    def __init__(self, kb : Knowledge_Base) -> None:
        
        # salva la kb
        self.kb = kb

        # inizia il ciclo
        self.main()


    def solve_problem(self):

        # creo il problema di ricerca
        my_problem = My_Problem(self.kb, self.start, self.end, self.person)

        # eseguo la ricerca con A*
        prompt("Creazione del problema utilizzando A*:")
        start_time = time.time()
        AStar_Searcher = AStarSearcher(my_problem)
        prompt(f"Creazione avvenuta in {time.time()-start_time} secondi.")
        start_time = time.time()
        AStar_solution = AStar_Searcher.search()
        prompt(f"{AStar_solution}")
        prompt(f"Costo = {AStar_solution.cost}")
        prompt(f"Eseguito in {time.time()-start_time} secondi.")

        # eseguo la ricerca con A e MPP*
        prompt("Creazione del problema utilizzando A* con MPP:")
        start_time = time.time()
        mpp_Searcher = SearcherMPP(my_problem)
        prompt(f"Creazione avvenuta in {time.time()-start_time} secondi.")
        start_time = time.time()
        mpp_solution = mpp_Searcher.search()
        prompt(f"{mpp_solution}")
        prompt(f"Costo = {mpp_solution.cost}")
        prompt(f"Eseguito in {time.time()-start_time} secondi.")


    def end_request(self) -> bool:
        query = prompt_request(f"Immetti il codice del luogo dove vuoi arrivare, oppure /bagno per il bagno più vicino, oppure /aulastudio per l'aula studio più vicina, infine /back se vuoi cambiare stanza di parttenza")
        
        # se l'utente vuole cambiare stanza allora ritorna al ciclo iniziale con una nuova identificazione
        if(query == "/back"): 
            prompt(f"Cambiando luogo di partenza...")
            return False
        
        if(not self.kb.get_boolean_query_result(f"is_place({query})")):
            prompt(f"Il codice luogo inserito non è corretto.")
            return True
        else:
            # salviamo i goal a seconda della query
            if(query == "/bagno"): 
                pass                    # query bath_room più vicino 
            elif(query ==  "/aulastudio"):
                pass                    # query study_room più vicina
            else:
                self.end = [query]
            
        # risolviamo il problema
        self.solve_problem()

        # return false per effettuare una nuova query a partire dalla stanza di partenza
        return False


    def start_request(self) -> bool:
        '''
        Metodo per l'esecuzione di una query con una persona specifica.
        Restituisce True se l'utente non ha immesso "/logout", Falso se l'utente vuole fare logout.
        '''
        # richiesta stanza di partenza
        start_place = prompt_request(f"Ciao {self.person}, immetti il codice della posizione da cui vuoi partire, /logout per scegliere un altro nome utente")
        
        # se l'utente vuole cambiare nome allora ritorna al ciclo iniziale con una nuova identificazione
        if(start_place == "/logout"): 
            prompt(f"Logout in corso...")
            return False
        
        # se l'utente inserisce un codice stanza che non è valido, allora inizierà un nuovo ciclo per acquisire la stanza
        if(not self.kb.get_boolean_query_result(f"is_place({start_place})")):
            prompt(f"Il codice stanza inserito non è corretto.")
            return True
        
        # l'utente ha inserito una stanza di partenza
        keep_going = True
        while(keep_going):
            self.start = start_place
            keep_going = self.end_request()

        # return iniziando un nuovo ciclo con la stessa persona
        return True

    def person_request(self) -> bool:
        '''
        Metodo per l'esecuzione di una query.
        Restituisce True se l'utente non ha immesso "/quit", Falso se l'utente vuole uscire.
        '''
        
        # richiesta codice utente
        person = prompt_request("Identificati digitando il tuo nome utente per effettuare una query oppure scrivi '/quit' per uscire dallo script")

        # se l'utente vuole uscire allora termina il programma
        if(person == "/quit"): 
            prompt(f"Chiusura del programma.")
            return False
        
        # se l'utente inserisce un codice utente che non è valido, allora inizierà un nuovo ciclo di identificazione
        if(not self.kb.get_boolean_query_result(f"is_person({person})")):
            prompt(f"Il codice utente inserito non è corretto.")
            return True

        # l'utente è riuscito ad identificarsi come persona appartenente alla Knowledge Base
        keep_going = True
        while(keep_going):
            self.person = person
            keep_going = self.start_request()

        # return iniziando un nuovo ciclo di identificazione
        return True
        
    def main(self):
        # ciclo prompt
        keep_going = True
        while(keep_going):
            keep_going = self.person_request()

#       --------------------------------------------------------------------------------------------------------------------       #
#                                                   Inizio dello Script                                                            #
#       --------------------------------------------------------------------------------------------------------------------       # 

# creazione della Knowledge Base
knowledge_base = Knowledge_Base(FILES_LIST)

# main loop per l'esecuzione delle query utente
My_Solver(knowledge_base)



#COLLO DI BOTTIGLIA
# faccio una prova
print("Che corso, seguito da quale prof, consente allo student_1 di entrare in office_1_21_5?",knowledge_base.get_list_query_result(f"follows_class(student_1,Class),teaches_class(Teacher,Class),office_owner(Teacher, office_1_21_5)"))
print("teacher_1 quale metodo può usare per salire se si trova in stairs_3_33_11?",knowledge_base.get_list_query_result("can_go_up_with_from(teacher_1, Method, stairs_3_33_11)"))

print(" Risolviamo il problema tra hallway_ingresso e hallway_2_11_5:\n")
p = My_Problem(knowledge_base, "hallway_ingresso", ["hallway_2_11_5"], "student_1")

# MPP
print("     A* con MPP:\n")
searcher = SearcherMPP(p)
start_time = time.time()
solution = searcher.search()
print(f"\n$ {solution}\n$ {solution.cost}\n$ in {time.time()-start_time}s.")

# AStar
print("     A* semplice:\n")
searcher = AStarSearcher(p)
start_time = time.time()
solution = searcher.search()
print(f"\n$ {solution}\n$ {solution.cost}\n$ in {time.time()-start_time}s.")

print(" Risolviamo il problema tra hallway_ingresso e hallway_2_11_11:")
p = My_Problem(knowledge_base, "hallway_ingresso", ["hallway_2_11_11"], "student_1")

# MPP
print("     A* con MPP:\n")
searcher = SearcherMPP(p)
start_time = time.time()
solution = searcher.search()
print(f"\n$ {solution}\n$ {solution.cost}\n$ in {time.time()-start_time}s.")

# AStar
print("     A* semplice:\n")
searcher = AStarSearcher(p)
start_time = time.time()
solution = searcher.search()
print(f"\n$ {solution}\n$ {solution.cost}\n$ in {time.time()-start_time}s.")
