import java.io.*;
import java.util.*;

public class javaProc
{
	public static void main(String[] args)
	{
        Scanner in = new Scanner(System.in);
        String data = in.next();

        while (data.equals("x")==false)
        {
            System.out.println("Java received: " + data);
        }
	}

}