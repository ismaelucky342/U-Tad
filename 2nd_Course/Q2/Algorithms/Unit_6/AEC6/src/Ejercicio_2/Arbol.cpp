/***************************************************************************************/
/*                                                                                     */
/*                                         ██╗   ██╗   ████████╗ █████╗ ██████╗        */
/*      AEC6 - Algorithms                  ██║   ██║   ╚══██╔══╝██╔══██╗██╔══██╗       */
/*                                         ██║   ██║█████╗██║   ███████║██║  ██║       */
/*      created:        02/04/2025         ██║   ██║╚════╝██║   ██╔══██║██║  ██║       */
/*      last change:    17/04/2025         ╚██████╔╝      ██║   ██║  ██║██████╔╝       */
/*                                          ╚═════╝       ╚═╝   ╚═╝  ╚═╝╚═════╝        */
/*                                                                                     */
/*       Ismael Hernandez Clemente              ismael.hernandez@live.u-tad.com        */
/*                                                                                     */
/*       Github:  https://github.com/ismaelucky342/                                    */
/*                                                                                     */
/***************************************************************************************/

#include <iostream>
#include <vector>
#include <queue>
#include <stdexcept>
#include <string>

using namespace std;

/**
 * @brief Función para verificar si un grafo es bipartito (rojiblanco).
 *
 * Realiza un recorrido por el grafo utilizando BFS para intentar colorear los nodos
 * con dos colores de manera que no haya aristas entre nodos del mismo color.
 *
 * @param num_vertices Número de vértices en el grafo.
 * @param adj Lista de adyacencia representando el grafo.
 * @param color Vector para almacenar los colores asignados a los nodos.
 * @return true si el grafo es bipartito (rojiblanco), false en caso contrario.
 *
 * @throws std::invalid_argument Si el número de vértices es menor que 1.
 *
 * @complexity
 * Tiempo: O(V + A), donde V es el número de vértices y A es el número de aristas.
 * Espacio: O(V), para almacenar los colores de los nodos y la cola del BFS.
 */
bool esRojiblanco(int num_vertices, const vector<vector<int>> &adj, vector<int> &color)
{
    if (num_vertices < 1)
    {
        throw invalid_argument("El número de vértices debe ser al menos 1.");
    }

    color.assign(num_vertices, -1); 
    queue<int> q;

    for (int start_node = 0; start_node < num_vertices; ++start_node)
    {
        if (color[start_node] == -1)
        {
            color[start_node] = 0; 
            q.push(start_node);

            while (!q.empty())
            {
                int u = q.front();
                q.pop();

                for (int v : adj[u])
                {
                    if (color[v] == -1)
                    {
                        color[v] = 1 - color[u]; 
                        q.push(v);
                    }
                    else if (color[v] == color[u])
                    {
                        return false;
                    }
                }
            }
        }
    }

    return true;
}

int main()
{
    string input;
    while (true)
    {
        cout << "Menú principal:" << endl;
        cout << "1. Comprobar si un grafo es bipartito (rojiblanco)." << endl;
        cout << "q. Salir." << endl;
        cout << "Seleccione una opción: ";
        cin >> input;

        if (input == "q")
        {
            cout << "Saliendo del programa..." << endl;
            break;
        }
        else if (input == "1")
        {
            int v, a;
            cout << "Ingrese el número de vértices (0 para salir): ";
            cin >> v;
            if (v == 0)
            {
                cout << "Saliendo al menú principal..." << endl;
                continue;
            }

            cout << "Ingrese el número de aristas: ";
            cin >> a;
            vector<vector<int>> adj(v);
            cout << "Ingrese las aristas (formato: u w):" << endl;
            for (int i = 0; i < a; ++i)
            {
                int u, w;
                cin >> u >> w;
                adj[u].push_back(w);
                adj[w].push_back(u);
            }

            vector<int> color;
            try
            {
                if (esRojiblanco(v, adj, color))
                {
                    cout << "SI" << endl;
                    cout << "Colores asignados a los nodos:" << endl;
                    for (int i = 0; i < v; ++i)
                    {
                        cout << "Nodo " << i << ": " << (color[i] == 0 ? "Rojo" : "Blanco") << endl;
                    }
                }
                else
                    cout << "NO" << endl;
            }
            catch (const invalid_argument &e)
            {
                cerr << "Error: " << e.what() << endl;
            }
        }
        else
        {
            cout << "Opción no válida. Intente de nuevo." << endl;
        }
    }
    return 0;
}