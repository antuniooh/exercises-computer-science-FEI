import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Stack;

/**
 * @author : Guilherme Wachs Lopes (gwachs@fei.edu.br)
 * @file : linhaProducao
 * @created : quinta abr 22, 2021 20:20:39 -03
 */

public class linhaProducao {
  public static void ImprimeMenorCaminho(List<Integer> esc1, List<Integer> esc2, int escFim) {

    Stack<Integer> s = new Stack<>();
    s.push(escFim);
    for (int i = esc1.size() - 1; i >= 0; i--) {
      int ultimo = s.get(0);
      if (ultimo == 1) {
        s.push(esc1.get(i));
      } else {
        s.push(esc2.get(i));
      }
    }

    s.forEach((Integer x) -> {
      System.out.println(x);
    });
  }

  public static int MenorTempo(List<Integer> a1, List<Integer> a2, List<Integer> t1, List<Integer> t2, int e1, int e2,
      int s1, int s2) {

    List<Integer> acc1 = new ArrayList<>(a1.size());
    List<Integer> acc2 = new ArrayList<>(a1.size());
    List<Integer> esc1 = new ArrayList<>(a1.size());
    List<Integer> esc2 = new ArrayList<>(a1.size());

    acc1.add(e1 + a1.get(0));
    esc1.add(1);
    acc2.add(e2 + a2.get(0));
    esc2.add(2);

    for (int i = 1; i < a1.size(); i++) {
      // Linha 1
      acc1.add(acc1.get(i - 1) + a1.get(i));
      esc1.add(1);
      int tmp = acc2.get(i - 1) + t2.get(i - 1) + a1.get(i);
      if (tmp < acc1.get(i)) {
        acc1.set(i, tmp);
        esc1.set(i, 2);
      }

      // Linha 2
      acc2.add(acc2.get(i - 1) + a2.get(i));
      esc2.add(2);
      tmp = acc1.get(i - 1) + t1.get(i - 1) + a2.get(i);
      if (tmp < acc2.get(i)) {
        acc2.set(i, tmp);
        esc2.set(i, 2);
      }
    }

    int total1 = acc1.get(acc1.size() - 1) + s1;
    int total2 = acc2.get(acc2.size() - 1) + s2;


    ImprimeMenorCaminho(esc1,esc2,  ( (total1 < total2) ? 1 : 2) );

    return ((total1 < total2) ? total1 : total2);
  }

  public static void main(String[] args) {
    List<Integer> a1 = Arrays.asList(7, 9, 3, 4, 8, 4);
    List<Integer> a2 = Arrays.asList(8, 5, 6, 4, 5, 7);
    List<Integer> t1 = Arrays.asList(2, 3, 1, 3, 4);
    List<Integer> t2 = Arrays.asList(2, 1, 2, 2, 1);

    int e1 = 2, e2 = 4;
    int s1 = 3, s2 = 2;

    System.out.println(MenorTempo(a1, a2, t1, t2, e1, e2, s1, s2));
  }
}
