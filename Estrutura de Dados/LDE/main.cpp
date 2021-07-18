/**
 * @author      : Guilherme Wachs Lopes (gwachs@fei.edu.br)
 * @file        : hash
 * @created     : quinta out 08, 2020 10:58:51 -03
 */
#include <functional>
#include <iostream>
#include <ostream>

#include "lde.hpp"

// ________
//< Não altere o Main   >
//< Nem o arquivo ldde.h>
// ----------------------
//        \   ^__^
//         \  (@@)\___
//            (__)\       )\/\
//                ||----w |
//                ||     ||
//
using namespace std;

template <typename K, typename V>
struct KeyValue {
    K key;
    V value;
};

template <typename K, typename V>
struct KeyValueComp {
    bool operator() (KeyValue<K, V> a, KeyValue<K, V> b) {
        return a.key < b.key;
    }
};


template <typename K, typename V>
ostream& operator<< (ostream& out, const struct KeyValue<K, V>& p) {
    out << p.key << ":" << p.value;
    return out;
}

template <typename K, typename V>
class Dictionary {
public:
    virtual bool insert (KeyValue<K, V> item) = 0;
    virtual bool remove (K key) = 0;
    virtual V search (K key, bool* ok = nullptr) = 0;
    virtual int getSize () = 0;
    virtual void clear () = 0;
    virtual ~Dictionary () {
    }
};

template <typename K>
struct DefaultHashFunc {
    unsigned long long int operator() (K key) {
        return key;
    }
};

template <typename K, typename V, int MAX = 10, typename HashFunc = DefaultHashFunc<K>>
class HashDictionary {
private:
    // Declarar membros da classe

    LinkedList < KeyValue<K, V>, KeyValueComp<K, V> > ldes[MAX];
    int hash(int x){
        return x % MAX;
    }
    int n = 0;

public:
    HashDictionary () {
    }

    bool insert (KeyValue<K, V> item) {
        ldes[hash(item.key)].insert(item);
        n++;
    }

    bool remove (K key){
        ldes[hash(key)].remove({key, V{}});
        n--;
    };

    V search (K key, bool* ok = nullptr) {
        KeyValue<K, V> obj = ldes[(key%MAX)].search({key, V{}}, ok);

        if (ok)
            return obj.value;
        else
            return V{};
    }

    int getSize () {
        return n;
    }

    void clear () {
        for (int i = 0; i < MAX; i++) {
            ldes[i].clear ();
        }
        n=0;
    }

    ~HashDictionary () {
    }
};


int main () {
    // Não alterar o MAIN
    HashDictionary<int, string> h;
    h.insert ({ 76, "sponsored" });
    h.insert ({ 52, "technology" });
    h.insert ({ 27, "transfer" });
    h.insert ({ 26, "projects" });
    h.insert ({ 71, "developing" });
    h.insert ({ 38, "country" });
    h.insert ({ 77, "context" });
    h.insert ({ 18, "Journal" });
    h.insert ({ 13, "Technology" });
    h.insert ({ 78, "Transfer" });
    h.insert ({ 55, "Technology" });
    h.insert ({ 60, "transfer" });
    h.insert ({ 52, "effective" });
    h.insert ({ 31, "mechanism" });
    h.insert ({ 65, "advance" });
    h.insert ({ 17, "technological" });
    h.insert ({ 55, "development" });
    h.insert ({ 99, "developing" });
    h.insert ({ 90, "country’s" });
    h.insert ({ 99, "economy." });
    h.insert ({ 3, "Though" });
    bool ok;
    cout << h.search (90, &ok) << endl;
    cout << (ok ? "encontrou" : "nao encontrou") << endl << endl;

    cout << h.search (3, &ok) << endl;
    cout << (ok ? "encontrou" : "nao encontrou") << endl << endl;

    cout << h.search (60, &ok) << endl;
    cout << (ok ? "encontrou" : "nao encontrou") << endl << endl;


    cout << h.search (20, &ok) << endl;
    cout << (ok ? "encontrou" : "nao encontrou") << endl << endl;

    cout << h.search (18, &ok) << endl;
    cout << (ok ? "encontrou" : "nao encontrou") << endl << endl;


    cout << (h.remove (18) ? "removeu" : "nao removeu") << endl;


    cout << h.search (18, &ok) << endl;
    cout << (ok ? "encontrou" : "nao encontrou") << endl << endl;

    return 0;
}