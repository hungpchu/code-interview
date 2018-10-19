public class sum{
    
    public static int Sum(int start, int end){
        
       
        
        return (end - start + 1)*(start + end) / 2;
    }

     public static void main(String []args){
        System.out.println("Result = " +  Sum(1,100));
     }
}
