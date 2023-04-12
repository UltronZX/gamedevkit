import time

class Timer():
    def __init__(self):
        self.start = time.time()
        self.pausestart = 0
        self.pausetime = 0
        self.resettime = -1
        self.alarmtime = -1
        self.STATE = 'running'
        self.ALARM = False
        
    def reset(self):
        '''Resets the timer.'''
        self.start = time.time()
        self.pausestart = 0
        self.pausetime = 0
        
    def get_time(self):
        '''Returns the current time on the timer'''
        if self.STATE == 'running':
            return time.time() - self.start - self.pausetime
        else:
            return self.pausestart - self.start - self.pausetime
        
    def pause(self):
        '''Pauses the timer,the timer does not update as far as it is paused.'''
        if self.STATE == 'running':
            self.STATE = 'paused'
            self.pausestart = time.time()
            
    def resume(self):
        '''Resumes the paused timer, now the timer works normally.'''
        if self.STATE == 'paused':
            self.STATE = 'running'
            self.pausetime += time.time() - self.pausestart
            
    def stop(self):
        '''Pauses the timer and returns the current time on the timer.'''
        self.pause()
        return self.get_time()
    
    def set_alarm(self,sectime):
        '''Sets the ALARM variable to True when the timer reaches the specific time.
        The update function needs to be called repeatedly (in a loop) for this function to work.'''
        self.alarmtime = sectime
    
    def off_alarm(self):
        '''Sets the ALARM variable to False.'''
        self.ALARM = False
    
    def auto_reset(self,sectime):
        '''Makes the alarm reset automatically after reaching a certain time.
        The update function needs to be called repeatedly (in a loop) for this function to work.'''
        self.resettime = sectime
        
    def off_auto_reset(self):
        '''Disables the auto reset function, the the timer runs infinitely.'''
        self.resettime = -1
        
    def update(self):
        '''Needs to be called repeatedly in a loop for auto_reset() and set_alarm() to work.'''
        if self.alarmtime > -1 and self.get_time() >= self.alarmtime:
            self.ALARM = True
        if self.resettime > -1 and self.get_time() >= self.resettime:
            self.reset()
