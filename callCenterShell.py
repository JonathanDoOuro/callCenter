import cmd
import Operator

class CallCenterShell(cmd.Cmd):
    '''Shell that acepts commands'''
    intro = 'Welcome to the call center. Type help or ? to list commands.\n'
    prompt = '(Call Center): '
    #========constructor===============
    
    #=====avalible commands============
    def do_call(self, callId):
        print(f'Call {callId} received')
        for key, value in operators.items():
            if value.getState() == 'available':
                value.setState('ringing')
                value.setCallId(callId)
                print(f'Call {callId} ringing for operator {key}')
                break
        

    def do_answer(self, operatorId):
        operators[operatorId].setState('busy')
        print(f'Call {operators[operatorId].getCallId()} answered by operator {operatorId}')

    def do_reject(self, operatorId):
        operators[operatorId].setState('available')
        print(f'Call {operators[operatorId].getCallId()} rejected by operator {operatorId}')
        operators[operatorId].setCallId(0) 

    def do_hangup(self, callId):
        for key, value in operators.items():
            if value.getCallId() == callId:
                value.setState('available')
                value.setCallId(0)
                print(f'Call {callId}] finished and operator {key} available')

    #======help of each command========
    def help_call(self):
        print('makes the application receive a call whose id is <id>.')
    def help_answer(self):
        print('makes operator <id> answer a call being delivered to it.')
    def help_reject(self):
        print('makes operator <id> reject a call being delivered to it.')
    def help_hangup(self):
        print('makes call whose id is <id> be finished.')
    #===========set the operators==========
    def preloop(self):
        """Register the telephone Operators."""
        print('Please register the operators id you want to simulate. To finish the registration you must type "end".')
        while True:
            print("id: ", end ="")
            id = input()
            if(id == 'end'):
                break
            operators[id] = Operator.Operator(id)
            
    #=======ends the application========
    def do_EOF(self, line):
        return True



#==================MAIN================
if __name__ == '__main__':
    operators = dict()
    d = CallCenterShell()
    d.cmdloop()