/**
 * @author      : Guilherme Wachs Lopes (gwachs@fei.edu.br)
 * @file        : LDS
 * @created     : quarta set 09, 2020 21:35:09 -03
 */
//
//     _________________________________
//    / ALTERAR APENAS AS FUNÇÕES COM \
//    \ COMENTÁRIO "IMPLEMENTAR"       /
//     ---------------------------------
//            \   ^__^
//             \  (oo)\_______
//                (__)\       )\/\
//                    ||----w |
//                    ||     ||
//


#include <iostream>
#include <vector>

using namespace std;

// Tipo abstrato de dados
template <typename T>
class AbstractOrderedList {
public:
  AbstractOrderedList () {
  }

  virtual bool insert (T value) = 0;
  virtual bool remove (T value) = 0;
  virtual bool search (T value) = 0;
  virtual T getAtIndex (unsigned int index) = 0;
  virtual unsigned int getSize () = 0;

  virtual void print () {
    for (unsigned int i = 0; i < getSize (); ++i) {
      cout << getAtIndex (i) << " ";
    }
    cout << endl;
  }


  virtual ~AbstractOrderedList () {
  }
};

template <typename T>
class AbstractResizableOrderedList : public AbstractOrderedList<T> {
public:
  // redimensiona a estrutura de modo que capacity=size
  virtual void shrink_to_fit () = 0;
  // redimensiona estrutura para novo newCapacity
  virtual bool resize (unsigned int newCapacity) = 0;
  virtual unsigned int capacity () = 0;


  virtual ~AbstractResizableOrderedList () {
  }
};


template <typename T>
class LDS : public AbstractResizableOrderedList<T> {
private:
  T* v;
  unsigned int cap;
  unsigned int size;

public:
  LDS () {
    cap = 10;
    size = 0;
    v = new T[cap];
  }

  bool insert (T value) {
    // encontrar posição
    // deslocar elementos
    // adicionar
    // size++
    if (size == cap) {
      if (!this->resize (2 * cap)) {
        return false;
      }
    }

    int i;
    for (i = 0; i < size && v[i] < value; i++)
      ;

    for (unsigned int j = size; j > i; j--) {
      v[j] = v[j - 1];
    }

    v[i] = value;
    size++;
    return true;
  }

  bool resize (unsigned int newCap) {
    // Aloca area com o dobro do tamanho
    // copia elementos
    T* newV = new T[newCap];
    if (!newV) // newV == nullptr
      return false;

    cap = newCap;
    size = ((size > cap) ? cap : size);

    for (int i = 0; i < size; i++) {
      newV[i] = v[i];
    }
    delete[] v;
    v = newV;

    return true;
  }


  void shrink_to_fit () {
    this->cap = this->size;
  }

  unsigned int capacity () {
      return this->cap;
  }

  unsigned int getSize () {
      return this->size;
  }

  T getAtIndex (unsigned int index) {
    if(index > this->size || index < 0) return nullptr;
    return v[index];
  }

  bool search (T value) {
    int i = 0;
    while (i <= this->size) {
      if(v[i] == value)
        return true;
      i++;
    }
    return false;  }

  bool remove (T value) {
    if (!search(value))
      return false;

    int i = 0;
    while (i <= this->size) {
        if(v[i] == value){
            for(int j = i; j < size - 1; j++){
                v[j] = v[j + 1];
            }
            this->size--;
            return true;
        }
        i++;
    }
   
    return false;  
    }

  void print () {
    for (int i = 0; i < size; i++) {
      cout << v[i] << endl;
    }
  }

  ~LDS () {
    delete[] v;
  }
};


int main () {
  LDS<string> l;
  l.insert ("babbs");
  l.insert ("coldren");
  l.insert ("highinterest");
  l.insert ("loney");
  l.insert ("bangwe");
  l.insert ("datagrams");
  l.insert ("needers");
  l.insert ("proboscidial");
  l.insert ("pighead");
  l.insert ("warfel");
  l.insert ("verbed");
  l.insert ("cyprinidae");
  l.insert ("dalmard");
  l.insert ("unhumbled");
  l.insert ("belinuridae");
  l.insert ("malibu");
  l.insert ("tuitionary");
  l.insert ("pushball");
  l.insert ("gatehouse");
  l.insert ("goodsprings");
  l.insert ("disillusion");
  l.insert ("bidkar");
  l.insert ("misumalpan");
  l.insert ("nonadecane");
  l.insert ("nahor");
  l.insert ("bimahs");
  l.insert ("cade");
  l.insert ("mbwisi");
  l.insert ("urfirnis");
  l.print ();
  cout << "capacity: " << l.capacity () << endl;
  cout << "size: " << l.getSize () << endl;
  cout << "====================" << endl;
  l.resize (5);
  l.insert ("jihad");
  l.print ();
  cout << "capacity: " << l.capacity () << endl;
  cout << "size: " << l.getSize () << endl;
  cout << "====================" << endl;
  l.shrink_to_fit ();
  l.print ();
  cout << "capacity: " << l.capacity () << endl;
  cout << "size: " << l.getSize () << endl;
  cout << "====================" << endl;
  cout << (l.remove ("pighead") ? "removeu pighead" : "nao removeu pighead") << endl;
  cout << (l.remove ("babbs") ? "removeu babbs" : "nao removeu babbs") << endl;
  cout << (l.remove ("jihad") ? "removeu jihad" : "nao removeu jihad") << endl;
  l.print ();
  cout << "capacity: " << l.capacity () << endl;
  cout << "size: " << l.getSize () << endl;
  cout << "====================" << endl;
  l.insert ("nonadecane");
  l.insert ("nahor");
  l.insert ("bimahs");
  l.insert ("cade");
  l.insert ("mbwisi");
  l.print ();
  cout << "capacity: " << l.capacity () << endl;
  cout << "size: " << l.getSize () << endl;
  cout << "====================" << endl;

  return 0;
}
