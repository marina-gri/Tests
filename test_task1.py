import unittest
from unittest import TestCase
from task1_collections import find_unique_mentors, top_unique_names, super_mentors
import pytest
import re



courses = ["Python-разработчик с нуля", "Java-разработчик с нуля", "Fullstack-разработчик на Python",
           "Frontend-разработчик с нуля"]

mentors = [
    ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев",
     "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков",
     "Роман Гордиенко"],
    ["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев",
     "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский",
     "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов",
     "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
    ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский",
     "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков",
     "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
    ["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин",
     "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
]


class TestUnittestCollections(TestCase):
    def test_find_unique_mentors(self):
        result = find_unique_mentors(mentors)
        expected = ('Адилет, Азамат, Александр, Алексей, Алена, Анатолий, Анна, Антон, Вадим, Валерий, '
                    'Владимир, Денис, Дмитрий, Евгений, Елена, Иван, Илья, Кирилл, Константин, Максим, Михаил, '
                    'Никита, Николай, Олег, Павел, Ринат, Роман, Сергей, Татьяна, Тимур, Филипп, Эдгар, Юрий')
        self.assertEqual(expected, result)

    def test_for_names(self):
        result = find_unique_mentors(mentors).split()
        for name in result:
            self.assertNotIn(" ", name)

    def test_len_of_list_popular_names(self):
        result = top_unique_names(mentors)
        pattern = r':\s\d+\sраз\(а\)'
        expected = re.sub(pattern, "", result)
        count_of_names = len(expected.split())
        self.assertEqual(3, count_of_names)

    def test_super_mentors_courses_in_one_pair(self):
        result = super_mentors(mentors, courses)
        result_list = result.split('\n')
        pattern = r'[A-Za-zа-яё-]+\s[а-я]+\s[A-Za-zа-я]+'

        for item in result_list:
            pair_of_courses = re.findall(pattern, item)
            self.assertNotEqual(pair_of_courses[0], pair_of_courses[1])

    def test_super_mentors_repetitions_of_courses_pairs(self):
        result = super_mentors(mentors, courses)
        result_list = result.split('\n')
        pattern = r'[A-Za-zа-яё-]+\s[а-я]+\s[A-Za-zа-я]+'

        unique_pairs_list = []
        for item in result_list:
            pair_of_courses = sorted(re.findall(pattern, item))
            self.assertNotIn(pair_of_courses, unique_pairs_list)
            unique_pairs_list.append(pair_of_courses)


class TestPytest:
    @pytest.mark.parametrize(
        'full_names, expected',
        (
                [[["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев",
     "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков",
     "Роман Гордиенко"], ["Максим Воронцов", "Евгений Грязнов"]],
                 'Азамат, Александр, Антон, Дмитрий, Евгений, Елена, Кирилл, Максим, Олег, Роман'],

            [[['Александр', 'Александр'], ['Кирилл']], 'Александр, Кирилл'],
        )

    )
    def test_pytest_find_unique_mentors(self, full_names, expected):
        result = find_unique_mentors(full_names)
        print(result)
        assert result == expected

    def test_pytest_for_names(self):
        result = find_unique_mentors(mentors).split()
        for name in result:
            assert " " not in name








