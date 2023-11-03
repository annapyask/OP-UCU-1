"""
    Module for working with csv gradebook
"""
import copy


SYLABUS = {'Лабораторні роботи':{
            'Лабораторна робота 1': 1,
            'Лабораторна робота 2': 1,
            'Лабораторна робота 3': 2,
            'Лабораторна робота 4': 2 ,
            'Лабораторна робота 5': 2 ,
            'Лабораторна робота 6': 2 ,
            'Лабораторна робота 7': 2 ,
            'Лабораторна робота 8': 2 ,
            'Лабораторна робота 9': 2 ,
            'Лабораторна робота 10': 2,
            'Лабораторна робота 11': 2,
            'Лабораторна робота 12': 2},
           'Проміжний іспит':{
            'Теоретичне завдання': 2.5 ,
            'Завдання на програмування': 7.5},
           'Тести по лекційним матеріалам':{
            'Тест 1': 0.5,
            'Тест 2': 0.5,
            'Тест 3': 0.5,
            'Тест 4': 0.5,
            'Тест 5': 0.5,
            'Тест 6': 0.5,
            'Тест 7': 0.5,
            'Тест 8': 0.5,
            'Тест 9': 0.5,
            'Тест 10': 0.5,
            'Тест 11': 0.5},
           'Міні-проєкти':{
            'Міні-проєкт 1': 7.5,
            'Міні-проєкт 2': 7.5,
            'Міні-проєкт 3': 7.5},
           'Фінальний іспит':{
            'Теоретичне завдання': 10,
            'Завдання на програмування 1': 10,
            'Завдання на програмування 2': 10,
            'Завдання на програмування 3': 10},
           'Додаткові бали': 10
}


def read_gradebook(path: str, sylabus: dict[str, dict[str, int] | int]):
    """
    Return dict of student_data and dict-structure of activities
    { (surname, name, email, subgroup): { activity_group: {activity_name: None} } } 
    
    :param str path: path to csv file of students list:
    Sample csv file:
    ### START ###
    surname,name,email,subgroup
    Петренко,Василь,vasyl@ucu.edu.ua,BA
    ### END ###
    
    :param dict[str, dict[str, int] | int] sylabus: dict with list of activities
    and maximal grades of each. Ex
    {'Лаболаторні': {'Лаболаторна1': 2, 'Лаболаторна2':2}, 'Тест': 5}
    Each key of sylabus is int (max_grade) or nested dict of subactivities. But
    max nest-level is 1

    >>> test_sylabus = {'Test': 10, "Problems": {"Problem1": 10, "Problem2": 10}} 
    >>> test_csv_content = 'surname,name,email,subgroup\\nПетренко,Василь,vasyl@ucu.edu.ua,BA'
    >>> import tempfile 
    >>> with tempfile.NamedTemporaryFile(mode='w', delete=False) as tmpfile:
    ...     _ = tmpfile.write(test_csv_content)
    >>> read_gradebook(tmpfile.name, test_sylabus)
    {('Петренко', 'Василь', 'vasyl@ucu.edu.ua', 'BA'): {'Test': None, 'Problems':\
 {'Problem1': None, 'Problem2': None}}}
    """

    empty_gradebook = dict.fromkeys(sylabus, None)
    for activity_name, subactivities in sylabus.items():
        if isinstance(subactivities, dict):
            empty_activity = dict.fromkeys(subactivities, None)
        else:
            empty_activity = None
        empty_gradebook[activity_name] = empty_activity

    result = {}
    with open(path, 'r', encoding="utf-8") as gradebook_file:
        gradebook_file.readline()
        for line in gradebook_file:
            line_parts = line.split(",")
            students_key = tuple(line_parts[:4])
            result[students_key] = copy.deepcopy(empty_gradebook)

    return result


def delete_add_scores():
    pass


def delete_add_new_activity(dct_activities : dict, activity : str|dict) -> dict:
    '''
    (dict, str|dict) -> dict
    In case you want to delete the activity you should input dictionary of 
    activities and name of activity, which should be deleted. If you want to add
    the activity, you should input dictionary of activities and dictionary where 
    the actiity is a key and dictionary of subactivities and their points is a value.
    The function deletes given activity from the file if it's already there.
    If given activity isn't in the file, the function adds it.
    >>> delete_add_new_activity({'Лабораторні роботи':{'Лабораторна робота 1': 1,\
'Лабораторна робота 2': 1,'Лабораторна робота 3': 2,'Лабораторна робота 4': 2,\
'Лабораторна робота 5': 2,'Лабораторна робота 6': 2,'Лабораторна робота 7': 2,\
'Лабораторна робота 8': 2,'Лабораторна робота 9': 2,'Лабораторна робота 10': 2,\
'Лабораторна робота 11': 2,'Лабораторна робота 12': 2},\
'Проміжний іспит':{'Теоретичне завдання': 2.5 ,'Завдання на програмування': 7.5},\
'Тести по лекційним матеріалам':{'Тест 1': 0.5,'Тест 2': 0.5,'Тест 3': 0.5,\
'Тест 4': 0.5,'Тест 5': 0.5,'Тест 6': 0.5,'Тест 7': 0.5,'Тест 8': 0.5,\
'Тест 9': 0.5,'Тест 10': 0.5,'Тест 11': 0.5},\
'Міні-проєкти':{'Міні-проєкт 1': 7.5,'Міні-проєкт 2': 7.5,'Міні-проєкт 3': 7.5},\
'Фінальний іспит':{'Теоретичне завдання': 10,'Завдання на програмування 1': 10,\
'Завдання на програмування 2': 10,'Завдання на програмування 3': 10},\
'Додаткові бали': 10}, 'Тести по лекційним матеріалам')
    {'Лабораторні роботи': {'Лабораторна робота 1': 1, 'Лабораторна робота 2': 1, \
'Лабораторна робота 3': 2, 'Лабораторна робота 4': 2, 'Лабораторна робота 5': 2, \
'Лабораторна робота 6': 2, 'Лабораторна робота 7': 2, 'Лабораторна робота 8': 2, \
'Лабораторна робота 9': 2, 'Лабораторна робота 10': 2, 'Лабораторна робота 11': 2, \
'Лабораторна робота 12': 2}, \
'Проміжний іспит': {'Теоретичне завдання': 2.5, 'Завдання на програмування': 7.5}, \
'Міні-проєкти': {'Міні-проєкт 1': 7.5, 'Міні-проєкт 2': 7.5, 'Міні-проєкт 3': 7.5}, \
'Фінальний іспит': {'Теоретичне завдання': 10, 'Завдання на програмування 1': 10, \
'Завдання на програмування 2': 10, 'Завдання на програмування 3': 10}, \
'Додаткові бали': 10}
    >>> delete_add_new_activity({'Лабораторні роботи':{'Лабораторна робота 1': 1,\
'Лабораторна робота 2': 1,'Лабораторна робота 3': 2,'Лабораторна робота 4': 2,\
'Лабораторна робота 5': 2,'Лабораторна робота 6': 2,'Лабораторна робота 7': 2,\
'Лабораторна робота 8': 2,'Лабораторна робота 9': 2,'Лабораторна робота 10': 2,\
'Лабораторна робота 11': 2,'Лабораторна робота 12': 2},\
'Проміжний іспит':{'Теоретичне завдання': 2.5 ,'Завдання на програмування': 7.5},\
'Тести по лекційним матеріалам':{'Тест 1': 0.5,'Тест 2': 0.5,'Тест 3': 0.5,\
'Тест 4': 0.5,'Тест 5': 0.5,'Тест 6': 0.5,'Тест 7': 0.5,'Тест 8': 0.5,\
'Тест 9': 0.5,'Тест 10': 0.5,'Тест 11': 0.5},\
'Міні-проєкти':{'Міні-проєкт 1': 7.5,'Міні-проєкт 2': 7.5,'Міні-проєкт 3': 7.5},\
'Фінальний іспит':{'Теоретичне завдання': 10,'Завдання на програмування 1': 10,\
'Завдання на програмування 2': 10, 'Завдання на програмування 3': 10},\
'Додаткові бали': 10}, {'Командні випробування на додаткові бали': \
{'Випробування 1': 1, 'Випробування 2': 1, 'Випробування 3': 1, \
'Випробування 4': 1, 'Випробування 5': 1}})
    {'Лабораторні роботи': {'Лабораторна робота 1': 1, 'Лабораторна робота 2': 1, \
'Лабораторна робота 3': 2, 'Лабораторна робота 4': 2, 'Лабораторна робота 5': 2, \
'Лабораторна робота 6': 2, 'Лабораторна робота 7': 2, 'Лабораторна робота 8': 2, \
'Лабораторна робота 9': 2, 'Лабораторна робота 10': 2, 'Лабораторна робота 11': 2, \
'Лабораторна робота 12': 2}, \
'Проміжний іспит': {'Теоретичне завдання': 2.5, 'Завдання на програмування': 7.5}, \
'Тести по лекційним матеріалам': {'Тест 1': 0.5, 'Тест 2': 0.5, 'Тест 3': 0.5, \
'Тест 4': 0.5, 'Тест 5': 0.5, 'Тест 6': 0.5, 'Тест 7': 0.5, 'Тест 8': 0.5, \
'Тест 9': 0.5, 'Тест 10': 0.5, 'Тест 11': 0.5}, \
'Міні-проєкти': {'Міні-проєкт 1': 7.5, 'Міні-проєкт 2': 7.5, 'Міні-проєкт 3': 7.5}, \
'Фінальний іспит': {'Теоретичне завдання': 10, 'Завдання на програмування 1': 10, \
'Завдання на програмування 2': 10, 'Завдання на програмування 3': 10}, \
'Додаткові бали': 10, \
'Командні випробування на додаткові бали': \
{'Випробування 1': 1, 'Випробування 2': 1, 'Випробування 3': 1, \
'Випробування 4': 1, 'Випробування 5': 1}}
    '''
    if isinstance(activity, str) and activity in dct_activities:
        dct_activities.pop(activity)
    else:
        dct_activities.update(activity)
    return dct_activities


def get_student_total_score():
    pass


def get_list_of_students():
    pass


def get_avg_score():
    pass


def get_score_by_letter():
    pass


def get_students_with_talon():
    pass


def write_students_gradebook():
    pass


def write_gradebook_for_student():
    pass


def add_new_student():
    pass


def get_random_groups():
    pass


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
