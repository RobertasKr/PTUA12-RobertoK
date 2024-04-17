"""
Sukurti klasę, kurioje atributas butu "text".

Sukurti metodus, kurie:
	1. Suskaičiuotų kiek yra žodžių tekste;
	2. Metoda, kuris gražintų visus žodžius, kurie būtų nurodyti metodo kintamajame.
	Pvz nurodytos raidės 'ams', turi išrinkti visus žodžius, kurie turis šias raides.
	3. Išrinktų visus žožius, kurių ilgis didesnis arba lygus nurodytam metode;

Prasau pagalvoti ar Jūsų sprendime nėra kodo dubliavimo ir pagalvokite kaip jo išvengti.
"""


class Text_class:
    def __init__(self):
        self.text = "as esu vienas du trys keturi visi geria ir as gersiu o tu nebegersi sa sa ssssaaaa labas atuiops"
        self.splitted_text = (
            self.text.split()
        )  # sita vieta galima apsirasyti ir nenaudoti metodo split_text()

    def split_text(self):  # Sitas metodas realiai gaunasi nereikalingas
        result = self.text.split()
        return len(result)

    # def get_words(self, text_sample: str):
    #     result = []
    #     temp_var = []
    #     for word in self.splitted_text:
    #         for word_char in text_sample:
    #             if word_char in word:
    #                 temp_var.append(True)
    #             else:
    #                 temp_var.append(False)
    #         if all(temp_var):
    #             result.append(word)
    #         temp_var = []
    #     return result
    def get_words(self, text_sample: str) -> list:
        result = []
        for word in self.splitted_text:
            if all(letter in word for letter in text_sample):
                result.append(word)
        return result

    def get_words_longer_than(self, text_length: int):
        result = []
        for word in self.splitted_text:
            if len(word) >= text_length:
                result.append(word)
        return result


text_operation1 = Text_class()

print(text_operation1.split_text())
print(text_operation1.get_words("as"))
print(text_operation1.get_words_longer_than(3))
