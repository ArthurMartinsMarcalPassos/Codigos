public class Calculadora{
    public int n1;
    public int n2; 
    
    public void soma(){
        System.out.println(n1+n2);
    }
    public void sub(){
        System.out.println(n1-n2);
    }
    public void  div(){
        System.out.println(n1*n2);
    }
    public void mult(){
        System.out.println(n1/n2);
    }
    
    public static void main (String[] args) {
        Calculadora cal= new Calculadora();
        
        cal.n1=20;
        cal.n2=20;
        
        cal.soma();
        cal.sub();
        cal.div();
        cal.mult();
    }
}