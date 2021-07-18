/**
 * @author      : Guilherme Wachs Lopes (gwachs@fei.edu.br)
 * @file        : main
 * @created     : quinta out 22, 2020 21:11:06 -03
 */

#include <iomanip>
#include <iostream>
#include <vector>


using namespace std;

template <typename T>
class Tree;

template <typename T>
class Node {
private:
  Node<T>* father;
  Node<T>* left;
  Node<T>* right;
  T value;
  int height;


public:
  T getValue () {
    return value;
  }
  Node () : father (nullptr), left (nullptr), right (nullptr), height(0) {
    value = T{};
  }
  Node (T value) : father (nullptr), left (nullptr), right (nullptr), value (value) {
  }

  friend class Tree<T>;
};

template <typename T>
class Tree {
private:
  Node<T>* root;
  int n;

  void print (Node<T>* x) {
    if (!x)
      return;

    print (x->left);
    cout << x->value << "\n";
    print (x->right);
  }

  void deleteSubTree (Node<T>* r) {
    if (!r)
      return;

    deleteSubTree (r->left);
    deleteSubTree (r->right);
    delete r;
  }

  void updateHeight(Node<T>* node){
    int l=-1;
    int r=-1;
    if(node->left)
      l=node->left->height;
    if(node->right)
      r=node->right->height;

    node->height = ((l>r) ? l : r);
    node->height++;
  }

  int child (Node<T>* n) {
    return (n->left != nullptr) + (n->right != nullptr);
  }

  Node<T>** fromParent (Node<T>* child) {
    if (child && child->father) {
      if (child->father->left == child)
        return &(child->father->left);
      else
        return &(child->father->right);
    }
    return nullptr;
  }

  Node<T>* sucessor (Node<T>* node) {
    node = node->right;
    while (node && node->left) {
      node = node->left;
    }
    return node;
  }

  bool remove (Node<T>* node) {
    if (!node)
      return false;

    Node<T>* father = node->father;

    if (child (node) == 0) {
      if (fromParent (node))
        *fromParent (node) = nullptr;
      else
        root = nullptr;

      delete node;
      n--;
      while(father){
        updateHeight(father);
        Balance(father);
        father=father->father;
      }
      return true;
    } else if (child (node) == 1) {
      Node<T>* son = node->left;
      if (!son)
        son = node->right;

      son->father = node->father;
      if (fromParent (node)) {
        *fromParent (node) = son;
      } else {
        root = son;
      }
      delete node;
      n--;
      while(father){
        updateHeight(father);
        Balance(father);
        father=father->father;
      }
      return true;
    } else {
      Node<T>* s = sucessor (node);
      node->value = s->value;
      return remove (s);
    }

  }


public:
  Tree () : root (nullptr), n (0) {
  }

  bool insert (T value) {
    Node<T>* novo = new Node<T> (value);
    if (!novo)
      return false;

    if (!root) {
      root = novo;
      n++;
      return true;
    }

    Node<T>* atual = root;
    Node<T>* anterior = nullptr;

    while (atual) {
      anterior = atual;

      if (value <= atual->value)
        atual = atual->left;
      else
        atual = atual->right;
    }

    novo->father = anterior;
    if (value <= anterior->value)
      anterior->left = novo;
    else
      anterior->right = novo;

    n++;

    novo=novo->father;
    while(novo){
      updateHeight(novo);
      Balance(novo);
      novo=novo->father;
    }

    return true;
  }

  Node<T>* search (T value) {
    Node<T>* atual = root;
    while (atual) {
      if (value < atual->value)
        atual = atual->left;
      else if (value > atual->value)
        atual = atual->right;
      else
        return atual;
    }
    return nullptr;
  }

  void print () {
    print (root);
  }

  void printDeitada (Node<T>* n, int nivel = 0) {
    if (!n)
      return;

    printDeitada (n->right, nivel + 1);

    for (int i = 0; i < nivel; i++) {
      cout << "     ";
    }
    cout << "    /" << endl;
    for (int i = 0; i < nivel; i++) {
      cout << "     ";
    }
    cout << setw (4) << n->getValue () << "(" << n->height << ")[" << BalanceFactor(n) << "]" << setw (0) << endl;
    for (int i = 0; i < nivel; i++) {
      cout << "     ";
    }
    cout << "    \\" << endl;

    printDeitada (n->left, nivel + 1);
  }

  void printDeitada () {
    //NÃO ALTERAR!
    cout << "=====================================================" << endl;
    printDeitada (root);
    cout << "=====================================================" << endl;
  }

  bool remove (T value) {
    return remove (search (value));
  }

  ~Tree () {
    deleteSubTree (root);
  }

  int BalanceFactor(Node<T>* node){
    int r = node->right ? node->right->height : -1;
    int l = node->left ? node->left->height : -1;
    return r-l;
  }

  void LeftRotate (Node<T>* X) {
    Node<T>* Y = X->right;
    Node<T>* b = Y->left;

    X->right = b;
    if (b)
      b->father = X;

    if (fromParent (X)) {
      *fromParent (X) = Y;
    } else {
      root = Y;
    }
    Y->father = X->father;

    Y->left = X;
    X->father = Y;

    while(X){
      updateHeight(X);
      X=X->father;
    }
  }

  void Balance(Node<T>* node){
    if(BalanceFactor(node) >= 2){
      if(BalanceFactor(node->right) < 0){
        RightRotate(node->right);
      }
      LeftRotate(node);
    }else if(BalanceFactor(node) <= -2){
      if(BalanceFactor(node->left) > 0){
        LeftRotate(node->left);
      }
      RightRotate(node);
    }
  }

  void RightRotate (Node<T>* X) {
    Node<T>* Y = X->left;
    Node<T>* b = Y->right;

    X->left = b;
    if (b)
      b->father = X;

    if (fromParent (X)) {
      *fromParent (X) = Y;
    } else {
      root = Y;
    }
    Y->father = X->father;

    Y->right = X;
    X->father = Y;

    while(X){
      updateHeight(X);
      X=X->father;
    }
  }
};
int main () {
  Tree<int> v;
  v.insert (315);
  v.insert (25);
  v.insert (325);
  v.insert (962);
  v.insert (687);
  v.insert (778);
  v.insert (695);
  v.printDeitada();
  v.insert (245);
  v.insert (299);
  v.insert (135);
  v.insert (50);
  v.insert (307);
  v.insert (640);
  v.printDeitada();
  cout << "=====================================" << endl;
  v.insert (564);
  v.insert (222);
  v.insert (913);
  v.insert (105);
  v.insert (279);
  v.insert (45);
  v.insert (826);
  v.insert (75);
  v.insert (495);
  v.insert (962);
  v.insert (913);
  v.remove (315);
  cout << "=====================================" << endl;
  v.printDeitada();
  v.remove (25);
  v.remove (325);
  v.remove (962);
  v.remove (687);
  v.remove (778);
  v.remove (695);
  v.remove (245);
  v.remove (299);
  v.remove (135);
  v.remove (50);
  v.remove (307);
  v.printDeitada();
  cout << "=====================================" << endl;
  v.remove (640);
  v.remove (564);
  v.remove (222);
  v.remove (913);
  v.remove (105);
  v.remove (279);
  v.remove (45);
  v.remove (826);
  v.remove (75);
  v.remove (495);
  v.remove (962);
  v.remove (913);
  v.printDeitada();
  cout << "=====================================" << endl;

  return 0;
}