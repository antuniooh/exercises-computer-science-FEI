package Ex02;

public class PhoneBook {
    private String nome;
    private String telefone;

    public PhoneBook(String nome, String telefone) {
        this.nome = nome;
        this.telefone = telefone;
    }

    public PhoneBook() {
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getTelefone() {
        return telefone;
    }

    public void setTelefone(String telefone) {
        this.telefone = telefone;
    }

    @Override
    public String toString() {
        return "PhoneBook{" + "nome=" + nome + ", telefone=" + telefone + '}';
    }
    
    
}
