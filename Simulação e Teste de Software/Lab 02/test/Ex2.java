package test;

//rtação das classes necessárias //layouts para alinhamento dos componentesimport java.awt.FlowLayout;import java.awt.GridLayout;//janelaimport javax.swing.JFrame;//butãoimport javax.swing.JButton;//caixa de seleção
import javax.swing.JComboBox;
import javax.swing.JFrame;
//inserção de texto e/ou imagem
import javax.swing.JLabel;
//classe Icon junto com ImageIcon anexão uma imagem a um Jlabel
import javax.swing.Icon;
import javax.swing.ImageIcon;
import javax.swing.JButton;
//exibição de textos numa pequena caixa de mensagens
import javax.swing.JOptionPane;
//painel
import javax.swing.JPanel;
//caixa de textos
import javax.swing.JTextArea;
//campo para inserção de valores ou caracteres
import javax.swing.JTextField;
import javax.swing.SwingConstants;
import javax.swing.plaf.FontUIResource;

//Evento para de ouvir um evento do botão
import java.awt.event.ActionListener;
import java.nio.charset.StandardCharsets;
//Evento de executar uma ação do evento que foi ouvido(ativado)
import java.awt.event.ActionEvent;
//Tratador de erros
import java.util.InputMismatchException;
import java.awt.FlowLayout;
import java.awt.Font;
import java.awt.GridLayout;

//Criação da classe EX2 extendendo a classe JFrame que foi importada
public class Ex2 extends JFrame {
    private String messageTy[] = {
            "Você está abaixo do peso recomendado.",
            "Você está muito bem! Continue assim!",
            "Você está acima do peso recomendado. Cuidado!",
            "<html><p style=\"width:200px\">Você está Obeso. Procure o acompanhamento de um nutricionista e realizar mais atividades físicas!</p></html>"
    };

    private String errorMessage = new String(
            "Há valores inválidos!\nEx: Use '.' ao invés de ',' para separar as casas decimais.\nVerifique se não foram inseridos valores negativos ou não-numéricos."
                    .getBytes(),
            StandardCharsets.UTF_8);

    private static String windowTitle = new String(
            "Cálculo do Indice de Massa Corporal (I.M.C.)".getBytes(),
            StandardCharsets.UTF_8);

    // numeros de pontos flutuantes (double)
    double altura, peso, imc;

    // criando um array já com os valores configurados do tipo double
    double imcs[] = { 18.5, 25, 30 };
    private String outputMessage = "";

    // criação do FlowLayout que alinha componentes da esquerda para a direita.
    private FlowLayout flowLayout = new FlowLayout();
    /*
     * criação de GridLayout com 4 linhas e 2 colunas com 10 de espaço em largura
     * e 1 de altura
     */
    private GridLayout gridLayout = new GridLayout(4, 2, 10, 1);
    private GridLayout outpuLayout = new GridLayout(2, 1, 10, 1);

    private JPanel gridJPanel = new JPanel();
    private JPanel outputPanel = new JPanel();

    // criação de dois botões com os nomes Calcular e Limpar Dados
    private JButton butao = new JButton("Calcular");
    private JButton butao2 = new JButton("Limpar Dados");
    private JLabel Laltura = new JLabel("Altura em cm:");
    private JLabel Lpeso = new JLabel("Peso em Kg:");
    private JLabel Lresultado = new JLabel("");
    private JLabel Limc = new JLabel("", SwingConstants.CENTER);
    private JTextField Faltura = new JTextField("", 5);
    private JTextField Fpeso = new JTextField("", 5);

    // construtor de Ex2 sem argumentos
    public Ex2() {
        // título da janela
        super(windowTitle);
        // alinhamento do frame com o uso do objeto flowLayout
        super.setLayout(flowLayout);
        // tamanho da janela
        setSize(370, 160);
        // inclusão dos componentes de maximinizar, miniminizar e fechar
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        gridJPanel.setLayout(gridLayout);

        gridJPanel.add(Laltura);
        gridJPanel.add(Faltura);
        gridJPanel.add(Lpeso);
        gridJPanel.add(Fpeso);
        gridJPanel.add(butao);
        gridJPanel.add(butao2);

        outputPanel.setLayout(outpuLayout);

        outputPanel.add(Limc);
        outputPanel.add(Lresultado);

        // adiciona a janela principal
        super.add(gridJPanel);
        super.add(outputPanel);

        butao.addActionListener(
                new ActionListener() {
                    // ao clicar no butao2 de nome limpar chama o método limpar
                    public void actionPerformed(ActionEvent event) {
                        Calculos();
                    }
                } // Fim da classe interna anônima
        );

        // classe interna anônima para butao2
        butao2.addActionListener(
                new ActionListener() {
                    // ao clicar no butao2 de nome limpar chama o método limpar
                    public void actionPerformed(ActionEvent event) {
                        limpar();
                    }
                } // Fim da classe interna anônima
        ); // fim da chamada para addActionListerner
    }

    // método que realiza os calculos
    private void Calculos() {
        try // tratador de erros com try e catch
        {
            // pega e converte os caracteres em ponto flutuante do campo Faltura para a
            // variavel altura
            altura = Double.parseDouble(Faltura.getText());
            // converte para metros
            // da mesma forma com Fpeso para a variável peso
            peso = Double.parseDouble(Fpeso.getText());

            if (altura < 0 || peso < 0) {
                throw new NumberFormatException();
            }

            altura /= 100;
            // realiza calculos
            imc = peso / (altura * altura);
            /*
             * Se a imc corporal for menor do que o estabelecido pelo vetor configure a
             * variável
             * outputMessage com essa frase
             */
            if (imc < imcs[0]) {
                outputMessage = messageTy[0];
            } else if ((imc >= imcs[0]) && (imc < imcs[1])) {
                outputMessage = messageTy[1];
            } else if ((imc >= imcs[1]) && (imc < imcs[2])) {
                outputMessage = messageTy[2];
            } else {
                outputMessage = messageTy[3];
            }

            outputMessage = new String(outputMessage.getBytes(), StandardCharsets.UTF_8);

            System.out.println(outputMessage);

            // reconfigure o tamanho da tela
            setSize(370, 300);
            // configure a label Lresultado com a variável outputMessage
            Limc.setText(String.format("%.2f", imc));
            Limc.setFont(new Font("Arial", Font.BOLD, 40));

            Lresultado.setText(outputMessage);
        }
        // caso ocorra uma excessão(erro) exiba uma mensagem nua caixa de mensagem
        catch (NumberFormatException exception) {
            JOptionPane.showMessageDialog(this, errorMessage, "ERRO", JOptionPane.ERROR_MESSAGE);
            // limpe s campos e variáveis
            limpar();
        }
    }

    // método para limpar os dados da tela e retornar a tela ao seu tamanho original
    private void limpar() {
        Fpeso.setText("");
        Faltura.setText("");
        Lresultado.setText("");
        peso = 0;
        altura = 0;
        // substitua a imagem atual por essa
        setSize(300, 160);
    }
} // Fim da classe Ex2