from Repository import FileRepo
from Validators import ValidateSentence
from Controller import SentenceController
from Ui import Console

repoSentences = FileRepo('sentences')

validateSentence = ValidateSentence()

sentenceController = SentenceController(repoSentences, validateSentence)

console = Console(sentenceController)

console.run()
