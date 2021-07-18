/**
 * @author      : Guilherme Wachs Lopes (gwachs@fei.edu.br)
 * @file        : Pilhas
 * @created     : quarta set 30, 2020 21:38:00 -03
 */

#include <iostream>
#include <vector>

using namespace std;

// _______________________________________
//< Não alterar o main, nem o TestaPilha >
// ---------------------------------------
//        \   ^__^
//         \  (oo)\_______
//            (__)\       )\/\
//                ||----w |
//                ||     ||
//

template <typename T>
class AbstractStack {
private:
public:
    AbstractStack (){};
    virtual bool push (T x) = 0;
    virtual T pop (bool* ok) = 0;
    virtual void clear () = 0;
    virtual ~AbstractStack (){};
    virtual int size () = 0; // <--- Método Novo
};

template <typename T>
class LinkedStack;

template <typename T>
class StackNode {
private:
    T value;
    StackNode* next;

public:
    T getValue () {
        return value;
    }

    friend class LinkedStack<T>;
};

template<typename T>
class LinkedStack : public AbstractStack <T>{
private:
    StackNode<T>* top;
    T n;

    void clone (const LinkedStack& other) {
        top = nullptr;
        StackNode<T>* pOther = other.top;
        StackNode<T>* pThis = nullptr;
        StackNode<T>* lastInserted = nullptr;


        while (pOther != nullptr) {
            pThis = new StackNode<T>;
            pThis->value = pOther->value;
            pThis->next = nullptr;

            if (lastInserted) {
                lastInserted->next = pThis;
            } else {
                top = pThis;
            }
            lastInserted = pThis;

            pOther = pOther->next;
        }
    }

public:
    LinkedStack () : top (nullptr), n (0) {
    }

    LinkedStack (const LinkedStack& other): top(nullptr), n (0) {
        clone (other);
    }

    LinkedStack& operator= (const LinkedStack& other) {
        clear ();
        clone (other);
        return *this;
    }

    int size(){
       return n;
    }

    bool push (T x) {
        //Adaptar para atualizar size
        StackNode<T>* newNode = new StackNode<T>;
        if (!newNode)
            return false;
        newNode->value = x;
        newNode->next = top;
        top = newNode;
        n++;
        return true;
    }


    T pop (bool* ok = nullptr) {
        //Adaptar para atualizar size
        if (!top) {
            if (ok)
                *ok = false;
            return int ();
        }

        StackNode<T>* temp = top->next;
        T r = top->value;
        delete top;
        top = temp;
        if (ok)
            *ok = true;

        n--;
        return r;
    }

    void clear () {
        //Adaptar para atualizar size
        StackNode<T>* t = top;
        while (t != nullptr) {
            StackNode<T>* temp = t->next;
            delete t;
            t = temp;
        }
        n=0;
    }

    ~LinkedStack () {
        clear ();
    }
};

void testaPilha () {
    LinkedStack<int> s;
    s.push (9);
    s.push (6);
    s.push (5);
    s.push (8);
    LinkedStack<int> s2;
    s2 = s;

    bool ok;
    int r = s.pop (&ok);
    while (ok) {
        cout << r << endl;
        r = s.pop (&ok);
    }

    r = s2.pop (&ok);
    while (ok) {
        cout << r << endl;
        r = s2.pop (&ok);
    }
}


bool checaExpressao (string s) {
    LinkedStack<char>* stack = new LinkedStack<char>;
    for (int i = 0; i < s.size(); i++) {
        if (s[i] == '{' || s[i] == '[' || s[i] == '(') {
            stack->push(s[i]);
        }
        else if (s[i] == '}' || s[i] == ']' || s[i] == ')') {
            char c = stack->pop();
            if (s[i] == '}' && c != '{' || s[i] == ']' && c != '[' || s[i] == ')' && c != '(') {
                return false;
            }
        }
    }

    if (stack->size() > 0){
        return false;
    }

    return true;
}

int main () {
    vector<string> v = {
            "{ 2 + 3 + [ 2 - 3 ] * ( 1 + 2 + [ 3 / 1 ] ) }", // OK
            "{ 2 + 3 + ( 2 - 3 ] * ( 1 + 2 + [ 3 / 1 ] ) }", // Falha
            "{ 23 + [ 5 ] * ( 1 + 2 + [ 3 / 1 ) ] }", // Falha
            "{ 2 + [ 2 - 3 ] * ( 1 + 2 + [ 3 / 1 ] ) }", // Ok
            "2 + 3", // Ok
            "2 + 3 )", // Falha
            "2 + 3 }", // Falha
            "{ 2 ", // Falha
    };



    testaPilha ();
    cout << "Fim do teste da pilha" << endl;

    for (auto& e : v) {
        bool r = checaExpressao (e);
        if (r)
            cout << "Expressao Ok" << endl;
        else
            cout << "Expressao Falhou" << endl;
    }


    return 0;
}