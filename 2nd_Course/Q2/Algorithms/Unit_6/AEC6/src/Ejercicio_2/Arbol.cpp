#include <iostream>
#include <vector>
#include <queue>

using namespace std;

// Constantes para colores
const int SIN_COLOR = 0;
const int ROJO = 1;
const int BLANCO = 2;

/**
 * bool esRojiblanco(const vector<vector<int>>& grafo)
 * Determina si el grafo dado puede ser pintado de rojiblanco (bipartito).
 * Utiliza BFS para recorrer el grafo asignando colores alternos.
 *
 * Precondiciones:
 * - El grafo debe estar representado correctamente como lista de adyacencias.
 * - No debe haber aristas a sí mismo ni aristas repetidas (el enunciado garantiza esto).
 *
 * Complejidad:
 * - Tiempo: O(V + A), donde V es el número de vértices y A el número de aristas.
 * - Espacio: O(V), para almacenar los colores y la cola del BFS.
 */
bool esRojiblanco(const vector<vector<int>>& grafo) {
    int V = grafo.size();
    vector<int> color(V, SIN_COLOR); // 0 = no coloreado aún

    for (int i = 0; i < V; ++i) {
        if (color[i] == SIN_COLOR) {
            queue<int> q;
            q.push(i);
            color[i] = ROJO;

            while (!q.empty()) {
                int u = q.front();
                q.pop();

                for (int v : grafo[u]) {
                    if (color[v] == SIN_COLOR) {
                        color[v] = (color[u] == ROJO) ? BLANCO : ROJO;
                        q.push(v);
                    } else if (color[v] == color[u]) {
                        return false; // Dos vecinos con el mismo color → No es bipartito
                    }
                }
            }
        }
    }
    return true;
}

/**
 * void procesarCasos()
 * Lee múltiples casos de prueba desde la entrada estándar,
 * procesa cada grafo y determina si puede pintarse de rojiblanco.
 *
 * Precondiciones:
 * - La entrada debe respetar el formato especificado en el enunciado.
 * - Protege errores de lectura usando cin.fail().
 *
 * Complejidad:
 * - Tiempo: O(T * (V + A)), donde T es el número de casos de prueba.
 * - Espacio: O(V), para cada caso por la lista de adyacencias.
 */
void procesarCasos() {
    int V;
    while (cin >> V) {
        if (V == 0)
            break;

        if (V < 0 || V > 100) {
            cerr << "Error: número de vértices fuera de rango (1-100)." << endl;
            exit(EXIT_FAILURE);
        }

        int A;
        if (!(cin >> A)) {
            cerr << "Error: lectura inválida del número de aristas." << endl;
            exit(EXIT_FAILURE);
        }

        vector<vector<int>> grafo(V);

        for (int i = 0; i < A; ++i) {
            int u, v;
            if (!(cin >> u >> v)) {
                cerr << "Error: lectura inválida de arista." << endl;
                exit(EXIT_FAILURE);
            }
            if (u < 0 || u >= V || v < 0 || v >= V) {
                cerr << "Error: vértices fuera de rango." << endl;
                exit(EXIT_FAILURE);
            }
            grafo[u].push_back(v);
            grafo[v].push_back(u);
        }

        if (esRojiblanco(grafo)) {
            cout << "SI" << endl;
        } else {
            cout << "NO" << endl;
        }
    }

    if (cin.fail() && !cin.eof()) {
        cerr << "Error: fallo en la lectura de datos." << endl;
        exit(EXIT_FAILURE);
    }
}

/**
 * int main(int argc, char* argv[])
 * Función principal protegida contra número incorrecto de argumentos.
 * No espera argumentos pero verifica argc.
 *
 * Precondiciones:
 * - argc debe ser igual a 1 (no se aceptan argumentos).
 */
int main(int argc, char* argv[]) {

    (void)argv;
    if (argc != 1) {
        cerr << "Error: este programa no recibe argumentos." << endl;
        return EXIT_FAILURE;
    }

    procesarCasos();

    return EXIT_SUCCESS;
}
