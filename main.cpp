#include <iostream>
#include <string>
using namespace std;
const int max_size = 1000;
class Stack {
    private:
        char arr[max_size];
        int top;

    public:
        Stack() {
            top = -1;
            
        }
        
        bool Empty() {
                return top == -1;
            }
        bool Full() {
                return top == max_size - 1;
            }
        
        bool push(char c) {
            if (Full()) {
                cout << "You have reached the maximum number of elements for the stack" << endl;
                return false;
            }
            arr[++top] = c;
            return true;
        }
        
        char pop() {
            if (Empty()) {
                cout << "The stack is empty so there is nothing to pop out" << endl;
                return '0';
            }
            return arr[top--];
        }
        
        char read() const {
                if (top < 0) return '0';
                return arr[top];
            }
};
class PDA {
    private:
        enum State {Start, letter, ParanthesesBracketsOpen, retT, retF};
        Stack stack;
    public:
        PDA() : current_state(Start) {};
        State current_state = Start;
        bool ProcessChar(char c) {
            if (!ValidCharacter(c)) {
                current_state = retF;
                return false;
            }
            switch(current_state) {
                case Start:
                    stack.push('$');
                    if (Alphabet(c)) {
                        current_state = letter;
                    } else if (c == '(' || c == '[') {
                        stack.push(c);
                        current_state = ParanthesesBracketsOpen;
                    } else if (c == ' ') {
                    } else if (c == '.') {
                        if (stack.read() == '$') {
                            stack.pop();
                            current_state = retT;
                        }
                        
                    } else {
                        current_state = retF;
                    }
                    break;
                    
                case letter:
                    if (Alphabet(c)) {
                        
                    } else if (c == '.') {
                        if (stack.read() == '$') {
                            stack.pop();
                            current_state = retT;
                        } else {
                            current_state = retF;
                        }
                    } else if (c == ' ') {
                        
                    } else if (c == '(' || c == '[') {
                        stack.push(c);
                        current_state = ParanthesesBracketsOpen;
                    } else {
                        current_state = retF;
                    }
                    break;
                    
                case ParanthesesBracketsOpen:
                    if (Alphabet(c)) {
                        
                    } else if (c == ')' || c == ']' ) {
                        if (stack.Empty() || !MatchingPair(stack.read(), c)) {
                            current_state = retF;
                        } else {
                            stack.pop();
                        }
                        
                    } else if (c == '(' || c == '[' ) {
                        stack.push(c);
                    } else if (c == ' ') {
                        
                    } else if (c == '.') {
                        if (stack.read() == '$') {
                            stack.pop();
                            current_state = retT;
                        }
                    } else {
                        current_state = retF;
                    }
                    break;
                
                    
                case retT:
                case retF:
                    return false;
                    
                    
            }
            return true;
        }
            
        bool IsAccepted() const {
            return current_state == retT;
        }
    
        bool MatchingPair(char open, char close) {
            return (open == '(' && close == ')') || (open == '[' && close == ']');
        }
        bool ValidCharacter(char c) {
            return Alphabet(c) || c == ' '|| c == '.' || c == '(' || c == ')' || c == '[' || c == ']';
        }
    
        bool Alphabet(char cc) {
            return cc == 'a' || cc == 'b' || cc == 'c' || cc == 'd' || cc == 'e' || cc == 'f' || cc == 'g' || cc == 'h' || cc == 'i' || cc == 'j' || cc == 'k' || cc == 'l' || cc == 'm' || cc == 'n' || cc == 'o' || cc == 'p' || cc == 'q' || cc == 'r' || cc == 's' || cc == 't' || cc == 'u' || cc == 'v' || cc == 'w' || cc == 'x' || cc == 'y' || cc == 'z';
        }
    
};

int main() {
    PDA pda;
    string input;

    cout << "Enter a string (alphabet {a-z, ' ', (, ), [, ] }) followed by '.': ";
    getline(cin, input);


    for (char c : input) {
        if (!pda.ProcessChar(c)) {
            break;
        }
    }

    if (pda.IsAccepted()) {
        cout << "String is accepted" << endl;
    } else {
        cout << "String is not accepted" << endl;
    }

    return 0;
}
