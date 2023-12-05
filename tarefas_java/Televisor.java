public class Televisor 
{
 public boolean ligado;
 public int volume;
 public int canal;
  
 public <volume> void aumentarvolume(volume){
    if (volume<30) volume++;
  }
 public void reduzirvolume(){
	if (volume>0) volume--;
  }
 public void trocarcanal(int canal){
	 this.canal=canal
	 
  }
 public void String mostrador(){
   return "Canal" + canal + "Volume" + volume;
	 }
 public void ligartv(){
    boolean = true
    }
 public void desligartv(){
    boolean = false
    }
  
}