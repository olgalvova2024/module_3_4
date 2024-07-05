def single_root_words(root_word, *other_word):
    same_word = []
    for i in range(len(other_word)):
        if ( root_word.lower() in other_word[i].lower() or other_word[i].lower() in root_word.lower() ):
            same_word.append(other_word[i])
    print('Входящий список:', root_word, other_word)
    print("'Однокоренные:'", same_word)


single_root_words('ака', 'собАка', 'АКСАКАЛ', 'ложка', 'нАкАл', 'осока', 'атака', 'арка', 'мАКАка')
single_root_words('апЕЛьсиновый', 'апельсин', 'сок')
single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')