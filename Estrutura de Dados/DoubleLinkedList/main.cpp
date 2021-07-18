/**
 * @author      : Guilherme Wachs Lopes (gwachs@fei.edu.br)
 * @file        : LDE
 * @created     : quinta ago 27, 2020 22:58:52 -03
 */

// _________________________
/// Alterar apenas a Classe \
//\ DoubleLinkedList        /
// -------------------------
//        \   ^__^
//         \  (oo)\_______
//            (__)\       )\/\
//                ||----w |
//                ||     ||
//
//
#include <iostream>
#include <cstdlib>
#include <new>
#include <set>

using std::cout;
using std::endl;

// Tipo abstrato de dados
class AbstractOrderedList {
public:
  AbstractOrderedList () {
  }

  virtual bool insert (int value) = 0;
  virtual bool remove (int value) = 0;
  virtual bool search (int value) = 0;
  virtual int getAtIndex (int index) = 0;
  virtual unsigned int getSize () = 0;

  virtual void print () {
    for (int i = 0; i < getSize (); ++i) {
      cout << getAtIndex (i) << " ";
    }
    cout << endl;
  }


  virtual ~AbstractOrderedList () {
  }
};


class DoubleLinkedList;
class Node {
private:
  int value;
  Node* next;
  Node* previous;
  friend class DoubleLinkedList;

public:
  static std::set<void*> allocs;
  ~Node () {
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
std::set<void*> Node::allocs;

class DoubleLinkedList : public AbstractOrderedList {
private:
  Node* first;
  Node* last;
  int n;

public:
  DoubleLinkedList () {
    first = nullptr;
    last = nullptr;
    n = 0;
  }


  // Construtor por cópia (l chega como other)
  DoubleLinkedList (const DoubleLinkedList& other) {
    cout << "chamei o construtor por copia" << endl;
    copy (other);
  }

  void copy (const DoubleLinkedList& other) {
    Node* novo;
    first = nullptr;
    last = nullptr;
    Node* ptrAtualOther = other.first;
    while (ptrAtualOther) {
      Node* novo = new Node;
      novo->value = ptrAtualOther->value;
      novo->previous = nullptr;
      novo->next = nullptr;
      if (!first) {
        first = novo;
        last = novo;
      } else {
        last->next = novo;
        novo->previous = last;
        last = novo;
      }
      ptrAtualOther = ptrAtualOther->next;
    }

    n = other.n;
  }

  DoubleLinkedList& operator= (const DoubleLinkedList& other) {
    clear ();
    copy (other);
    return *this;
  }

  bool insert (int value) {
    // 1 alocar a memória
    // 2 setar os atributos do nó
    // 3 encontrar a posição de onde inserir
    // 4 ligar ponteiros
    // 5 n++
    // 6 return true

    // 1
    Node* novo = new Node;
    if (!novo)
      return false;
    // 2
    novo->next = nullptr;
    novo->previous = nullptr;
    novo->value = value;

    // 3
    Node* ptrAnt = nullptr;
    Node* ptrAtual = first;
    while (ptrAtual != nullptr && ptrAtual->value < value) {
      ptrAnt = ptrAtual;
      ptrAtual = ptrAtual->next;
    }

    // pra frente
    if (ptrAnt) {
      ptrAnt->next = novo;
    } else {
      first = novo;
    }
    novo->next = ptrAtual;

    // pra trás
    if (ptrAtual) {
      ptrAtual->previous = novo;
    } else {
      last = novo;
    }
    novo->previous = ptrAnt;

    // 5
    n++;
    return true;
  }

  bool remove (int value) {
    if (!search(value))
      return false;

    Node* it = first;

    while(it != nullptr){
      if(it->value == value){
        if(it->previous == nullptr && it->next == nullptr){
            first = nullptr;
            last = nullptr;
        }
        else if(it->previous == nullptr){
            it->next->previous = nullptr;
            first = it->next;
        }
        else if (it->next == nullptr){
          it->previous->next = nullptr;
          last = it->previous;
        }
        else{
          it->previous->next = it->next;
          it->next->previous = it->previous;
        }
        delete it;
        this->n--;
        return true;
      }
      it = it->next;
    }
    return false;
  }
  bool search (int value) {
    Node* it = first;
    while(it != nullptr){
      if(it->value == value){
        return true;
      }
      it = it->next;
    }

    return false;
  }

  int getAtIndex (int index) {
    Node* tmp = first;
    for (int i = 0; tmp != nullptr && i < index; i++) {
      tmp = tmp->next;
    }
    if (tmp != nullptr)
      return tmp->value;
    else
      return -1;
  }

  virtual void print () const {
    Node* tmp = first;
    while (tmp) {
      cout << tmp->value << " ";
      tmp = tmp->next;
    }
    cout << endl;
  }
  unsigned int getSize () {
    return 0;
  }

  void clear () {
    Node* tmp = first;
    Node* tmpNext;
    while (tmp) {
      tmpNext = tmp->next;
      delete tmp;
      tmp = tmpNext;
    }
  }

  ~DoubleLinkedList () {
    cout << "destrutor invocado" << endl;
    clear ();
  }
};


void ImprimeDoMeuJeito (const DoubleLinkedList x) {
  cout << "Vou imprimir" << endl;
  x.print ();
}

int main () {
  {
    // NÃO ALTERAR O MAIN
    DoubleLinkedList l;
    cout << (l.remove (0) ? "removi 0" : "nao removi") << endl;
    l.print ();
    cout << (l.insert (5) ? "inseri 5" : "nao inseri") << endl;
    l.print ();
    cout << (l.insert (85) ? "inseri 85" : "nao inseri") << endl;
    l.print ();
    cout << (l.insert (69) ? "inseri 69" : "nao inseri") << endl;
    l.print ();
    cout << (l.remove (5) ? "removi 5" : "nao removi") << endl;
    l.print ();
    cout << (l.insert (84) ? "inseri 84" : "nao inseri") << endl;
    l.print ();
    cout << (l.insert (83) ? "inseri 83" : "nao inseri") << endl;
    l.print ();
    cout << (l.remove (84) ? "removi 84" : "nao removi") << endl;
    l.print ();
    cout << (l.remove (83) ? "removi 83" : "nao removi") << endl;
    l.print ();
    cout << (l.insert (38) ? "inseri 38" : "nao inseri") << endl;
    l.print ();
    cout << l.search (85) << endl;
    cout << l.search (86) << endl;
    cout << (l.insert (856) ? "inseri 856" : "nao inseri") << endl;
    l.print ();
    cout << (l.insert (846) ? "inseri 846" : "nao inseri") << endl;
    l.print ();
    cout << (l.remove (856) ? "removi 856" : "nao removi") << endl;
    l.print ();
    cout << (l.insert (390) ? "inseri 390" : "nao inseri") << endl;
    l.print ();
    cout << (l.remove (390) ? "removi 390" : "nao removi") << endl;
    l.print ();
    cout << l.search (9000) << endl;
    cout << l.search (-1) << endl;

    {
      // Criando e excluindo uma "cópia"
      // Construtor por cópia
      DoubleLinkedList q = l;
      cout << (l.remove (5) ? "removi 5" : "nao removi") << endl;
      l.print ();
      cout << (l.remove (38) ? "removi 38" : "nao removi") << endl;
      l.print ();
      cout << (l.remove (69) ? "removi 69" : "nao removi") << endl;
      l.print ();
      cout << (l.remove (83) ? "removi 83" : "nao removi") << endl;
      l.print ();
      cout << (l.remove (84) ? "removi 84" : "nao removi") << endl;
      l.print ();
      cout << (l.remove (85) ? "removi 85" : "nao removi") << endl;
      l.print ();
      cout << (l.remove (390) ? "removi 390" : "nao removi") << endl;
      l.print ();
      cout << (l.remove (846) ? "removi 846" : "nao removi") << endl;
      l.print ();
      cout << (l.remove (856) ? "removi 856" : "nao removi") << endl;
      l.print ();
      cout << (l.remove (5) ? "removi 5" : "nao removi") << endl;
      l.print ();
      cout << (l.remove (38) ? "removi 38" : "nao removi") << endl;
      l.print ();
      cout << (l.remove (69) ? "removi 69" : "nao removi") << endl;
      l.print ();
      cout << (l.remove (83) ? "removi 83" : "nao removi") << endl;
      l.print ();
      cout << (l.remove (84) ? "removi 84" : "nao removi") << endl;
      l.print ();
      cout << (l.remove (85) ? "removi 85" : "nao removi") << endl;
      l.print ();
      cout << (l.remove (390) ? "removi 390" : "nao removi") << endl;
      l.print ();
      cout << (l.remove (846) ? "removi 846" : "nao removi") << endl;
      l.print ();
      cout << (l.remove (856) ? "removi 856" : "nao removi") << endl;
      l.print ();

      q = l;
      q.insert (800);
      cout << "Vou imprimir" << endl;
      ImprimeDoMeuJeito (q);
    }

    cout << "Vou imprimir" << endl;
    ImprimeDoMeuJeito (l);

    if (Node::allocs.size () != 0) {
      cout << "SOBRARAM PONTEIROS NAO DESALOCADOS" << endl;
    }
  }

  return 0;
}