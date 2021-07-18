/**
 * @author      : Guilherme Wachs Lopes (gwachs@fei.edu.br)
 * @file        : LDE
 * @created     : quinta ago 27, 2020 22:58:52 -03
 */

// _________________________
/// Alterar apenas a Classe \
//\ LinkedQueue             /
// -------------------------
//        \   ^__^
//         \  (oo)\_______
//            (__)\       )\/\
//                ||----w |
//                ||     ||
//
//
#include <cstdlib>
#include <iostream>
#include <new>
#include <set>


using std::cout;
using std::endl;

template <typename T>
class AbstractQueue {
public:
  virtual bool enqueue (T value) = 0;
  virtual bool dequeue (T* outElement = nullptr) = 0;
  virtual void clear () = 0;
  virtual ~AbstractQueue () {
  }
};

template <typename T>
class LinkedQueue;

template <typename T>
class QueueNode {
private:
  int value;
  QueueNode* next;
  friend class LinkedQueue<T>;

public:
  static std::set<void*> allocs;
  ~QueueNode () {
  }
  void* operator new (size_t n) {
    auto x = malloc (n);
    allocs.insert (x);
    return x;
  }

  void operator delete (void* p) {
    if (allocs.erase (p) == 0) {
      cout << "ERRO DE DESALOCACAO" << endl;
    };
    free (p);
  }
};

template <typename T>
std::set<void*> QueueNode<T>::allocs;

template <typename T>
class LinkedQueue : public AbstractQueue<T> {
private:
  QueueNode<T>* first;
  QueueNode<T>* last;
  int n;

public:
  LinkedQueue () {
    first = nullptr;
    last = nullptr;
    n = 0;
  }

  // Construtor por cópia (l chega como other)
  LinkedQueue (const LinkedQueue& other) {
    copy (other);
  }

  void copy (const LinkedQueue& other) {
    if(other.first == nullptr) return;
    
    QueueNode<T>* tmp = other.first;

    this->first = new QueueNode<T>();
    this->first->value = tmp->value;
    this->first->next = nullptr;

    QueueNode<T>* current = this->first;

    tmp = tmp->next;

    while (tmp->next != nullptr)
    {
        current->next = new QueueNode<T>();
        current = current->next;
        current->value = tmp->value;
        current->next = nullptr;
        tmp = tmp->next;
    }

    this->last = new QueueNode<T>();
    this->last->value = tmp->value;
    this->last->next = nullptr;
    current->next = this->last;
    this->n = other.n;
  }

  LinkedQueue& operator= (const LinkedQueue& other) {
    clear ();
    copy (other);
    return *this;  }

  bool enqueue(T value)
  {
    QueueNode<T>* newNode = new QueueNode<T>();

    if (!newNode)
        return false;

    newNode->value = value;
    newNode->next  = nullptr;

    if (first)
    {
        this->last->next = newNode;
        this->last       = newNode;
    }
    else
    {
        this->first = newNode;
        this->last  = newNode;
    }

    this->n++;
    return true;
  }

  bool dequeue (T* outElement = nullptr) {
    if(n == 0) return false;
    if (!this->first)
        return false;

    if (outElement)
        *outElement = this->first->value;

    QueueNode<T>* tmp = this->first;
    this->first = tmp->next;
    delete tmp;
    n--;       
    return true;      
  }

  virtual void print () const {
    QueueNode<T>* tmp = first;
    while (tmp) {
      cout << tmp->value << " ";
      tmp = tmp->next;
    }
    cout << endl;
  }

  unsigned int getSize () {
    return n;
  }

  void clear () {
    QueueNode<T>* current = this->first;

    while(current != nullptr)
    {
        current = current->next;
        delete this->first;
        this->first = current;
    }

    delete current;
    n = 0;
  }

  ~LinkedQueue () {
    cout << "destrutor invocado" << endl;
    clear ();
  }
};


int main () {
  // NÃO ALTERAR O MAIN
  {
    LinkedQueue<int> l;
    int temp;
    cout << "==========TESTE 1==========" << endl;

    l.enqueue (5);
    l.enqueue (6);

    cout << "Tamanho: " << l.getSize () << endl;

    {
      cout << "==========TESTE 2==========" << endl;
      cout << "Construtor por copia sera invocado" << endl;
      LinkedQueue<int> l2 = l;
      l2.enqueue (10);
      l2.enqueue (11);
      l2.enqueue (15);
      int temp;
      while (l2.dequeue (&temp)) {
        cout << "Removido de l2 " << temp << endl;
      }
      l2.enqueue (13);
      l2.enqueue (19);
      cout << "imprimindo l2:" << endl;
      l2.print ();
      l2.clear ();
      cout << "imprimindo l2:" << endl;
      l2.print ();
    }
    cout << "==========TESTE 2 acabou===" << endl;
    {
      cout << "==========TESTE 3==========" << endl;
      LinkedQueue<int> l3;
      cout << "Atribuicao por copia sera invocado" << endl;
      l3 = l;
      l3.enqueue (50);
      l3.enqueue (51);
      l3.enqueue (55);
      int temp;
      while (l3.dequeue (&temp)) {
        cout << "Removido de l3 " << temp << endl;
      }
      l3.enqueue (53);
      l3.enqueue (59);
      cout << "imprimindo l3:" << endl;
      l3.print ();
      l3.clear ();
      cout << "imprimindo l3:" << endl;
      l3.print ();
      cout << "==========TESTE 3 acabou===" << endl;
    }

    cout << "imprimindo l:" << endl;
    l.print ();

    l.enqueue(4);
    l.dequeue (&temp);
    cout << temp << endl;
    l.enqueue (8);

    l.print ();
  }

  if (QueueNode<int>::allocs.size ())
    cout << "Existem nos alocados" << endl;
  cout << "==========TESTE 1 acabou===" << endl;

  return 0;
}
