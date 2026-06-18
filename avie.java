import java.util.*;
public class avie{
    
    List<Integer> kth= new ArrayList<>();
    public void kthlevel(Node root,int k, int level){
        
        level =0;
        if(root==null){
            return ;
        }
        if(level ==k){
            kth.add(root.data);
            return;

        }
        kthlevel(root.left,k, level+1);
        kthlevel(root.right,k,level+1);
        
    }
    
}