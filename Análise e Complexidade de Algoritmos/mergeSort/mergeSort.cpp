/**
 * @author      : Guilherme Wachs Lopes (gwachs@fei.edu.br)
 * @file        : mergeSort
 * @created     : quinta mar 25, 2021 19:18:18 -03
 */

#include <algorithm>
#include <chrono>
#include <iostream>
#include <random>
#include <vector>

using namespace std;

void merge(vector<int> &v, int l, int p, int r) { // Theta(n)
  vector<int> s;
  int e = l, d = p + 1;
  while (e <= p && d <= r) { // passa n número
    if (v[e] < v[d]) {
      s.push_back(v[e]);
      e++;
    } else {
      s.push_back(v[d]);
      d++;
    }
  }

  while (e <= p) {
    s.push_back(v[e]);
    e++;
  }

  while (d <= r) {
    s.push_back(v[d]);
    d++;
  }

  copy(s.begin(), s.end(), v.begin() + l);
}

void mergeSort(vector<int> &v, int l, int r) {
  // cout << "MS(" << l << ", " << r << ");" << endl;
  if (l < r) {
    int p = (l + r) / 2;
    mergeSort(v, l, p);
    mergeSort(v, p + 1, r);
    merge(v, l, p, r);
  }
}

int main() {

  random_device dev;
  mt19937 rng(dev());
  uniform_int_distribution<mt19937::result_type> dist100(1, 100);

  for (int i = 100; i < 100000; i += 1000) {

    vector<int> l;
    for (int j = 0; j < i; j++) {
      l.push_back(dist100(dev));
    }
    chrono::steady_clock::time_point tInicio = chrono::steady_clock::now();

    mergeSort(l, 0, l.size() - 1);

    auto tFim = chrono::steady_clock::now();
    cout << i << "\t"
         << chrono::duration_cast<chrono::nanoseconds>(tFim - tInicio).count()
         << "" << endl;
  }

  return 0;
}
