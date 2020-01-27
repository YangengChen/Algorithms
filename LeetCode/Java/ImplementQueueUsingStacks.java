package LeetCode.Java;

import java.util.Stack;

class MyQueue {

    Stack<Integer> stack;
    /** Initialize your data structure here. */
    public MyQueue() {
        stack = new Stack<>();
    }
    
    /** Push element x to the back of queue. */
    public void push(int x) {
        stack.push(x);
    }
    
    /** Removes the element from in front of queue and returns that element. */
    /** Recursively calling function calls N times, popping then restoring, 
     *  returning the most inner element.
    */
    public int pop() {
        int top = stack.pop();
        if(stack.isEmpty())
            return top;
        int front = this.pop();
        stack.push(top);
        return front;
    }
    
    /** Get the front element. */
    /** Recursively calling function calls N times, popping then restoring, 
     *  returning the most inner element.
    */
    public int peek() {
        int top = stack.pop();
        if(stack.isEmpty()) {
            stack.push(top);
            return top;
        }
        int front = this.peek();
        stack.push(top);
        return front;
    }
    
    /** Returns whether the queue is empty. */
    public boolean empty() {
        return stack.isEmpty();
    }
}

class MyQueue2 {

    Stack<Integer> inStack;
    Stack<Integer> outStack;
    /** Initialize your data structure here. */
    public MyQueue2() {
        inStack = new Stack<>();
        outStack = new Stack<>();
    }
    
    /** Push element x to the back of queue. */
    public void push(int x) {
        inStack.push(x);
    }
    
    /** Removes the element from in front of queue and returns that element. */
    public int pop() {
        if(outStack.isEmpty()) {
            while(!inStack.isEmpty())
                outStack.push(inStack.pop());
        }
        
        return outStack.pop();
    }
    
    /** Get the front element. */
    public int peek() {
        if(outStack.isEmpty()) {
            while(!inStack.isEmpty())
                outStack.push(inStack.pop());
        }
            
        return outStack.peek();
    }
    
    /** Returns whether the queue is empty. */
    public boolean empty() {
        return inStack.isEmpty() && outStack.isEmpty();
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */