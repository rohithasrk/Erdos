import java.lang.*;
import java.util.*;

public class p4{
	
	public static void main(String args[]){
		System.out.println(isPal("1"));
		long sum=0;
		for(long i=1;i<1000000000;i++){
			if(isPal(toHex(i))){
				if(isPal(toOct(i))){
					if(isPal(toBin(i))){
						sum+=i;
					}
				}
			}
		}
		System.out.println(sum);
	}
	
	public static String toHex(long n){
		String res="";
		while(n>0){
			int r=(int)n%16;
			if(r==10) res='a'+res;
			else if(r==11) res='b'+res;
			else if(r==12) res='c'+res;
			else if(r==13) res='d'+res;
			else if(r==14) res='e'+res;
			else if(r==15) res='f'+res;
			else res=r+res;
			n/=16;
		}
		return res;
	}
	
	public static String toBin(long n){
		String res="";
		while(n>0){
			int r=(int)n%2;
			res=r+res;
			n/=2;
		}
		return res;
	}
	
	public static String toOct(long n){
		String res="";
		while(n>0){
			int r=(int)n%8;
			res=r+res;
			n/=8;
		}
		return res;
	}
	
	public static boolean isPal(String s){
		int l=s.length();
		int r=l/2;
		for(int i=0;i<=r;i++){
			if(s.charAt(i)!=s.charAt(l-1-i)){
				return false;
			}
		}
		return true;
	}
}	
