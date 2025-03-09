import ollama
import time
import logging


def test_leetcode():
    return """
    Task LeetCode: Recover a Tree From Preorder Traversal

    We run a preorder depth-first search (DFS) on the root of a binary tree.

    At each node in this traversal, we output D dashes (where D is the depth of this node), then we output the value of this node.  If the depth of a node is D, the depth of its immediate child is D + 1.  The depth of the root node is 0.

    If a node has only one child, that child is guaranteed to be the left child.

    Given the output traversal of this traversal, recover the tree and return its root.

    Example 1:

    Input: traversal = "1-2--3--4-5--6--7"
    Output: [1,2,5,3,4,6,7]

    Example 2:

    Input: traversal = "1-2--3---4-5--6---7"
    Output: [1,2,5,3,null,6,null,4,null,7]

    Example 3:

    Input: traversal = "1-401--349---90--88"
    Output: [1,401,null,349,88,90]

    Constraints:

    The number of nodes in the original tree is in the range [1, 1000].
    1 <= Node.val <= 109

    Code example for leetcode:
    # Definition for a binary tree node.
    # class TreeNode:
    #     def __init__(self, val=0, left=None, right=None):
    #         self.val = val
    #         self.left = left
    #         self.right = right
    class Solution:
        def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
    """

def test_unittest():
    return """
    With Python and library unittest for Python write 4 or 5 unittests for this code, 
    which defines a file system iterator class using a generator:
    import os


    class FileSystemIterator:
        def __init__(self, root: str, only_files: bool = False, only_dirs: bool = False, pattern: str | None = None):
            
            self.root = root

            if not os.path.isdir(root):
                print(f"Path {root} does not exist")
                raise FileNotFoundError

            self.only_files = only_files
            self.only_dirs = only_dirs

            if only_dirs and only_files:
                print("Choose one or none")
                raise ValueError

            self.pattern = pattern or ""

            self.result = self.get_all_elements()

        def get_pattern(self, directory: str, elements: list):
            for element in elements:
                if self.pattern in element:
                    yield os.path.join(directory, element)


        def get_all_elements(self):
            for dirpath, dirnames, dirfiles in os.walk(self.root):
                if not self.only_files:
                    yield from self.get_pattern(dirpath, dirnames)
                if not self.only_dirs:
                    yield from self.get_pattern(dirpath, dirfiles)


        def __iter__(self):
            return self


        def __next__(self):
            try:
                return next(self.result)
            except StopIteration:
                print("Generator is over")
                raise StopIteration
        """

def test_integral():
    return """
    Solve the integral: ∫(3x² + 2x + 1) dx.
    """

def test_equation():
    return """
    The parametric equations are given: 
    x = 2t + 1,
    y = t² - 3.
    Find dy/dx.
    """

def test_sentence_correct():
    return """
    Correct spelling and punctuation errors in this text written in Russian: 
    The quick brown fox jump over the lazy dog, but it didnt see the hole in the ground.
    She went to the store to buy apples bananas and oranges but she forgot her wallet at home.
    Their going to the park tomorow even though its supposed to rain all day.
    """

def test_write_poem():
    return """
    Write a poem for March 8 (International Women's Day)
    """
    
def test_write_story():
    return """
    Write a story about how the right and left mouse buttons had a fight and then made up.
    """

def test_retelling_text():
    return """
    Retell Chekhov's story "Chameleon". 
    In the story, police inspector Ochumelov tries to find out whose dog bit master Khryukin, 
    but his opinion changes depending on who the dog belongs to.
    """

def test_cross_text():
    return """
    Cross Chekhov's stories "Chameleon" and "The Man in a Case". 
    Imagine that Belikov (the hero of "The Man in a Case") witnessed the events of "Chameleon". 
    How would he react?
    """

def stress_test(num_requests, prompt):
    """
    Функция для стресс-тестирования модели.
    :param num_requests: Количество запросов.
    :param prompt: Текст запроса.
    :return: Статистика (среднее время обработки, количество ошибок).
    """
    logging.info(f"Начало стресс-тестирования с {num_requests} запросами...")
    total_time = 0
    success_count = 0
    error_count = 0

    for i in range(num_requests):
        logging.info(f"Запрос {i + 1}/{num_requests}")
        start_time = time.time()

        try:
            response = ollama.chat(
                model='deepseek-r1:1.5b',
                messages=[{"role": "user", "content": prompt}]
            )
            answer = response['message']['content']
            processing_time = time.time() - start_time
            logging.info(f"Ответ на запрос {i + 1}: {answer}")
            logging.info(f"Время обработки: {processing_time:.2f} секунд")
            total_time += processing_time
            success_count += 1
        except Exception as e:
            logging.error(f"Ошибка в запросе {i + 1}: {e}")
            error_count += 1

    # Итоговая статистика
    avg_time = total_time / success_count if success_count > 0 else 0
    logging.info(f"Стресс-тестирование завершено.")
    logging.info(f"Успешных запросов: {success_count}")
    logging.info(f"Ошибок: {error_count}")
    logging.info(f"Среднее время обработки: {avg_time:.2f} секунд")

    return avg_time, error_count