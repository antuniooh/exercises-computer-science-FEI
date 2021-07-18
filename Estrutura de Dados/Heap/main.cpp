/**
 * @author      : Guilherme Wachs Lopes (gwachs@fei.edu.br)
 * @file        : Heap
 * @created     : quarta out 14, 2020 22:20:47 -03
 */

#include <iostream>
#include <vector>

using namespace std;

class Heap {
private:
  vector<int> v;
  int n;

  int fe (int i) {
    return 2 * i + 1;
  }
  int fd (int i) {
    return 2 * i + 2;
  }
  int pai (int i) {
    return (i - 1) / 2;
  }
  int ultPai () {
    if (n <= 1)
      return -1;
    return pai (n - 1);
  }

  void sift (int i) {
    if (i > ultPai ()) {
      return;
    }

    // indice do maior filho
    int maiorFilho = fe (i);
    if (fd (i) < n && v[fd (i)] > v[maiorFilho]) {
      maiorFilho = fd (i);
    }

    if (v[maiorFilho] > v[i]) {
      swap (v[maiorFilho], v[i]);
      sift (maiorFilho);
    }
  }


public:
  Heap (vector<int> v) : v (v), n (v.size ()) {
    for (int i = ultPai(); i >= 0; i--) {
      sift(i);
    }
  }

  bool insert(int value){
      v.push_back(value);
      n++;
      int i;
      for(i = ultPai(); i > 0; i = pai(i))
        sift(i);
      sift(0);
      return true;
  }

  int remove(bool *ok = nullptr){
      if(n == 0) {
        if(ok)
          *ok = false;
        return v[0];
      }

    swap(v[0], v[n-1]);
    n--;
    sift(0);

    if(ok)
      *ok = true;

    return v[n];
  }

  void print(){
    for (int i = 0; i < n; i++) {
      cout << v[i] << " " ;
    }
    cout << endl;
  }
};

int main() {
  vector<int> v{ 1, 3, 2, 5, 6, 3, 2, 7, 5 };
  Heap h (v);
  h.insert (9);
  h.insert (0);
  bool ok;
  int x = h.remove (&ok);
  while (ok) {
    cout << "saiu " << x << endl;
    h.print ();
    x = h.remove (&ok);
  }

  return 0;
}