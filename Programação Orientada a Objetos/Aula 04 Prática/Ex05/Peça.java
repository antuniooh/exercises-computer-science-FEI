
package Ex05;

public class Peça {
    private String tipo;
    private String cor;
    private String posicao;

    public Peça(String tipo, String cor, String posicao) {
        this.tipo = tipo;
        this.cor = cor;
        this.posicao = posicao;
    }

    public Peça() {
    }

    public String getTipo() {
        return tipo;
    }

    public void setTipo(String tipo) {
        this.tipo = tipo;
    }

    public String getCor() {
        return cor;
    }

    public void setCor(String cor) {
        this.cor = cor;
    }

    public String getPosicao() {
        return posicao;
    }

    public void setPosicao(String posicao) {
        this.posicao = posicao;
    }

    @Override
    public String toString() {
        return "Pe\u00e7a{" + "tipo=" + tipo + ", cor=" + cor + ", posicao=" + posicao + '}';
    }
    
    
    
}
