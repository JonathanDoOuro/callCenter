class Operator:
    '''This class represents a telephone operator'''

    def __init__(self, id):
        self._id = id 
        self._states = ['available', 'ringing', 'busy']
        self._state = 'available'
        self._callId = 0 #in this context 0 means no call

    #Getters and Setters
    def setState(self, state):
        if(state in self._states):
            self._state = state

    def setCallId(self, callId):
        self._callId = callId

    def getCallId(self):
        return self._callId

    def getState(self):
        return self._state

    def getId(self):
        return self._id