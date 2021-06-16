/**
 * @author      : Guilherme Wachs Lopes (gwachs@fei.edu.br)
 * @file        : grafos
 * @created     : quinta mai 13, 2021 20:07:31 -03
 */

#include <algorithm>
#include <iostream>
#include <queue>
#include <vector>

using namespace std;

class Grafo {
private:
  vector<vector<int>> v;

public:
  Grafo(int N) { v.assign(N, vector<int>()); }

  const vector<int> &getNeightbors(int x) const { return v[x]; }

  int getNumNodes() { return v.size(); }

  void addEdge(int f, int t) {
    v[f].push_back(t);
    v[t].push_back(f);
  }

  void removeEdge(int f, int t) {
    auto iter = remove(v[f].begin(), v[f].end(), t);
    v[f].erase(iter);
    iter = remove(v[t].begin(), v[t].end(), f);
    v[t].erase(iter);
  }
};

class BFS {
private:
  Grafo g;
  vector<int> dist;
  vector<int> pai;

public:
  BFS(Grafo g) : g(g) {
    dist.assign(g.getNumNodes(), -1);
    pai.assign(g.getNumNodes(), -1);
  }

  void run(int start) {
    queue<int> fila;
    fila.push(start);
    dist[0] = 0;
    while (!fila.empty()) {
      int atual = fila.front();
      fila.pop();
      for (const auto &viz : g.getNeightbors(atual)) {
        if (dist[viz] == -1) {
          pai[viz] = atual;
          dist[viz] = dist[atual] + 1;
          fila.push(viz);
        }
      }
    }
  }

  void imprime() {
    cout << "Distancias: ";
    for (auto &e : dist) {
      cout << e << " ";
    }
    cout << endl;
    cout << "Pais: ";
    for (auto &e : pai) {
      cout << e << " ";
    }
  }
};

int main() {
  Grafo g(9);
  g.addEdge(0, 1);
  g.addEdge(0, 3);
  g.addEdge(0, 4);
  g.addEdge(1, 2);
  g.addEdge(2, 3);
  g.addEdge(4, 5);
  g.addEdge(3, 5);
  g.addEdge(3, 8);
  g.addEdge(4, 6);
  g.addEdge(4, 7);
  g.addEdge(5, 7);
  g.addEdge(6, 7);

  BFS bfs(g);
  bfs.run(0);
  bfs.imprime();

  return 0;
}
