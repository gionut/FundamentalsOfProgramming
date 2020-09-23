from Ui import Console
from Controller import SentenceController
from Repository import FileRepo

repoSentences = FileRepo('sentences')

sentenceController = SentenceController(repoSentences)

console = Console(sentenceController)

console.run()