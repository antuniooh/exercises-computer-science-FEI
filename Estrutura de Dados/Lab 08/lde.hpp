/**
 * @author      : Guilherme Wachs Lopes (gwachs@fei.edu.br)
 * @file        : LDE
 * @created     : quinta ago 27, 2020 22:58:52 -03
 */
// 
//  __________________________ 
// ( NAO ALTERAR ESSE ARQUIVO )
//  -------------------------- 
//         o   ^__^
//          o  (oo)\_______
//             (__)\       )\/\
//                 ||----w |
//                 ||     ||
// 

#include <iostream>
#include <functional>

using std::cout;
using std::endl;
using std::less;


// Tipo abstrato de dados
template <typename T>
class AbstractOrderedList {
public:
  AbstractOrderedList () {
  }

  virtual bool insert (T value) = 0;
  virtual bool remove (T value) = 0;
  virtual T search (T value, bool* ok) = 0;
  virtual T getAtIndex (int index) = 0;
  virtual unsigned int getSize () = 0;

  virtual ~AbstractOrderedList () {
  }
};


template <typename T, typename LessFunc>
class LinkedList;

template <typename T, typename LessFunc>
class Node {
private:
  T value;
  Node<T, LessFunc>* next;

  friend class LinkedList<T, LessFunc>;

public:
  ~Node () {
  }
};

template <typename T, typename LessFunc=less<T>>
class LinkedList : public AbstractOrderedList<T> {
private:
  Node<T, LessFunc>* first;
  int n;
  LessFunc Less;

  bool DiffFunc(T a, T b){
    return Less(a,b) || Less(b,a);
  }

public:
  LinkedList () {
    first = nullptr;
    n = 0;
  }
  

  bool insert (T value) {
    Node<T, LessFunc>* newNode = new Node<T, LessFunc>;
    if (newNode == nullptr)
      return false;

    newNode->value = value;
    newNode->next = nullptr;

    Node<T, LessFunc>* ptrAnt = nullptr;
    Node<T, LessFunc>* ptrAtual = first;
    while (ptrAtual != nullptr && Less(ptrAtual->value, value)) {
      ptrAnt = ptrAtual;
      ptrAtual = ptrAtual->next;
    }

    if (ptrAnt != nullptr)
      ptrAnt->next = newNode;
    else
      this->first = newNode;

    newNode->next = ptrAtual;

    this->n++;
    return true;
  }

  bool remove (T value) {
    Node<T, LessFunc> *ptrAtual = first, *ptrAnterior = nullptr;
    while (ptrAtual && Less(ptrAtual->value, value)) {
      ptrAnterior = ptrAtual;
      ptrAtual = ptrAtual->next;
    }

    if (!ptrAtual || DiffFunc(ptrAtual->value, value))
      return false;

    if (ptrAnterior)
      ptrAnterior->next = ptrAtual->next;
    else
      first = ptrAtual->next;

    free (ptrAtual);

    this->n--;

    return true;
  }
  T search (T value, bool* ok=nullptr) {
    Node<T, LessFunc>* ptrAtual = first;
    while (ptrAtual && Less(ptrAtual->value, value)) {
      ptrAtual = ptrAtual->next;
    }
    if (!ptrAtual || DiffFunc(ptrAtual->value, value))
      if(ok){
        *ok=false;
        return T{};
      }

    if(ok)
      *ok = true;
    return ptrAtual->value;
  }

  T getAtIndex (int index) {
    Node<T, LessFunc>* tmp = first;
    for (int i = 0; tmp != nullptr && i < index; i++) {
      tmp = tmp->next;
    }
    if (tmp != nullptr)
      return tmp->value;
    else
      return T{};
  }

  virtual void print () {
    Node<T, LessFunc>* tmp = first;
    while (tmp) {
      cout << tmp->value << " ";
      tmp = tmp->next;
    }
    cout << endl;
  }
  unsigned int getSize () {
    return 0;
  }
  ~LinkedList () {
    Node<T, LessFunc>* tmp = first;
    Node<T, LessFunc>* tmpNext;
    while (tmp) {
      tmpNext = tmp->next;
      delete tmp;
      tmp = tmpNext;
    }
  }
};

