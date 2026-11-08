from wordCounter import count_words

class TestWordCounter(unittest.TestCase):
    def test_normal_sentence(self):
        self.assertEqual(count_words("I love python"),3)

    def test_single_word(self):
            self.assertEqual(count_words("hello"),1)

    def test_empty_string(self):
         self.assertEqual(count_words(""),0)

    def test_word_exists(self):
         self.assertIn("python","i love python")

    def test_not_equal(self):
         self.assertNotEqual(count_words("i love pyhton"),5)





if __name__ == "__main__":
     unittest.main()