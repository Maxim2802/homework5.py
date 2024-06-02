# Практическое задание по теме: "Неизменяемые и изменяемые объекты. Кортежи и списки"

immutable_var_ = 1, 2, "banana", "lemon"
print(immutable_var_)
# immutable_var_[0][0] = 5
# print(immutable_var_) Изменить нельзя так как Ошибка  сообщает нам, что кортеж не поддерживает обращение по элементам
#                       ну либо по русски, нужно поставить квадртные скобки   xD
mutable_list = [1, 2, "lemon", True]
print(mutable_list)
mutable_list[0] = "apple"
mutable_list[1] = 675
mutable_list[2] = "watermelon"
mutable_list[3] = 27
print(mutable_list)