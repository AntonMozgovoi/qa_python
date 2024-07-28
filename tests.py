import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_add_new_book_not_add_same_book(self):
        collector2 = BooksCollector()
        collector2.add_new_book('Титаник')
        collector2.add_new_book('Титаник')
        assert len(collector2.get_books_genre()) == 1

    @pytest.mark.parametrize('book_name', ['a'*10, 'b'*39, 'c'*40])
    def test_add_new_book_valid_name(self, book_name):
        collector3 = BooksCollector()
        collector3.add_new_book(book_name)
        assert book_name in collector3.books_genre

    def test_add_new_book_over40_symbols(self):
        collector4 = BooksCollector()
        collector4.add_new_book('a'*41)
        assert len(collector4.get_books_genre()) == 0

    def test_set_book_genre(self):
        collector5 = BooksCollector()
        collector5.add_new_book('Кладбище домашних животных')
        collector5.set_book_genre('Кладбище домашних животных','Ужасы')
        assert collector5.get_book_genre('Кладбище домашних животных') == 'Ужасы'

    def test_get_book_with_specific_genre(self):
        collector6 = BooksCollector()
        collector6.add_new_book('Град обреченный')
        collector6.set_book_genre('Град обреченный', 'Фантастика')
        assert collector6.get_books_with_specific_genre('Фантастика') == ['Град обреченный']

    def test_get_books_for_children_return_name(self):
        collector7 = BooksCollector()
        collector7.add_new_book('Смешарики')
        collector7.set_book_genre('Смешарики', 'Мультфильмы')
        assert collector7.get_books_for_children() == ['Смешарики']

    def test_add_book_in_favorites_get_favorites(self):
        collector8 = BooksCollector()
        collector8.add_new_book('Интерстеллар')
        collector8.add_book_in_favorites('Интерстеллар')
        assert 'Интерстеллар' in collector8.get_list_of_favorites_books()

    def test_delete_book_from_favorites_book_deleted(self):
        collector9 = BooksCollector()
        collector9.add_new_book('Капитал')
        collector9.add_book_in_favorites('Капитал')
        collector9.delete_book_from_favorites('Капитал')
        assert 'Капитал' not in collector9.get_list_of_favorites_books()