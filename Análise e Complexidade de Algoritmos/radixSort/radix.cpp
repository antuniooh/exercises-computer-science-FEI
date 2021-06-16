#include <iostream>
#include <vector>

using namespace std;

int digito(int num, int dig){
  for (int i= 0; i < dig; i++){
    num /= 10;
  }
  return num % 10;
}

void countingSort(vector<int> &v, int d) {
    vector<int> counting(10,0);
    vector<int> temp = v;

  for(auto &e : v){
    counting[digito(e, d)]++;
  }

  for(int i = 1; i < counting.size(); i++){
    counting[i] +=counting[i -1];
  }

  for(int i = v.size() -1; i >=0; i--){
    temp[counting[digito(v[i], d)] -1] = v[i];
    counting[digito(v[i], d)] -=1;
  }

  v = temp;
}

int main() {
  vector<int> v={532,243,112,420,423,999,116};

  countingSort(v, 0);
  countingSort(v, 1);
  countingSort(v, 2);

  for(auto& e: v){
    cout << e << " ";
  }

  cout << endl; 
  return 0;
}