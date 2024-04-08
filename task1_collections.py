""" Соберите уникальные имена преподавателей """


def find_unique_mentors(mentors):
    # Добавьте в список всех преподавателей со всех курсов
    all_list = sum(mentors, [])

    # Сделайте список all_names_list, состоящий только из имён, и заполните его
    all_names_list = []
    for mentor in all_list:
        all_names_list.append(mentor.split()[0])

    unique_names = [sorted(set(all_names_list))]
    result = str()
    for unique_name in unique_names:
        result += ', '.join(unique_name)

    return result


""" Узнайте топ-3 популярных имён """


def top_unique_names(mentors):
    all_list = sum(mentors, [])

    # Сделайте список all_names_list, состоящий только из имён, и заполните его
    all_names_list = []

    for mentor in all_list:
        all_names_list.append(mentor.split()[0])

    unique_names = [sorted(set(all_names_list))]
    result = str()
    for unique_name in unique_names:
        result += ', '.join(unique_name)

    # Уникальные имена будут в unique_names
    unique_ = result.split(',')
    # for name in unique_names:
    for name in unique_:
        unique_names.append(name.strip())

    # Подсчитайте встречаемость каждого имени через list.count()
    popular = []
    for i in all_names_list:
        for j in unique_names:
            if i == j:
                popular.append([i, all_names_list.count(i)])
        # Добавьте подсчёт имён
    res = []
    [res.append(x) for x in popular if x not in res]

    # Это код для сортировки списка с элементами вида [имя, количество] по убыванию встречаемости
    # Используйте его, как есть, или напишите собственный :)
    res.sort(key=lambda x: x[1], reverse=True)
    # Получите топ-3 часто встречающихся имён из списка popular
    # Подсказка: возьмите срез списка
    top_3 = res[0:3]
    top_3_parse = []
    for name, count_name in top_3:
        top_3_parse.append(f'{name}: {count_name} раз(а)')
        result = ', '.join(top_3_parse)

    return result


""" Суперимена: преподаватели с какими именами учат сразу на двух курсах? """


def super_mentors(mentors, courses):
    # Делаем список списков имён
    mentors_names = []
    for mentor in mentors:
        names = []
        for name in mentor:
            names.append(name.split()[0])
        mentors_names += [sorted(set(names))]

    # # Храните здесь пары курсов, в которых есть совпавшие имена
    # # # Попарное сравнение "наборов" преподавателей на курсах. Каждую новую пару запоминаем для исключения повторов.
    pairs = []
    text = ''
    result_list = []
    for id1 in range(len(mentors_names)):
        for id2 in range(len(mentors_names)):
            if id1 == id2:
                continue
            else:
                intersection_set = set(mentors_names[id1]) & set(mentors_names[id2])

                if len(intersection_set) > 0:
                    pair = {courses[id1], courses[id2]}
                    if pair not in pairs:
                        pairs.append(pair)
                        text = f"На курсах '{courses[id1]}' и '{courses[id2]}' преподают: {', '.join(sorted(intersection_set))}"
                        result_list.append(text)

    result = '\n'.join(result_list)
    return result

