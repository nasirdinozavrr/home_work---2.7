class Bubble:
    def __init__(self, my_list ):
            self.my_list = my_list

    def bubble_sort(self):
        for i in range(len(self.my_list)-1, 0, -1):
            for j in range(i):
                if self.my_list[j] > self.my_list[j + 1]:
                    self.my_list[j], self.my_list[j + 1] = self.my_list[j + 1], self.my_list[j]

        return self.my_list

bubble = Bubble(my_list= [3, 1, 81, 35, 22])

print(bubble.bubble_sort())



class Quick:
    def __init__(self, my_list):
        self.my_list = my_list


    def quick_sort(self):
        if len(self.my_list) <= 1:
            return self.my_list
        element = self.my_list[0]
        left = list(filter(lambda num: num < element, self.my_list))
        center = [num for num in self.my_list if num == element]
        right = list(filter(lambda num: num > element, self.my_list))

        return left + center + right

q = Quick(my_list=[3, 1, 81, 35, 22])

print(q.quick_sort())


class Polindrome:
    def __init__(self, number):
        self.number = number

    def polindrome_str(self):
        for i in range(len(str(self.number))):
            if str(self.number) == str(self.number)[::-1]:
                return True
            else:
                return False

p = Polindrome(number=545)

print(p.polindrome_str())


