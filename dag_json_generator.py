import json
import random

def generate_random_dag(num_nodes=6, max_dependencies=3):
    nodes = [f"Step {i}" for i in range(1, num_nodes + 1)]
    dag = []

    for node in nodes:
        possible_deps = [n for n in nodes if n != node]
        dependencies = random.sample(possible_deps, random.randint(0, max_dependencies))
        dependencies = [dep for dep in dependencies if nodes.index(dep) < nodes.index(node)]

        dag.append({
            "id": node,
            "dependencies": dependencies
        })

    with open("dag_graph.json", "w") as file:
        json.dump({"components": dag}, file, indent=4)
    
    print("Random DAG graph generated successfully in 'dag_graph.json'.")

if __name__ == "__main__":
    generate_random_dag()
