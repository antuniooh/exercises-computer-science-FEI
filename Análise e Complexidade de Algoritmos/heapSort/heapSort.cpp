/**
 * @author      : Guilherme Wachs Lopes (gwachs@fei.edu.br)
 * @file        : teste
 * @created     : terça abr 13, 2021 19:38:39 -03
 */

#include <iostream>
#include <vector>
#include <algorithm>



using namespace std;

int pai(int idx) { return (idx - 1) / 2; }

int fd(int idx) { return 2 * idx + 2; }
int fe(int idx) { return 2 * idx + 1; }

void sift(vector<int> &v, int idx, int n) {
  int maior = idx;
  if(fe(idx) < n  && v[fe(idx)] > v[maior] ){
    maior = fe(idx);
  }
  if(fd(idx) < n  && v[fd(idx)] > v[maior] ){
    maior = fd(idx);
  }

  if( maior != idx){
    //houve violação
    swap(v[idx], v[maior]);
    sift(v, maior, n);
  }
}

void makeHeap(vector<int> &v) {
  for (int i = pai(v.size() - 1); i >= 0; i--) {
    sift(v, i, v.size());
  }
}

void HeapSort(vector<int> &v){
  makeHeap(v);

  int n=v.size();
  for (int i = 0; i < v.size()-1; i++) {
    swap(v[0], v[n-1]);
    n--;
    sift(v, 0, n);
  }
}

int main() {

  vector<int> v = {8, 7, 7, 5, 7, 9, 10};

  HeapSort(v);

  for (auto& e : v) {
    cout << e << endl;
  }

  return 0;
}
