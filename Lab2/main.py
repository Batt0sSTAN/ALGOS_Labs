import os
from datetime import datetime
from urllib.parse import urlparse


class Counter:
    def __init__(self, iterable=None):
        self.counts = {}
        
        if iterable is not None:
            self.update(iterable)

    def update(self, iterable):
        for item in iterable:
            if item in self.counts:
                self.counts[item] += 1
            else:
                self.counts[item] = 1

    def get(self, item) -> int:
        return self.counts.get(item, 0)

    def most_common(self, n: int) -> list:
        items_list = list(self.counts.items())
        
        items_list.sort(key=lambda x: x[1], reverse=True)
        
        return items_list[:n]

class HistoryNode:

    def __init__(self, url: str, is_bookmark: bool = False):
        self.url = url
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.is_bookmark = is_bookmark
        self.prev = None
        self.next = None
    @property
    def domain(self) -> str:
        parsed_url = urlparse(self.url if "://" in self.url else f"http://{self.url}")
        return parsed_url.netloc


class BrowserHistory:

    def __init__(self):
        self.all_history = []
        self.current = None

    def visit(self, url: str, is_bookmark: bool = False):
        if not url:
            print("Ошибка: URL не может быть пустым.")
            return

        new_node = HistoryNode(url, is_bookmark)
        self.all_history.append(new_node)

        if not self.current:
            self.current = new_node
        else:
            self.current.next = new_node
            new_node.prev = self.current
            self.current = new_node
        
        print(f"Посещено: {url}")

    def back(self) -> str:
        if not self.current or not self.current.prev:
            print("Достигнуто начало истории. Назад идти некуда.")
            return self.current.url if self.current else None
        
        self.current = self.current.prev
        print(f"Назад к: {self.current.url}")
        return self.current.url

    def forward(self) -> str:
        if not self.current or not self.current.next:
            print("Достигнута крайняя точка истории. Вперед идти некуда.")
            return self.current.url if self.current else None
        
        self.current = self.current.next
        print(f"Вперед к: {self.current.url}")
        return self.current.url

    def clear_history(self):
        self.all_history.clear()
        self.current = None
        print("История успешно очищена.")

    def search_by_domain(self, domain_keyword: str):
        if not domain_keyword:
            print("Ошибка: Ключевое слово для поиска не может быть пустым.")
            return

        filtered = [node for node in self.all_history if domain_keyword.lower() in node.domain.lower()]
        
        print(f"\nРезультаты поиска по домену '{domain_keyword}':")
        self._print_table(filtered)

    def display_full_history(self):
        """Вывод всей истории в виде таблицы."""
        print("\n=== ПОЛНАЯ ИСТОРИЯ ПОСЕЩЕНИЙ ===")
        self._print_table(self.all_history)

    def get_top_transitions(self, n: int = 3):
        if len(self.all_history) < 2:
            print("\nНедостаточно данных для формирования переходов.")
            return

        transitions = []
        for i in range(len(self.all_history) - 1):
            from_domain = self.all_history[i].domain
            to_domain = self.all_history[i+1].domain
            # Исключаем переходы на самого себя, если это необходимо по логике
            if from_domain != to_domain:
                transitions.append((from_domain, to_domain))

        counter = Counter(transitions)
        top_n = counter.most_common(n)

        print(f"\n=== ТОП-{n} ПЕРЕХОДОВ МЕЖДУ ДОМЕНАМИ ===")
        if not top_n:
            print("Нет переходов между различными доменами.")
            return

        print(f"{'Исходный домен':<15} -> {'Целевой домен':<15} | {'Кол-во переходов':<5}")
        print("-" * 75)
        for (src, dest), count in top_n:
            print(f"{src:<15} -> {dest:<15} | {count:<5}")

    def _print_table(self, nodes_list):
        """Вспомогательный метод для красивого вывода данных в виде таблицы."""
        if not nodes_list:
            print("История пуста.")
            return

        col_url = "URL"
        col_time = "Время посещения"
        col_bm = "Закладка"

        max_url_len = max(max(len(node.url) for node in nodes_list), len(col_url))

        header = f"| {col_url:<{max_url_len}} | {col_time:<20} | {col_bm:<10} |"
        separator = "-" * len(header)
        
        print(separator)
        print(header)
        print(separator)
        
        for node in nodes_list:
            bookmark_status = "Да" if node.is_bookmark else "Нет"
            current_marker = " <(Текущая)" if node == self.current else ""
            
            print(f"| {node.url:<{max_url_len}} | {node.timestamp:<20} | {bookmark_status:<10} |{current_marker}")
        
        print(separator)


if __name__ == "__main__":
    browser = BrowserHistory()

    # 1. Тест граничных случаев на пустой истории
    print("--- Проверка пустой истории ---")
    browser.back()
    browser.forward()
    browser.display_full_history()

    print("\n--- Заполнение истории ---")
    browser.visit("google.com", is_bookmark=True)
    browser.visit("github.com/features")
    browser.visit("habr.com/ru/post/123", is_bookmark=True)
    browser.visit("google.com/search?q=python")
    browser.visit("github.com/trending")

    # Вывод таблицы
    browser.display_full_history()

    # 2. Тестирование навигации назад/вперед
    print("\n--- Навигация ---")
    browser.back()
    browser.back()     
    browser.forward()  

    # Переход по новому адресу
    browser.visit("youtube.com") 
    browser.display_full_history()
    browser.forward()  # Вперед идти некуда

    # 3. Поиск по домену
    browser.search_by_domain("github")
    browser.search_by_domain("google")

    # 4. Топ-N переходов
    browser.get_top_transitions(3)

    # 5. Очистка
    print("\n--- Очистка истории ---")
    browser.clear_history()
    browser.display_full_history()