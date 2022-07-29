import java.io.*;
import java.util.*;

class Main
{
    public static void main (String args[]) throws IOException  // entry point from OS
    {
        int n;
	
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	StringTokenizer st = new StringTokenizer(br.readLine());
	n = Integer.parseInt(st.nextToken());

	StringTokenizer st2 = new StringTokenizer(br.readLine());
	long sum = 0;
	for(int a=0; a<n; a++){
		sum += Integer.parseInt(st2.nextToken());
	}
	System.out.println(sum);
    }
}