import re
from getconfig import settings

class Story:
    #the initial prompt is very special.
    #We want it to be permanently in the AI's limited memory (as well as possibly other strings of text.)
    def __init__(self, generator, prompt='', numResults=1):
        self.numResults=numResults
        self.story = []
        self.longTermMemory = []
        self.generator = generator
        self.prompt = prompt

    def act(self, action):
        assert(self.prompt+action)
        results=[]
        for i in range(self.numResults):
            assert(settings.getint('top-keks') is not None)
            results.append(
                    self.generator.generate(
                        self.getStory()+action,
                        self.prompt,
                        temperature=settings.getfloat('temp'),
                        top_p=settings.getfloat('top-p'),
                        top_k=settings.getint('top-keks'),
                        repetition_penalty=settings.getfloat('rep-pen')))
                    #self.longTermMemory.join('\n\n'), self.prompt))
            
        self.story.append([action, results])
        return results

    #only relevant when multiple results are supported
    #chosen result is always placed first, simplifies many things
    def chooseResult(self, num):
       results=self.story[1] 
       best=results.pop(num)
       results.insert(0,best)

    #Results 
    def getStory(self):
        lines = []
        for line in self.story:
            lines.append(line[0])
            lines.append(line[1][0])
        return '\n\n'.join(lines)

    def getSuggestion(self):
        #temporary fix (TODO)
        return re.sub('\n.*', '',
                self.generator.generate_raw(
                    self.getStory()+"\n\n> You",
                    self.prompt,
                    temperature=settings.getfloat('action-temp'),
                    top_p=settings.getfloat('top-p'),
                    top_k=settings.getint('top-keks'),
                    repetition_penalty=1))
                #, stop_tokens=['\n', '\n\n'])#longterm memory here

    def __str__(self):
        return self.prompt+self.getStory()

#    def save()
#        file=Path('saves', self.filename)
