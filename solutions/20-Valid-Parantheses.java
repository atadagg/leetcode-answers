import java.util.Stack;

class Solution {

public static boolean isValid(String s) {		
    Stack<Character> newStack = new Stack();

	if(s.length() == 1 || s.charAt(0) == ')' ||s.charAt(0) == ']' || s.charAt(0) == '}') {
		return false;
	}


		for (int i = 0; i < s.length(); i++) {
			if(s.charAt(i) == '(' ||s.charAt(i) == '[' || s.charAt(i) == '{') {
				newStack.push(s.charAt(i));
				System.out.println(s.charAt(i));
			} else {
                if(newStack.isEmpty()) {
					return false;
				}
				if(s.charAt(i) == ')' && newStack.pop() != '(') {
					return false;
				} else if(s.charAt(i) == ']' && newStack.pop() != '[') {
					return false;
				} else if(s.charAt(i) == '}' && newStack.pop() != '{') {
					return false;
				}
			}
			
			
		}
		
		if(newStack.isEmpty()) {
			return true;
		} else {
			return false;
		}
	    	
	    	
	    	
	    	
	}
}
