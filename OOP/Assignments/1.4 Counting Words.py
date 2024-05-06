import collections

word_guy = ('There once was a frog named Castelius. He was quite famous in his small town of Frogstalia,'
            'some may even refer to him as some sort of local legend. Despite Castelius\' stats, he found it quite'
            'difficult to find love. He tried so hard to woo the local ladies, but much to his dismay, his attempts'
            'were unsuccessful. One day, just as he was about to give up, Castelius stumbled upon a frog lady reading'
            'a book by the town fountain. He was quite familiar with the book, as it was one of his favourites. He'
            'approached the lady frog and asked how she thought of it so far, "Quite fascinating," she said. He was'
            'shocked, he had never encountered anyone who knew of his favourite book, let alone found it as'
            'captivating as he. He saw she was about half way through and asked how long she had been reading. "About'
            'three days now," she said. He was impressed. It took him many more days to get that far. He asked the lady'
            'if she wanted to start a reading club of sorts, as a way to improve his reading skills. "Of course!" she'
            'responded. He had never been more excited in his life, not even after slaying the great snake that'
            'threatened their town not too long ago. The two formed their little book club and spent the rest of their'
            'days reading and critiquing together and they lived happily ever after. THE END'
            ).casefold().split()
excluded_words = ['a', 'the', 'is', 'of', 'in', 'and', 'to']
dawg = []

for i in word_guy:
    if i not in excluded_words:
        word = ''
        for j in i:
            if j.isalnum():
                word += j
        dawg.append(word)

word_number = collections.Counter(word_guy).most_common(10)

print(word_number)